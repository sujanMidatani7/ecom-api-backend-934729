from fastapi import FastAPI, Response, UploadFile, File, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from .models import File as FileModel
from .schemas import FileResponse
from .utils import encrypt_file, decrypt_file
import shutil
from .setting import TORTOISE_ORM

app = FastAPI()


@app.post("/upload", response_model=FileResponse)
async def upload_file(file: UploadFile = File(...)):
    """
    Uploads a file to the server and saves it in the 'app/static/uploads' directory.
    
    Args:
        file (UploadFile): The file to be uploaded.
        
    Returns:
        FileResponse: The response containing the details of the uploaded file.
    """
    file_location = f"app/static/uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    encrypt_file(file_location)

    db_file = await FileModel.create(
        filename=file.filename,
        file_path=file_location
    )
    
    return FileResponse.from_orm(db_file)

@app.get("/files/{file_id}")
async def get_file(file_id: int):
    """
    Retrieve a file by its ID.

    Parameters:
    - file_id (int): The ID of the file to retrieve.

    Returns:
    - Response: The decrypted file data as a response with media type "application/octet-stream".

    Raises:
    - HTTPException: If the file with the given ID is not found (status code 404).
    """
    file_record = await FileModel.get(id=file_id)
    if not file_record:
        raise HTTPException(status_code=404, detail="File not found")

    decrypted_data = decrypt_file(file_record.file_path)
    return Response(decrypted_data, media_type="application/octet-stream")

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

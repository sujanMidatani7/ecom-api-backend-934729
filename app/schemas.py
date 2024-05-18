from pydantic import BaseModel
import datetime
class FileResponse(BaseModel):
    """
    Represents a file response object.

    Attributes:
        id (int): The ID of the file.
        filename (str): The name of the file.
        file_path (str): The path of the file.
        created_at (datetime.datetime): The creation timestamp of the file.
    """

    id: int
    filename: str
    file_path: str
    created_at: datetime.datetime 

    class Config:
        orm_mode = True
        from_attributes=True

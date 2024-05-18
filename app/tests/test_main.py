import requests

# Base URL of your running FastAPI application
base_url = "http://127.0.0.1:8000"

def test_upload_file():
    """
    Test function to check file upload functionality.

    This function creates a test file, uploads it to the server using a POST request,
    and asserts that the response status code is 200.

    Returns:
        None
    """
    file_path = "test_file.txt"
    with open(file_path, "w") as f:
        f.write("This is a test file")

    with open(file_path, "rb") as f:
        response = requests.post(f"{base_url}/upload", files={"file": f})

    assert response.status_code == 200
    print("File upload test passed!")

def test_get_file():
    """
    Test case for retrieving a file using the API.

    Sends a GET request to the specified file endpoint and checks if the response status code is 200.
    Prints a success message if the test passes and also prints the response content if needed.
    """
    response = requests.get(f"{base_url}/files/{1}")

    assert response.status_code == 200
    print("File retrieval test passed!")
    
    print(response.content)

if __name__ == "__main__":
    test_upload_file()
    
    test_get_file()

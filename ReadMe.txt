📚 Book Library API
A simple and efficient RESTful API for managing a collection of books, built with Python and FastAPI. This project allows you to perform complete CRUD (Create, Read, Update, Delete) operations on a book library. 

✨ Features

Create, Read, Update, and Delete books. 

FastAPI Framework: Built using the modern, high-performance FastAPI framework.


SQLite Database: Uses a simple file-based SQLite database for data persistence. 


Input Validation: Checks for duplicate entries and invalid data (e.g., future publication years). 


Error Handling: Provides clear error messages for common issues, like not finding a book. 


Automatic Interactive Docs: Comes with interactive API documentation (Swagger UI) right out of the box. 

🛠️ Technology Stack
Python 3

FastAPI: The web framework used to build the API.

Uvicorn: The ASGI server used to run the application.

SQLite: The SQL database engine.

🚀 Getting Started
Follow these instructions to get the project up and running on your local machine.

Prerequisites
Make sure you have Python 3.8+ installed on your system.

Installation & Setup
Clone the repository:

Bash

git clone <your-repository-url>
cd <repository-folder>
Create a virtual environment (recommended):

On macOS and Linux:

Bash

python3 -m venv venv
source venv/bin/activate
On Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
Install the required packages:
The requirements.txt file contains all the necessary Python packages.

Bash

pip install -r requirements.txt
Run the API server:

Bash

uvicorn main:app --reload
The --reload flag makes the server restart automatically after code changes.

The API will now be running at http://127.0.0.1:8000.

📖 API Endpoints Documentation
This API provides endpoints to manage books.

Interactive Documentation
For a rich, interactive experience, run the server and navigate to:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Here you can view and test all the API endpoints directly from your browser!

Endpoint Details
1. Get All Books
Endpoint: /books/

Method: GET

Description: Retrieves a list of all books in the library.

Success Response (200 OK):

JSON

{
  "books": [
    {
      "id": 1,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "year": 1925
    },
    {
      "id": 2,
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "year": 1960
    }
  ]
}
Error Response (404 Not Found):

JSON

{
  "detail": "No books found"
}
2. Find a Specific Book
Endpoint: /find/

Method: GET

Description: Finds and retrieves a single book by its id.

Query Parameters:

id (integer, required): The unique ID of the book.

curl Example:

Bash

curl -X GET "http://127.0.0.1:8000/find/?id=1"
Success Response (200 OK):

JSON

{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925
}
Error Response (404 Not Found):

JSON

{
  "detail": "Book not found"
}
3. Add a New Book
Endpoint: /addbook/

Method: GET (Note: POST is conventionally used for creating resources)

Description: Adds a new book to the library.

Query Parameters:

title (string, required)

author (string, required)

year (integer, required)

curl Example:

Bash

curl -X GET "http://127.0.0.1:8000/addbook/?title=New%20Book&author=Some%20Author&year=2025"
Success Response (200 OK):

JSON

{
  "message": "Book 'New Book' added successfully!"
}
Error Responses:

409 Conflict: If a book with the same title, author, and year already exists.

422 Unprocessable Entity: If the year is in the future.

4. Update a Book
Endpoint: /updatebook/

Method: GET (Note: PUT or PATCH is conventionally used for updating resources)

Description: Updates the details of an existing book by its id.

Query Parameters:

id (integer, required)

title (string, required)

author (string, required)

year (integer, required)

curl Example:

Bash

curl -X GET "http://127.0.0.1:8000/updatebook/?id=1&title=Updated%20Title&author=Updated%20Author&year=2024"
Success Response (200 OK):

JSON

{
  "message": "Book with id 1 updated successfully!"
}
Error Response (404 Not Found):

JSON

{
  "detail": "Book not found"
}
5. Delete a Book
Endpoint: /deletebook/

Method: GET (Note: DELETE is conventionally used for deleting resources)

Description: Deletes a book from the library by its id.

Query Parameters:

id (integer, required): The unique ID of the book to delete.

curl Example:

Bash

curl -X GET "http://127.0.0.1:8000/deletebook/?id=1"
Success Response (200 OK):

JSON

{
  "message": "Book with id 1 deleted successfully!"
}
Error Response (404 Not Found):

JSON

{
  "detail": "Book not found"
}

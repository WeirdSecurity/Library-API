<div align="center">
  <h1>📚 BookAPI Library </h1>
  <p>A simple and efficient RESTful API for managing a collection of books, built with Python and FastAPI.</p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white" alt="Python 3.8+">
    <img src="https://img.shields.io/badge/FastAPI-005571.svg?logo=fastapi&logoColor=white" alt="FastAPI">
    <img src="https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white" alt="SQLite">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  </p>
</div>

---

### ✨ Features

- **Complete CRUD Operations:** Create, Read, Update, and Delete book records with ease.
- **High-Performance Framework:** Built using the modern, fast, and robust **FastAPI**.
- **Lightweight Database:** Data is stored persistently in a simple, file-based **SQLite** database.
- **Robust Validation:** The API intelligently validates input, handling invalid data and duplicate entries.
- **Clear Error Handling:** Provides user-friendly error messages with appropriate HTTP status codes (e.g., `404 Not Found`).
- **Automatic Interactive Docs:** Get started instantly with auto-generated API documentation via Swagger UI.

---

### 🛠️ Technology Stack

- **Python 3.8+**: The core programming language.
- **FastAPI**: The web framework used to build the API.
- **Uvicorn**: An ultra-fast ASGI server for running the application.
- **SQLite**: The serverless, self-contained SQL database engine.

---

### 🚀 Getting Started

Follow these simple steps to get the API up and running on your local machine.

#### Prerequisites

- Ensure you have **Python 3.8+** installed on your system.

#### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-folder>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    # On macOS and Linux
    python3 -m venv venv
    source venv/bin/activate

    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    The `requirements.txt` file contains all the necessary dependencies.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the API server:**
    ```bash
    uvicorn main:app --reload
    ```
    The `--reload` flag enables automatic server restarts on code changes. The API will now be live at `http://127.0.0.1:8000`.

---

### 📖 API Documentation

This API provides a complete set of endpoints to manage your books. For a rich, interactive experience, navigate to the auto-generated documentation pages:

-   **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
-   **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

#### Endpoint Details

| Endpoint                                       | Method | Description                                            | Notes                                                 |
| ---------------------------------------------- | :----: | ------------------------------------------------------ | ----------------------------------------------------- |
| `/books/`                                      |  `GET` | Retrieves a list of all books.                         | Returns `404` if no books are found.                  |
| `/find/?id={id}`                               |  `GET` | Finds a specific book by its unique ID.                | Returns `404` if the book ID is not found.            |
| `/addbook/?title={title}&author={author}&year={year}` |  `GET` | Adds a new book to the library.                        | **Note:** Conventionally, `POST` is used for creation. |
| `/updatebook/?id={id}&title={title}&author={author}&year={year}` | `GET` | Updates the details of an existing book.               | **Note:** Conventionally, `PUT` or `PATCH` is used for updates. |
| `/deletebook/?id={id}`                         |  `GET` | Deletes a book from the library by its ID.             | **Note:** Conventionally, `DELETE` is used for deletion. |

---


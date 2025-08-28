<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Library API</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #3B82F6;
            --secondary-color: #1F2937;
            --text-color: #333;
            --bg-color: #F9FAFB;
            --card-bg: #FFFFFF;
            --border-color: #E5E7EB;
        }

        body {
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 2rem;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            background: var(--card-bg);
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.05);
        }

        header {
            text-align: center;
            margin-bottom: 2rem;
        }

        h1 {
            color: var(--primary-color);
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
        }

        h1 .emoji {
            font-size: 2.5rem;
        }

        .subtitle {
            font-size: 1.1rem;
            color: var(--secondary-color);
            font-weight: 400;
        }

        .badges {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        
        .badge {
            padding: 0.3em 0.7em;
            border-radius: 4px;
            font-size: 0.85rem;
            font-weight: 700;
            color: white;
            background-color: #555;
        }
        
        .badge.rest { background-color: #0077b6; }
        .badge.python { background-color: #3776AB; }
        .badge.fastapi { background-color: #005571; }
        .badge.sqlite { background-color: #003B57; }

        section {
            margin-top: 2rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--border-color);
        }

        h2 {
            color: var(--secondary-color);
            border-bottom: 2px solid var(--primary-color);
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            font-size: 1.8rem;
        }

        p, ul {
            margin-bottom: 1rem;
        }

        ul {
            list-style-type: disc;
            padding-left: 1.5rem;
        }

        code {
            background-color: #F0F2F5;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 0.9rem;
        }

        pre {
            background-color: #1E293B;
            color: #E2E8F0;
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: monospace;
            font-size: 0.9rem;
        }

        .endpoint-card {
            background: #F8F9FB;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
        }

        .endpoint-card h3 {
            margin: 0 0 0.5rem 0;
            color: var(--primary-color);
            font-size: 1.4rem;
        }

        .endpoint-card .method {
            display: inline-block;
            padding: 0.2rem 0.6rem;
            margin-right: 0.5rem;
            border-radius: 4px;
            font-weight: bold;
            color: white;
        }

        .method.get { background-color: #10B981; }
        .method.post { background-color: #3B82F6; }
        .method.put { background-color: #F59E0B; }
        .method.delete { background-color: #EF4444; }

        .endpoint-path {
            font-family: monospace;
            background-color: var(--card-bg);
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            border: 1px solid var(--border-color);
            font-size: 0.9rem;
        }

        .response-code {
            font-weight: bold;
        }
        
        .success { color: #10B981; }
        .error { color: #EF4444; }

        .note {
            background-color: #FEF9C3;
            border-left: 4px solid #FCD34D;
            padding: 1rem;
            border-radius: 4px;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><span class="emoji">📚</span> Book Library API</h1>
            <p class="subtitle">A simple and efficient RESTful API for managing a collection of books.</p>
            <div class="badges">
                <span class="badge rest">RESTful</span>
                <span class="badge python">Python 3</span>
                <span class="badge fastapi">FastAPI</span>
                <span class="badge sqlite">SQLite</span>
            </div>
        </header>

        <section id="features">
            <h2>✨ Features</h2>
            <ul>
                <li><strong>CRUD Operations:</strong> Create, read, update, and delete books with ease.</li>
                <li><strong>FastAPI Framework:</strong> Built on the modern, high-performance FastAPI.</li>
                <li><strong>SQLite Database:</strong> Uses a lightweight, file-based SQLite database for persistence.</li>
                <li><strong>Input Validation:</strong> Includes checks for duplicate entries and invalid data (e.g., future publication years).</li>
                <li><strong>Error Handling:</strong> Provides clear and user-friendly error messages for common issues.</li>
                <li><strong>Automatic Interactive Docs:</strong> Automatically generates comprehensive API documentation with Swagger UI and ReDoc.</li>
            </ul>
        </section>

        <section id="getting-started">
            <h2>🚀 Getting Started</h2>
            <p>Follow these simple steps to get the API running on your local machine.</p>
            
            <h3>Prerequisites</h3>
            <p>Ensure you have <strong>Python 3.8+</strong> installed.</p>
            
            <h3>Installation & Setup</h3>
            <ol>
                <li><strong>Clone the repository:</strong>
                    <pre><code>git clone &lt;your-repository-url&gt;
cd &lt;repository-folder&gt;</code></pre>
                </li>
                <li><strong>Create a virtual environment (recommended):</strong>
                    <pre><code># On macOS and Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
.\venv\Scripts\activate</code></pre>
                </li>
                <li><strong>Install the required packages:</strong>
                    <p>All dependencies are listed in the <code>requirements.txt</code> file.</p>
                    <pre><code>pip install -r requirements.txt</code></pre>
                </li>
                <li><strong>Run the API server:</strong>
                    <pre><code>uvicorn main:app --reload</code></pre>
                    <p>The <code>--reload</code> flag enables auto-reloading during development. The API will be live at <code>http://127.0.0.1:8000</code>.</p>
                </li>
            </ol>
        </section>

        <section id="api-docs">
            <h2>📖 API Endpoints Documentation</h2>
            <p>This API provides a set of endpoints to manage your book collection. For a full interactive experience, visit the auto-generated documentation pages:</p>
            <ul>
                <li><strong>Swagger UI:</strong> <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a></li>
                <li><strong>ReDoc:</strong> <a href="http://127.0.0.1:8000/redoc">http://127.0.0.1:8000/redoc</a></li>
            </ul>
            
            <p>Here are the key endpoints:</p>

            <div class="endpoint-card">
                <h3>1. Get All Books</h3>
                <span class="method get">GET</span> <span class="endpoint-path">/books/</span>
                <p>Retrieves a list of all books in the library.</p>
                <h4>Responses:</h4>
                <p>
                    <span class="response-code success">200 OK</span>: Returns a JSON array of all books.
                </p>
                <p>
                    <span class="response-code error">404 Not Found</span>: If no books are in the database.
                </p>
            </div>

            <div class="endpoint-card">
                <h3>2. Find a Specific Book</h3>
                <span class="method get">GET</span> <span class="endpoint-path">/find/</span>
                <p>Finds a single book by its unique ID.</p>
                <h4>Query Parameters:</h4>
                <ul>
                    <li><code>id</code> (integer, required): The ID of the book.</li>
                </ul>
                <h4>Responses:</h4>
                <p>
                    <span class="response-code success">200 OK</span>: Returns the JSON object for the book.
                </p>
                <p>
                    <span class="response-code error">404 Not Found</span>: If the book ID does not exist.
                </p>
            </div>

            <div class="endpoint-card">
                <h3>3. Add a New Book</h3>
                <span class="method get">GET</span> <span class="endpoint-path">/addbook/</span>
                <div class="note">
                    <strong>Note:</strong> While this API uses a <code>GET</code> method, the conventional method for creating resources is <code>POST</code>.
                </div>
                <p>Adds a new book to the library.</p>
                <h4>Query Parameters:</h4>
                <ul>
                    <li><code>title</code> (string, required)</li>
                    <li><code>author</code> (string, required)</li>
                    <li><code>year</code> (integer, required)</li>
                </ul>
                <h4>Responses:</h4>
                <p>
                    <span class="response-code success">200 OK</span>: Success message.
                </p>
                <p>
                    <span class="response-code error">409 Conflict</span>: If a book with the same details already exists.
                </p>
                <p>
                    <span class="response-code error">422 Unprocessable Entity</span>: If the year is invalid (e.g., in the future).
                </p>
            </div>

            <div class="endpoint-card">
                <h3>4. Update a Book</h3>
                <span class="method get">GET</span> <span class="endpoint-path">/updatebook/</span>
                <div class="note">
                    <strong>Note:</strong> While this API uses a <code>GET</code> method, the conventional methods for updating resources are <code>PUT</code> or <code>PATCH</code>.
                </div>
                <p>Updates the details of an existing book by its ID.</p>
                <h4>Query Parameters:</h4>
                <ul>
                    <li><code>id</code> (integer, required)</li>
                    <li><code>title</code> (string, required)</li>
                    <li><code>author</code> (string, required)</li>
                    <li><code>year</code> (integer, required)</li>
                </ul>
                <h4>Responses:</h4>
                <p>
                    <span class="response-code success">200 OK</span>: Success message.
                </p>
                <p>
                    <span class="response-code error">404 Not Found</span>: If the book ID is not found.
                </p>
            </div>

            <div class="endpoint-card">
                <h3>5. Delete a Book</h3>
                <span class="method get">GET</span> <span class="endpoint-path">/deletebook/</span>
                <div class="note">
                    <strong>Note:</strong> While this API uses a <code>GET</code> method, the conventional method for deleting resources is <code>DELETE</code>.
                </div>
                <p>Deletes a book from the library by its ID.</p>
                <h4>Query Parameters:</h4>
                <ul>
                    <li><code>id</code> (integer, required): The ID of the book to delete.</li>
                </ul>
                <h4>Responses:</h4>
                <p>
                    <span class="response-code success">200 OK</span>: Success message.
                </p>
                <p>
                    <span class="response-code error">404 Not Found</span>: If the book ID is not found.
                </p>
            </div>
        </section>

        <section id="contributions">
            <h2>🤝 Contribution</h2>
            <p>Contributions are welcome! Feel free to open an issue or submit a pull request.</p>
        </section>
    </div>
</body>
</html>

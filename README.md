<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Library API</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-color: #0077B6;
            --secondary-color: #1a1a2e;
            --text-color: #333;
            --bg-color: #f4f7f9;
            --card-bg: #FFFFFF;
            --border-color: #e0e6ed;
            --code-bg: #f8f9fa;
        }

        body {
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 2rem;
            max-width: 900px;
            margin: 0 auto;
        }

        .container {
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
            font-size: 2.8rem;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.75rem;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #555;
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
            padding: 0.3em 0.8em;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
            color: white;
            background-color: #555;
            text-transform: uppercase;
        }

        .badge.rest { background-color: #0077B6; }
        .badge.python { background-color: #3776AB; }
        .badge.fastapi { background-color: #005571; }
        .badge.sqlite { background-color: #003B57; }

        section {
            margin-top: 2.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid var(--border-color);
        }

        h2 {
            color: var(--secondary-color);
            border-bottom: 3px solid var(--primary-color);
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
            font-size: 2rem;
        }

        h3 {
            color: var(--secondary-color);
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
        }

        p, ul {
            margin-bottom: 1rem;
        }

        ul {
            list-style-type: none;
            padding-left: 0;
        }
        
        ul li::before {
            content: '•';
            color: var(--primary-color);
            font-weight: bold;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }

        pre {
            background-color: #2D2D2D;
            color: #CCCCCC;
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            font-family: monospace;
            font-size: 0.9rem;
            line-height: 1.5;
            margin-top: 1rem;
        }

        code {
            background-color: var(--code-bg);
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 0.95rem;
            color: #c7254e;
        }

        .endpoint-card {
            background: #F8F9FA;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            transition: transform 0.2s;
        }

        .endpoint-card:hover {
            transform: translateY(-5px);
        }

        .endpoint-card h4 {
            margin: 0 0 0.5rem 0;
            font-size: 1.25rem;
            color: var(--primary-color);
        }

        .endpoint-card .method {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            margin-right: 0.5rem;
            border-radius: 6px;
            font-weight: bold;
            color: white;
            text-transform: uppercase;
            font-size: 0.8rem;
        }

        .method.get { background-color: #10B981; }
        .method.post { background-color: #3B82F6; }
        .method.put { background-color: #F59E0B; }
        .method.delete { background-color: #EF4444; }

        .endpoint-path {
            font-family: monospace;
            background-color: var(--card-bg);
            padding: 0.3rem 0.8rem;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            font-size: 0.9rem;
            color: #1F2937;
        }

        .response-code {
            font-weight: bold;
        }
        
        .success { color: #10B981; }
        .error { color: #EF4444; }

        .note {
            background-color: #FFFBEA;
            border-left: 5px solid #FCD34D;
            padding: 1rem;
            border-radius: 8px;
            margin-top: 1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1><span role="img" aria-label="books emoji">📚</span> Book Library API</h1>
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
                <li><strong>Complete CRUD Operations:</strong> Seamlessly create, read, update, and delete book records.</li>
                <li><strong>High-Performance Framework:</strong> Built using the modern, fast, and robust **FastAPI**.</li>
                <li><strong>Lightweight Database:</strong> Data is stored persistently in a simple, file-based **SQLite** database.</li>
                <li><strong>Robust Input Validation:</strong> The API intelligently validates data, handling cases like duplicate entries and invalid publication years.</li>
                <li><strong>Clear Error Handling:</strong> Provides user-friendly error messages with appropriate HTTP status codes for a better developer experience.</li>
                <li><strong>Automatic Interactive Docs:</strong> Get started instantly with auto-generated API documentation via Swagger UI and ReDoc.</li>
            </ul>
        </section>

        <section id="technology-stack">
            <h2>🛠️ Technology Stack</h2>
            <p>This project leverages the following technologies:</p>
            <ul>
                <li><strong>Python 3:</strong> The core programming language.</li>
                <li><strong>FastAPI:</strong> The web framework for building the API.</li>
                <li><strong>Uvicorn:</strong> An ultra-fast ASGI server for running the application.</li>
                <li><strong>SQLite:</strong> The serverless, self-contained SQL database engine.</li>
            </ul>
        </section>

        <section id="getting-started">
            <h2>🚀 Getting Started</h2>
            <p>Follow these simple steps to get the API up and running on your local machine.</p>
            
            <h3>Prerequisites</h3>
            <p>Ensure you have <strong>Python 3.8+</strong> installed on your system.</p>
            
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
                    <p>The <code>requirements.txt</code> file contains all the necessary dependencies.</p>
                    <pre><code>pip install -r requirements.txt</code></pre>
                </li>
                <li><strong>Run the API server:</strong>
                    <pre><code>uvicorn main:app --reload</code></pre>
                    <p>The <code>--reload</code> flag enables automatic server restarts on code changes. The API will now be live at <a href="http://127.0.0.1:8000" target="_blank">http://127.0.0.1:8000</a>.</p>
                </li>
            </ol>
        </section>

        <section id="api-endpoints">
            <h2>📖 API Endpoints Documentation</h2>
            <p>The API provides a complete set of endpoints to manage your books. For a rich, interactive experience, navigate to the auto-generated documentation pages:</p>
            <ul>
                <li><strong>Swagger UI:</strong> <a href="http://127.0.0.1:8000/docs" target="_blank">http://127.0.0.1:8000/docs</a></li>
                <li><strong>ReDoc:</strong> <a href="http://127.0.0.1:

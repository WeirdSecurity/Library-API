from fastapi import FastAPI
import sqlite3

def database():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        year INTEGER
    )
    """)
    conn.commit()
    conn.close()

database()


app = FastAPI()

def exist(conn,cursor,id):
    cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
    book = cursor.fetchone()
    if not book:
        conn.close()
        return {"Book not found"}
    
def not_exist(conn,cursor,id,title,author,year):
    cursor.execute(
        "SELECT * FROM books WHERE title = ? AND author = ? AND year = ?",
        (title, author, year)
    )
    existing_book = cursor.fetchone()
    if existing_book:
        conn.close()
        return  {"error": "Book already exists"}

@app.get("/books/")
def get_books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        return {"message": "No books found"}
    books = [{"id": r[0], "title": r[1], "author": r[2], "year": r[3]} for r in rows]
    return {"books": books}

@app.get("/addbook/")
def add_book(title: str, author: str, year: int):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    result = not_exist(conn, cursor, None, title, author, year)
    if result:
        return result
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", 
                   (title, author, year))
    conn.commit()
    conn.close()
    return {"message": f"Book '{title}' added successfully!"}

@app.get("/deletebook/")
def delete_book(id: int):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    exist(conn,cursor,id)
    cursor.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return {"message": f"Book with id {id} deleted successfully!"}

@app.get("/updatebook/")
def update_book(id: int, title: str, author: str, year: int):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    exist(conn,cursor,id)
    cursor.execute("""
        UPDATE books 
        SET title = ?, author = ?, year = ?
        WHERE id = ?
    """, (title, author, year, id))
    conn.commit()
    conn.close()
    return {"message": f"Book with id {id} updated successfully!"}
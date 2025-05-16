from fastapi import FastAPI
app = FastAPI()

#books object
BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]

# api-endpoint is just the url path to call the python function
@app.get("/books") # decorator to specify api endpoint thta will call this function URL:127.0.0.1:8000
async def read_all_books(): #async is not needed with FastAPI bc if it is async fastapi will add the functionality behind the scene
    return BOOKS

#path parameters##################
@app.get("/books/mybook")
async def read_all_books():
    return {'book_title': 'My favorite book!'}

#grab a single book title
@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book 

####### query paramaters
# filter data based on url provdied 
@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

#### query with path paramater
@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
             books_to_return.append(book)

    return books_to_return

####### POST REQUEST ##################
# post requests send data in the body
from fastapi import Body
# adds new book to BOOKS
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

##### #### PUT Methods #########
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


######## DELETE REQUEST #########
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break



### Assignment 1 
"""
create new api endpoint that can fetch all books from a specific author
using either Path Parameters or Query Parameters 
"""
@app.get("/books/byauthor/{book_author}")
async def read_author_by_query_param(book_author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold():
            books_to_return.append(book)

    return books_to_return

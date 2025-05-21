from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

# use real book object
class Book:
    id: int
    title: str
    author: str
    description: str 
    rating : int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

# creat a pydantic BookRequest object that can be validated then 
# later converted into a Book object if it meets the criteria
class BookRequest(BaseModel):
    id: int
    title: str
    author: str  
    description : str
    rating : int 

BOOKS = [
    Book(1, 'Computer Science Pro','codingwithjessie','A very nice book', 5),
    Book(2, 'Be Fast with FastAPI','codingwithjessie','A great book', 5),
    Book(3, 'Master Endpoints','codingwithjessie','An awesome book', 5),
    Book(4, 'HP1','author1','An ok book', 3),
    Book(5, 'HP2','author2','It was a good book ', 4)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

# create book with request w/ data validation
@app.post("/create-book")
async def create_book(book_request: BookRequest): #subsitute Body() for book_request of type BookRequest (pydantic objcet)
    new_book = Book(**book_request.model_dump()) # converting the request to Book object
    BOOKS.append(new_book)


    
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()


class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(title="Description of the book",
                                       max_length=100,
                                       min_length=1)
    rating: int = Field(gt=-1, lt=101)


BOOKS = []


@app.get("/")
async def read_all_books():
    if len(BOOKS) < 1:
        create_books_no_api()
    return BOOKS


@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book


def create_books_no_api():
    book_1 = Book(id="aa5d05cc-f79f-4164-bf7a-8499c3cf4c62",
                  title="Title 1",
                  author="Author 1",
                  description="Description 1",
                  rating=60)
    book_2 = Book(id="8eed41f7-d916-40b5-850b-e5dedd33ce25",
                  title="Title 2",
                  author="Author 2",
                  description="Description 2",
                  rating=70)
    book_3 = Book(id="1915ebb4-25b5-4559-925a-801d0af197aa",
                  title="Title 3",
                  author="Author 3",
                  description="Description 3",
                  rating=80)
    book_4 = Book(id="0e0b682d-032f-4e7b-a6d2-c92a6842a001",
                  title="Title 4",
                  author="Author 4",
                  description="Description 4",
                  rating=90)

    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)
    BOOKS.append(book_4)

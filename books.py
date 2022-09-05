from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}


class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"


# async def read_all_books(skip_book: str = "book_3"):
# async def read_all_books(skip_book: str):
@app.get('/')
async def read_all_books(skip_book: Optional[str] = None):
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS


@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return {"Direction": direction_name, "sub": "Up"}
    if direction_name == DirectionName.south:
        return {"Direction": direction_name, "sub": "Down"}
    if direction_name == DirectionName.west:
        return {"Direction": direction_name, "sub": "Left"}
    if direction_name == DirectionName.east:
        return {"Direction": direction_name, "sub": "Right"}


@app.get("/books/mybook")
async def read_favorite_book():
    return {"book_title": "My favorite book"}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    """
        book_id: int => FastAPI 에서 자동으로 string->integer 로 변환 but, int 형태가 아닌
        다른 'foo' 같은 변수가 들어가면 에러 발생
    :param book_id: integer type variable of book_id
    :return:
    """
    return {"book_title": book_id}

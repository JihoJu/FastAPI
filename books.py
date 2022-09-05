from fastapi import FastAPI

app = FastAPI()

BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}


@app.get('/')
async def read_all_books():
    return BOOKS


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

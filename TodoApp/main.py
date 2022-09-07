from fastapi import FastAPI, Depends
from database import engine, SessionLocal
import models as models
from sqlalchemy.orm import Session

app = FastAPI()

# 스키마 생성: 메타데이터를 보관하고 있는 Base를 이용해 스키마를 간단하게 생성
models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


"""
- Session: Manages persistence operations for ORM-mapped objects.
- Dependency Injection이란 코드의 재활용을 위해 제공해주는 fastapi의 기능
    만약 두 개의 path operation이 있다면 모두 같은 기능을 한다
    -> 그럼 2 개를 모두 쓰는 것보단 하나의 기능으로 정의 후 재활용을 하면 효율적일 것이다.
    -> Depends 사용!! 
"""
@app.get("/")
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()

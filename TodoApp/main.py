from fastapi import FastAPI
from database import engine
import models as models

app = FastAPI()

# 스키마 생성: 메타데이터를 보관하고 있는 Base를 이용해 스키마를 간단하게 생성
models.Base.metadata.create_all(bind=engine)


@app.get("/")
async def create_database():
    return {"Database": "Created"}

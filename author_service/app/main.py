from fastapi import FastAPI, HTTPException
from app.author import Author


authors: list[Author] = [
    Author(0, 'Людовико Эйнауди', 'Минимализм'),
    Author(1, 'Роберто Каччапалья', 'Современная классика'),
    Author(2, 'Джо Хисаиси', 'Классика')
]

app = FastAPI()


@app.get("/v1/auth")
async def get_auth():
    return authors

@app.get("/v1/auth/{id}")
async def get_auth_by_id(id: int):
    result = [item for item in authors if item.id == id]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code = 404, detail="Документ не найден")
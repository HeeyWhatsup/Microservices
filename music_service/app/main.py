from fastapi import FastAPI, HTTPException
from app.music import Music


musics: list[Music] = [
    Music(0, 'Experience', '16th april, 2020'),
    Music(1, 'Fly(Moscow)', '8th april, 2012'),
    Music(2, 'Una Mattina', '6th april, 2012'),
    Music(3, 'My time', '21 January, 2012')
]

app = FastAPI()


@app.get("/v1/musics")
async def get_musics():
    return musics

@app.get("/v1/musics/{id}")
async def get_musics_by_id(id: int):
    result = [item for item in musics if item.id == id]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code = 404, detail="Документ не найден")
from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    sheep = db.get_sheep(id)
    if sheep is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep
@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep already exists")
    db.data[sheep.id] = sheep
    return sheep
@app.get("/sheep/", response_model=list[Sheep])
def read_all_sheep():
    return db.get_all_sheep()
@app.put("/sheep/{sheep_id}", response_model=Sheep)
def update_sheep(sheep_id: int, sheep: Sheep):
    if sheep.id != sheep_id:
        raise HTTPException(status_code=400, detail="ID in URL doesn’t match ID in body.")
    if sheep_id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return db.update_sheep(sheep)
@app.delete("/sheep/{sheep_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(sheep_id: int):
    if sheep_id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return db.delete_sheep(sheep_id)

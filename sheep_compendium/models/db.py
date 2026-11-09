from models.models import Sheep
from typing import Dict


class FakeDB:
    def __init__(self):
        self.data : Dict[int, Sheep] = {}

    def get_sheep(self, id: int) -> Sheep:
        return self.data.get(id)

    def add_sheep(self, sheep: Sheep) -> Sheep:
        if sheep.id in self.data:
            raise ValueError(f"Sheep with id {sheep.id} already exists")
        self.data[sheep.id] = sheep
        return sheep

    def get_all_sheep(self) -> list[Sheep]:
        return [sheep for sheep in self.data.values()]

    def update_sheep(self, sheep: Sheep) -> Sheep:
        if sheep.id not in self.data:
            raise ValueError(f"Sheep with id {sheep.id} does not exist")
        self.data[sheep.id] = sheep
        return sheep

    def delete_sheep(self, sheep_id: int) -> None:
        if sheep_id not in self.data:
            raise ValueError(f"Sheep with id {sheep_id} does not exist")
        del self.data[sheep_id]


db = FakeDB()
db.data = {
    1: Sheep(id = 1, name ="Spice" , breed="Gotland" , sex="ewe"),
    2: Sheep(id = 2, name ="Blondie" , breed="Polypay" , sex="ram"),
    3: Sheep(id = 3, name ="Deedee" , breed="Jacobs Four Horns" , sex="ram"),
    4: Sheep(id = 4, name ="Rommy" , breed="Romney" , sex="ewe"),
    5: Sheep(id = 5, name ="Vala" , breed="Valais Blacknose" , sex="ewe"),
    6: Sheep(id = 6, name ="Esther" , breed="Border Leicester" , sex="ewe")
}


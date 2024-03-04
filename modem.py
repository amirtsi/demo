from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Modem(BaseModel):
    id: int
    name: str
    brand: str
    model: str
    price: float
    available: bool

fake_modems = [
    Modem(id=1, name="Modem A", brand="Brand X", model="Model 123", price=99.99, available=True),
    Modem(id=2, name="Modem B", brand="Brand Y", model="Model 456", price=149.99, available=False),
    Modem(id=3, name="Modem C", brand="Brand Z", model="Model 789", price=199.99, available=True),
]

@app.get("/modems")
async def get_modems(brand: Optional[str] = None, available: Optional[bool] = None):
    filtered_modems = fake_modems
    if brand:
        filtered_modems = [modem for modem in filtered_modems if modem.brand == brand]
    if available is not None:
        filtered_modems = [modem for modem in filtered_modems if modem.available == available]
    return filtered_modems

@app.get("/modems/{modem_id}")
async def get_modem(modem_id: int):
    for modem in fake_modems:
        if modem.id == modem_id:
            return modem
    return {"error": "Modem not found"}

@app.post("/modems")
async def create_modem(modem: Modem):
    fake_modems.append(modem)
    return modem

@app.put("/modems/{modem_id}")
async def update_modem(modem_id: int, new_modem: Modem):
    for i, modem in enumerate(fake_modems):
        if modem.id == modem_id:
            fake_modems[i] = new_modem
            return new_modem
    return {"error": "Modem not found"}

@app.delete("/modems/{modem_id}")
async def delete_modem(modem_id: int

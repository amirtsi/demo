from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}


@router.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@router.post("/items/")
async def create_item(item: dict):
    return item


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "updated_item": item}


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id, "message": "Item deleted successfully"}


@router.get("/items/")
async def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "items": []}


@router.get("/items/{item_id}/details")
async def get_item_details(item_id: int):
    if item_id == 42:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "details": "Item details"}


@router.get("/users/{user_id}/items/")
async def get_user_items(user_id: int, category: str):
    return {"user_id": user_id, "category": category, "items": []}

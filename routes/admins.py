from fastapi import APIRouter, Request, HTTPException
from services.db import admins_collection
router = APIRouter()

@router.get("/admins/")
def get_admins():
    admins = list(admins_collection.find())
    for admin in admins:
        admin["_id"] = str(admin["_id"])
    return admins

@router.post("/adminLogin")
async def login_admin(request: Request):
    data = await request.json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        raise HTTPException(status_code=400, detail="Username and password are required")

    admin = admins_collection.find_one({
        "username": username,
        "password": password
    })

    if not admin:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    admin["_id"] = str(admin["_id"])
    return admin
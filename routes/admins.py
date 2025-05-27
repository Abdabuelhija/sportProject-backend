from fastapi import APIRouter
from services.db import admins_collection
router = APIRouter()
@router.get("/admins/")
def get_admins():
    admins = list(admins_collection.find())
    for admin in admins:
        admin["_id"] = str(admin["_id"])
    return admins

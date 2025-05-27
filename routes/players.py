from fastapi import APIRouter
from bson import ObjectId
from services.db import players_collection
from models.player_model import Player

router = APIRouter()

@router.post("/players/")
def add_player(player: Player):
    player_dict = player.dict()
    player_dict["city_id"] = ObjectId(player.city_id)
    player_dict["sports"] = [ObjectId(s) for s in player.sports]
    result = players_collection.insert_one(player_dict)
    return {"message": "Player added", "id": str(result.inserted_id)}

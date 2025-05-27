from pymongo import MongoClient
from starlette.config import Config
from services import config

MONGO_URI = config.MONGO_URL
client = MongoClient(MONGO_URI)
db = client[config.MONGO_DBNAME]

countries_collection = db["countries"]
cities_collection = db["cities"]
sports_collection = db["sports"]
players_collection = db["players"]
groups_collection = db["groups"]
courts_collection = db["courts"]
schedules_collection = db["schedules"]
admins_collection = db["admins"]




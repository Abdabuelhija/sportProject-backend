from pymongo import MongoClient
import certifi
from services import config

client = MongoClient(config.MONGO_URL, tlsCAFile=certifi.where())
db = client[config.MONGO_DBNAME]
print("this is a test",config.MONGO_URL)
countries_collection = db["countries"]
cities_collection = db["cities"]
sports_collection = db["sports"]
players_collection = db["players"]
groups_collection = db["groups"]
courts_collection = db["courts"]
schedules_collection = db["schedules"]
admins_collection = db["admins"]




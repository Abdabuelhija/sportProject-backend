from pymongo import MongoClient

MONGO_URI = "mongodb+srv://aabdab28:Abd281202@cluster0.tvvhmmw.mongodb.net/sportDB"
client = MongoClient(MONGO_URI)
db = client["sportDB"]

countries_collection = db["countries"]
cities_collection = db["cities"]
sports_collection = db["sports"]
players_collection = db["players"]
groups_collection = db["groups"]
courts_collection = db["courts"]
schedules_collection = db["schedules"]
admins_collection = db["admins"]




from fastapi import FastAPI
from routes import players, admins

app = FastAPI()

# Include routers
app.include_router(players.router)
app.include_router(admins.router)
from fastapi import FastAPI
from routes import players, admins

app = FastAPI()

@app.get("/")
def read_root():
    return {"welcome to sport project backend"}

# Include routers
app.include_router(players.router)
app.include_router(admins.router)
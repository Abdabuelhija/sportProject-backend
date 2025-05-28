from fastapi import FastAPI
from routes import players, admins
import ssl, sys

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "welcome to sport project backend"}

@app.get("/versions")
def versions():
    return {
        "python_version": sys.version,
        "openssl_version": ssl.OPENSSL_VERSION,
    }

# Include routers
app.include_router(players.router)
app.include_router(admins.router)

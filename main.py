from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import players, admins

app = FastAPI()

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "welcome to sport project backend"}

# Include routers
app.include_router(players.router)
app.include_router(admins.router, prefix="/admins")


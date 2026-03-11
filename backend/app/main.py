from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import cities, attractions

app = FastAPI(title="RoTravel API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cities.router)
app.include_router(attractions.router)

@app.get("/")
async def root():
    return {"status": "RoTravel API is running"}
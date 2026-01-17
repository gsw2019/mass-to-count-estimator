from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import get_items_collection

app = FastAPI()

origins = [
    "http://localhost:5173",    # where we can get requests from (where frontend runs)
    "localhost:5173"

]

# so can specify where requests can come from
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to FastAPI."}

@app.get("/items", tags=["inventory"])
async def get_items() -> dict:
    return {
        "items": await get_items_collection("marcos")
    }
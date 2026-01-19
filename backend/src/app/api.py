from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import get_items_collection, add_item

app = FastAPI()

# where we can get requests from (where frontend runs)
origins = [
    "http://localhost:5173",
    "localhost:5173",
    "https://mass-to-count-estimator.vercel.app",
    "mass-to-count-estimator.vercel.app"
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
async def read_root_route() -> dict:
    return {"message": "Welcome to FastAPI."}

#
# TODO: allow user to choose establishment and pass it through to here
#

@app.get("/items", tags=["inventory"])
async def get_items_route() -> dict:
    return {
        "items": await get_items_collection("marcos")
    }

@app.post("/add-item", tags=["inventory"])
async def add_item_route(item: dict) -> dict:
    return {
        "new item": await add_item(item, "marcos")
    }
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import get_items, add_item, get_estabs

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
    """ home route

    :return: FastAPI message
    """
    return {"message": "Welcome to FastAPI."}


@app.get("/estabs", tags=["establishments"])
async def get_estabs_route() -> dict:
    """ steps into db to get establishments supported

    :return: list of establishment documents
    """
    return {
        "estabs": await get_estabs()
    }

@app.get("/items", tags=["inventory"])
async def get_items_route(estab: str) -> dict:
    """ steps into db to get all an establishments items

    :param estab: name of database for establishment
    :return:
    """
    return {
        "items": await get_items(estab)
    }

@app.post("/add-item", tags=["inventory"])
async def add_item_route(item: dict, estab: str) -> dict:
    """ steps into db to add a new item to an establishments items

    :param item: item with appropriate fields to be added
    :param estab: establishment item will be added to
    :return:
    """
    return {
        "new item": await add_item(item, estab)
    }
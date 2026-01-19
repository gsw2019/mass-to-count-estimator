from pymongo import AsyncMongoClient
import os
from dotenv import load_dotenv

# get env variables from .env file
load_dotenv()

uri = os.getenv("MONGO_URI")
client = AsyncMongoClient(uri)      # create a MongoDB client and connect to server

async def get_items_collection(est_name: str):
    try:
        database = client.get_database(est_name)
        items_collection = database.get_collection(f"{est_name}_items")

        # retrieve all the entries
        items = await items_collection.find().to_list()

        # convert the MongoDB _id to string
        for item in items:
            item["id"] = str(item["_id"])
            del item["_id"]

        print(items)
        return items

    except Exception as e:
        raise Exception(f"Error fetching items for {est_name}", e)


async def add_item(item: dict, est_name: str):
    try:
        database = client.get_database(est_name)
        items_collection = database.get_collection(f"{est_name}_items")

        # should already be of expected key:value pairs for DB
        new_item = await items_collection.insert_one(item)

        return {
                "id": str(new_item.inserted_id),
                "acknowledged": new_item.acknowledged
        }

    except Exception as e:
        raise Exception(f"Error fetching items for {est_name}", e)

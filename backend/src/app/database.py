from pymongo import AsyncMongoClient
import os
from dotenv import load_dotenv

# get env variables from .env file (for development)
load_dotenv()


async def get_items_collection(store_name):
    # should work for local env and deployed env
    uri = os.getenv("MONGO_URI")
    # create a MongoDB client and connect to server
    client = AsyncMongoClient(uri)

    try:
        database = client.get_database(store_name)
        items_collection = database.get_collection("marcos_items")

        # retrieve all the entries
        items = await items_collection.find().to_list()

        # convert the MongoDB _id to string
        for item in items:
            item["id"] = str(item["_id"])
            del item["_id"]

        print(items)
        return items

    except Exception as e:
        raise Exception(f"Error fetching items for {store_name}", e)

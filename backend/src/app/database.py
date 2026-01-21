from pymongo import AsyncMongoClient
import os
from dotenv import load_dotenv

# get env variables from .env file
load_dotenv()

uri = os.getenv("MONGO_URI")
client = AsyncMongoClient(uri)      # create a MongoDB client and connect to server

async def get_estabs() -> list:
    """ gets all the current establishments data has been recorded for

    :return: list of names
    """
    try:
        database = client.get_database("establishments")
        estabs = database.get_collection("establishment_names")

        estabs = await estabs.find().to_list()

        # convert the MongoDB _id to string
        for estab in estabs:
            estab["id"] = str(estab["_id"])
            del estab["_id"]

        print(estabs)
        return estabs

    except Exception as e:
        raise Exception(f"Error fetching establishments: {e}")


async def get_items(estab_name: str) -> list:
    """ fetches the items stored under the database named estab_name

    :param estab_name: name of a database
    :return: all items in estab_name
    """
    try:
        database = client.get_database(estab_name)
        items = database.get_collection("items")

        # retrieve all the entries
        items = await items.find().to_list()

        # convert the MongoDB _id to string
        for item in items:
            item["id"] = str(item["_id"])
            del item["_id"]

        print(items)
        return items

    except Exception as e:
        raise Exception(f"Error fetching items for {estab_name}: {e}")


async def add_item(item: dict, estab_name: str) -> dict:
    """ adds an item to the collection of items in estab_name

    :param item: data of item to be added
    :param estab_name: which database the item is to be added to
    :return: object with descriptors of the operations result
    """
    try:
        database = client.get_database(estab_name)
        items_collection = database.get_collection("items")

        # should already be of expected key names for db document
        new_item = await items_collection.insert_one(item)

        return {
                "id": str(new_item.inserted_id),
                "acknowledged": new_item.acknowledged
        }

    except Exception as e:
        raise Exception(f"Error fetching items for {estab_name}", e)

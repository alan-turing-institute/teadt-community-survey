import streamlit as st
import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
import os
from config import (
    DATABASE_NAME_ENV,
    COLLECTION_NAME_ENV,
    CONNECTION_STRING_ENV,
)
from typing import Optional
from datetime import datetime


@st.cache_resource
def init_connection() -> MongoClient:
    client: MongoClient = MongoClient(os.getenv(CONNECTION_STRING_ENV))

    try:
        client.server_info()
    except pymongo.errors.ServerSelectionTimeoutError:
        raise TimeoutError(
            "Invalid API for MongoDB connection string or timed out when"
            " attempting "
            "to connect"
        )

    return client


def add_survey_results(client: MongoClient, data: dict[str, str]) -> None:

    collection: Collection = get_survey_collection(client)
    data["modification_date"] = str(datetime.today().replace(microsecond=0))

    collection.update_one(
        {
            "_id": data["_id"],
        },
        {"$set": data},
        upsert=True,
    )


def get_survey_collection(client: MongoClient) -> Collection:
    database_value: Optional[str] = os.getenv(DATABASE_NAME_ENV)
    collection_value: Optional[str] = os.getenv(COLLECTION_NAME_ENV)

    if database_value is None or collection_value is None:
        raise ValueError(
            f"We need values for database ({database_value}) "
            f"and collection ({collection_value})"
        )

    database = client[database_value]
    collection: Collection = database[collection_value]
    return collection


def get_field_values(client: MongoClient, field_name: str) -> dict[str, list]:

    collection: Collection = get_survey_collection(client)

    query_results: Cursor = collection.find(filter={}, projection=[field_name])

    return {
        field_name: [document[field_name] for document in list(query_results)]
    }

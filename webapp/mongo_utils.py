import streamlit as st
import pymongo
from pymongo import MongoClient
import os
from config import DATABASE_NAME_ENV, COLLECTION_NAME_ENV, CONNECTION_STRING_ENV
from typing import Optional


@st.cache_resource
def init_connection() -> MongoClient:
    client: MongoClient = MongoClient(os.getenv(CONNECTION_STRING_ENV))

    try:
        client.server_info()
    except pymongo.errors.ServerSelectionTimeoutError:
        raise TimeoutError(
            "Invalid API for MongoDB connection string or timed out when attempting "
            "to connect"
        )

    return client


def add_survey_results(client: MongoClient, data: dict[str, str]) -> None:
    database_value: Optional[str] = os.getenv(DATABASE_NAME_ENV)
    collection_value: Optional[str] = os.getenv(COLLECTION_NAME_ENV)

    if database_value is None or collection_value is None:
        raise ValueError(
            f"We need values for database ({database_value}) "
            f"and collection ({collection_value})"
        )

    database = client[database_value]
    collection = database[collection_value]

    collection.update_one({"_id": data["_id"]}, {"$set": data}, upsert=True)

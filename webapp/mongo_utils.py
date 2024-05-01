import streamlit as st
import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.results import UpdateResult
import os
from config import (
    DATABASE_NAME_ENV,
    COLLECTION_NAME_ENV,
    CONNECTION_STRING_ENV,
    EMAIL_STATE_KEY,
    ALL_CONSENT_STATE_KEYS,
    CONSENT_QUESTIONS,
)
from typing import Optional
from datetime import datetime
import logging
from email_validator import validate_email, ValidatedEmail
from typing import Any


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


def validate_survey_results(data: dict[str, Any]):
    # Validate.
    provided_mail: str = (
        data[EMAIL_STATE_KEY] if EMAIL_STATE_KEY in data else None
    )

    if provided_mail:
        validated_email: ValidatedEmail = validate_email(provided_mail)
        # Update with the normalized form.
        data[EMAIL_STATE_KEY] = validated_email.email

    consent_responses: list[bool] = [
        data[state_key]
        for state_key in ALL_CONSENT_STATE_KEYS
        if state_key in data
    ]

    if len(consent_responses) != CONSENT_QUESTIONS or not all(
        consent_responses
    ):
        raise ValueError(
            "You did not provide consent for your data to be stored."
            " Please go back to the Consent page."
        )


def add_survey_results(client: MongoClient, data: dict[str, str]) -> None:

    validate_survey_results(data)

    collection: Collection = get_survey_collection(client)
    data["modification_date"] = str(datetime.today().replace(microsecond=0))

    logging.info(f"Storing responses with {data['_id']=}")

    result: UpdateResult = collection.update_one(
        {
            "_id": data["_id"],
        },
        {"$set": data},
        upsert=True,
    )
    logging.info(f"Updated documents: {result.modified_count=}")


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
        field_name: [
            document[field_name]
            for document in list(query_results)
            if field_name in document
        ]
    }

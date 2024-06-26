import streamlit as st
import pymongo
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.results import UpdateResult
from itertools import combinations
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


def check_response_count(client, threshold=10):
    """
    Checks the total number of responses and displays a warning
    if the number of responses is below the specified threshold.

    Args:
        client (MongoClient): The MongoDB client.
        threshold (int): The response count threshold for displaying a warning.

    Returns:
        int: The total number of responses.
    """
    total_response_data = count_responses(client, {})
    total_response_count = total_response_data["total"]

    if total_response_count < threshold:
        st.warning(
            f"""
            🎉 Amazing, you are one of our first {threshold} respondents!
            Please note that the data is based on limited responses
            and may not fully represent broader trends yet.
            """
        )

    return total_response_count


def count_responses(client, query):
    """
    Count the number of documents in a MongoDB collection
    that match each individual query item
    and every combination of query items.

    Args:
        client (MongoClient): The MongoDB client.
        database_name (str): The name of the database.
        collection_name (str): The name of the collection.
        query (dict): A dictionary representing the MongoDB query.

    Returns:
        dict: A dictionary with keys as the query item combinations
        and values as their respective counts.
    """

    db = client[os.getenv(DATABASE_NAME_ENV)]
    collection = db[os.getenv(COLLECTION_NAME_ENV)]

    results = {}
    # Handle the empty query case
    if not query:
        results["total"] = collection.count_documents({})
        return results

    # Generate all possible combinations of query keys
    keys = list(query.keys())
    for r in range(1, len(keys) + 1):
        for combo in combinations(keys, r):
            # Build the subquery for current combination
            subquery = {key: query[key] for key in combo}
            # Count documents that match the subquery
            count = collection.count_documents(subquery)
            # Store the count with a descriptive key
            results[", ".join(combo)] = count

    return results


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


def get_field_values(
    client: MongoClient, field_name: str, myfilter: dict[str, str] = {}
) -> dict[str, list]:

    collection: Collection = get_survey_collection(client)

    query_results: Cursor = collection.find(
        filter=myfilter, projection=[field_name]
    )

    return {
        field_name: [
            document[field_name]
            for document in list(query_results)
            if field_name in document
        ]
    }

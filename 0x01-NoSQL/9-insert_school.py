#!/usr/bin/env python3
"""
This project module contains a function that inserts
a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Function that inserts a new document in a
    collection based on kwargs.
    Returns:
        The new _id
    """
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id

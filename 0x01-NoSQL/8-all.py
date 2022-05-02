#!/usr/bin/env python3
"""
This project module contains a function that lists all
documents in a collection.
"""

def list_all(mongo_collection):
    """
    Function that lists all documents in a collection.
    Returns:
        A list of all documents in a collection.
        An empty list if no document in the collection
    """
    if mongo_collection is None:
        return []

    return list(mongo_collection.find({}))

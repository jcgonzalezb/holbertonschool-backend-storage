#!/usr/bin/env python3
"""
This project module contains a function that changes
all topics of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics of a school
    document based on the name.
    name (string) will be the school name to update.
    topics (list of strings) will be the list of
    topics approached in the school
    Returns:
        updated topics
    """
    myquery = {"name": name}
    newvalues = {"$set": {"topics": topics}}

    mongo_collection.update_one(myquery, newvalues)

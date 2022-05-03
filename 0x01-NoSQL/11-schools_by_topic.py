#!/usr/bin/env python3
"""
This project module contains a function that returns
the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns the list of school
    having a specific topic.
    Returns:
        List of school
    """
    return list(mongo_collection.find({"topics": topic}))

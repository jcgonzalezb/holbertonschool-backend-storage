#!/usr/bin/env python3
"""
This project module contains a Python script that provides
some stats about Nginx logs stored in MongoDB.
"""

import pymongo
from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
my_database = myclient["logs"]
my_collection = my_database["nginx"]
total_count = my_collection.count_documents({})
print(total_count, "Logs")
print("Methods:")


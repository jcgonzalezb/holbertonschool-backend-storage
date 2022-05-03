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
total_count_get = my_collection.count_documents({"method": "GET"})
print("    method GET: ", total_count_get)
total_count_post = my_collection.count_documents({"method": "POST"})
print("    method POST: ", total_count_post)
total_count_put = my_collection.count_documents({"method": "PUT"})
print("    method PUT: ", total_count_put)
total_count_patch = my_collection.count_documents({"method": "PATCH"})
print("    method PATCH: ", total_count_patch)
total_count_delete = my_collection.count_documents({"method": "DELETE"})
print("    method DELETE: ", total_count_delete)
total_count_status = my_collection.count_documents(
    {"method": "GET", "path": "/status"})
print(total_count_status, "status check")

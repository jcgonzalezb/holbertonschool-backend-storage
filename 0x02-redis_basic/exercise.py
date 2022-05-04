#!/usr/bin/env python3
"""
Redis caching module
"""
import redis
import uuid


class Cache:
    """
    Redis chache class
    """

    def __init__(self):
        """
        Cache class initialization
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """
        Store method that generates a random key
        (e.g. using uuid), store the input data
        in Redis using the random key.
        Returns:
                Returns the random key.
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

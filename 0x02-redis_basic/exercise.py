#!/usr/bin/env python3
"""
Redis caching module
"""
import redis
from typing import Union, Callable, Optional
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

    def store(self, data: Union[str, bytes, int, float]) -> str:
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

    def get(
            self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Returns the key's value.
        fn is an optional argument that will be used to
        convert the data back to the desired format.
        """
        result = self._redis.get(key)
        if fn:
            return fn(result)
        return result

    def get_str(self, key):
        """
        Returns key value as string.
        """
        return get(key, str)

    def get_int(self, key):
        """
        Returns key value as integer.
        """
        return get(key, int)

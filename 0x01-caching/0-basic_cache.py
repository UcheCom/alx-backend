#!/usr/bin/python3
"""0. Basic dictionary"""

BasicCaching = __import__('basic_caching').BasicCaching


class BasicCache(BaseCaching):
    """A caching system that inherits from the parent class
       - BaseCaching
    """

    def put(self, key, item):
        """Puts or adds a new item to the cache system"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value linked to key in the cache"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

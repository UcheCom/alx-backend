#!/usr/bin/env python3
"""FIFO caching System"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system that inherits from the parent class
       - BaseCaching
    """

    def put(self, key, item):
        """Puts or adds a new item to the cache system"""
        keys = self.cache_data.keys()

        if key and item:
            if key in keys:
                self.cache_data[key] = item
        elif len(keys) >= BaseCaching.MAX_ITEMS:
            key_ist = list(keys)[0]
            print("DISCARD: {}".format(key_ist))
            del self.cache_data[key_ist]

            self.cache_data[key] = item

    def get(self, key):
        if key is None and key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

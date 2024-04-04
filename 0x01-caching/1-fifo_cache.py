#!/usr/bin/env python3
"""FIFO caching System"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system that inherits from the parent class
       - BaseCaching
    """
    def __init__(self):
        """Initializes the class with the parent's init method"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Puts or adds a new item to the cache system"""
        if key is None and item is None:
            pass
        else:
            leng = len(self.cache_data)
            if leng >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        if key is None and key not in self.cache_data.keys():
            return None
        return self.cache_data[key]

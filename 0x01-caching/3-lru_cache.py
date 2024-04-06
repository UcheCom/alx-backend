#!/usr/bin/env python3
"""FIFO Caching System"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU Caching that inherits from the parent class"""

    def __init__(self):
        """Initializes the parent class
        """
        super().__init__()
        self.__itemsUsed = []

    def put(self, key, item):
        """ This adds a new item to the cache"""

        if key and item:
            if key not in self.__itemsUsed:
                self.__itemsUsed.append(key)
            else:
                u_key = self.__itemsUsed.pop(self.__itemsUsed.index(key))
                self.__itemsUsed.append(u_key)

            self.cache_data[key] = item
            if len(self.__itemsUsed) > BaseCaching.MAX_ITEMS:
                key_lru = self.__itemsUsed.pop(0)
                del self.cache_data[key_lru]
                print("DISCARD: {}".format(key_lru))

    def get(self, key):
        """ Get an item from the cache by key"""
        if not key or key not in self.cache_data.keys():
            return None
        key_lru = self.__itemsUsed.pop(self.__itemsUsed.index(key))
        self.__itemsUsed.append(key_lru)
        return self.cache_data[key]

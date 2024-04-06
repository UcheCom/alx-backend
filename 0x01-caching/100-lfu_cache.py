#!/usr/bin/env python3
"""LFU Caching System"""

from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching that inherits from the parent class"""
    def __init__(self):
        """Initializes the parent class
        """
        super().__init__()
        self.__timestamps = {}
        self.__frequency = {}

    def put(self, key, item):
        """ This adds a new item to the cache"""

        if key and item:
            self.__timestamps[key] = datetime.now()

            if key not in self.__frequency:
                self.__frequency[key] = 1
            else:
                self.__frequency[key] += 1

            self.cache_data[key] item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                fq_v = [v for k, v in self.__frequency.items() if k != key]
                min_freq = min(fq_v)
                min_ks = [key for key, freq in self.__frequency.items()
                          if freq == min_freq]
                min_k = min(
                    min_ks,
                    key=lambda key: self.__timestamps[key],
                )
                del self.cache_data[min_k]
                del self.__frequency[min_k]
                del self.__timestamps[min_k]
                print("DISCARD: {}".format(min_k))

    def get(self, key):
        """ This gets an item from the cache by key"""
        if not key or key not in self.cache_data.keys():
            return None

        self.__frequency[key] += 1
        self.__timestamps[key] = datetime.now()

        return self.cache_data[key]

#!/usr/bin/env python3
"""Module shows simple pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """function returns a tuple of size
    two containing a start index and an end index
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """This returns the appropriate page of the
           dataset (i.e. the correct list of rows).
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        data_set = self.dataset()
        x = len(data_set)
        if start_idx >= x or end_idx > x:
            return []
        return data_set[start_idx:end_idx]

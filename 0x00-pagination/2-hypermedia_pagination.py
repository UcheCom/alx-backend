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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """This returns a dictionary containing the following key-value pairs:
           page_size: the length of the returned dataset page
           page: the current page number
           data: the dataset page (equivalent to return from previous task)
           next_page: number of the next page, None if no next page
           prev_page: number of the previous page, None if no previous page
           total_pages: the total number of pages in the dataset as an integer
        """
        dic_t = {}
        data = self.get_page(page, page_size)
        dic_t['page_size'] = len(data)
        dic_t['page'] = page
        dic_t['data'] = data
        tot_page = math.ceil(len(self.dataset()) / page_size)
        dic_t['next_page'] = None if page >= tot_page else page + 1
        dic_t['prev_page'] = None if page == 1 else page - 1
        dic_t['total_pages'] = tot_page
        return dic_t

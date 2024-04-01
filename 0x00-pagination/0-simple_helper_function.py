#!/usr/bin/env python3
"""Module shows simple helper function"""


def index_range(page, page_size):
    """function returns a tuple of size
    two containing a start index and an end index
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)

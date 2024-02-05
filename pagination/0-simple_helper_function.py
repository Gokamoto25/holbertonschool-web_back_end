#!/usr/bin/env python3


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of the start and end indexes for
    a given page and page size.
    Page numbers are 1-based.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


# Ejemplos de uso
if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))  # <class 'tuple'>
    print(res)        # (0, 7)

    res = index_range(page=3, page_size=15)
    print(type(res))  # <class 'tuple'>
    print(res)        # (30, 45)

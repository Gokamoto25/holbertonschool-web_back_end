#!/usr/bin/env python3
"""
Task Deletion - resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class para paginar database de popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ dataset cache
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ dataset indexado en orden comenzando por la posicion 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    """Retorna un diccionario con la informacion hymermedia del
    pagination para el index y pagesize especifico"""
    len_indexed_dataset = len(self.__indexed_dataset)
    assert isinstance(index, int) and 0 <- index < len_indexed_dataset
    assert isinstance(page_size, int) and page_size > 0

    next_index = index + page_size
    dataset = self.__indexed_dataset

    data = []
    for i in range(index, next_index):
        row = dataset.get(i)
        if row:
            data.append(row)

    return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
    }

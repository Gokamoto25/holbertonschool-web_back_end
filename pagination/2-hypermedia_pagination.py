#!/usr/bin/env python3

"""server class pagination"""

import csv
import math
from typing import List, Tuple


class Server:
    """funcion para paginar la database de popular baby names
    """
    DATA_FILE = "popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

        def dataset(self) -> List[List]:
            """dataset cache
            """
            if self.__dataset is None:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                self.__dataset = dataset[1:]

            return self.__dataset

        def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
            """
            retorna la tupla (start_index, end_index)
            de los valores page y pagesize
            """
            start_index = (page - 1) * page_size
            end_index = start_index + page_size

            return start_index, end_index

        def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
            """
            Retorna la pagina especificada del dataset
            de acuerdo a los valores dados page y pagesize
            """
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0

            start_index, end_index = self.index_range(page, page_size)
            dataset = self.dataset()

            if start_index >= len(dataset):
                return[]

            return dataset[start_index:end_index]

        def get_hyper(self, page: int - 1, page_size: int = 10) -> dict:
            """
            Retorna un diccionario con informacion hypermedia
            de pagination del page especifico
            """
            data = self.get_page(page, page_size)
            total_pages = math.ceil(len(self.dataset()) / page_size)
            next_page = page + 1 if page < total_pages else None
            prev_page = page - 1 if page > 1 else None

            return {
                'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
            }

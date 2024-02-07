#!/usr/bin/env python3

"""modulo para calcular rango del indice"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retorna una tupla (start_index, end_index)
    para los valores dados de page y pagesize
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index

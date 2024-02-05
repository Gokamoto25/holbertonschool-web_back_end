#!/usr/bin/env python3


def index_range(page: int, page_size: int) -> tuple:
    """
    Devuelve una tupla de los índices inicial
    y final para una página y un tamaño de página determinados.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


if __name__ == "__main__":
    """
    se ejecutará solo si el script se ejecuta como programa
    principal
    """
    res = index_range(1, 7)
    print(type(res))  # <class 'tuple'>
    print(res)        # (0, 7)

    res = index_range(page=3, page_size=15)
    print(type(res))  # <class 'tuple'>
    print(res)        # (30, 45)

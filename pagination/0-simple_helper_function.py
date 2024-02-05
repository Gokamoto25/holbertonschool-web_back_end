#!/usr/bin/env python3


def index_range(page: int, page_size: int) -> tuple:
    """
    Devuelve una tupla de los índices inicial
    y final para una página y un tamaño de página determinados.

    Parametros:
    - pagina (int): el numero de pagina (basado en 1).
    - page_size (int): el tamaño de cada página.

    Return:
    tupla: una tupla que contiene los índices inicial y final.

    Ejemplo:
    >>> index_range(1, 7)
    (0, 7)

    >>> index_range(page=3, page_size=15)
    (30, 45)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


if __name__ == "__main__":
    """
    se ejecutará solo si el script se ejecuta como programa
    principal

    Example:
    >>> python script.py
    El código dentro de este bloque se ejecutará.

    Atributos: - res: Variable utilizada para almacenar el
    resultado de llamar a la función index_range.

    Uso: Este bloque se usa comúnmente para probar o ejecutar
    código específico cuando el script se ejecuta directamente.
    """
    res = index_range(1, 7)
    print(type(res))  # <class 'tuple'>
    print(res)        # (0, 7)

    res = index_range(page=3, page_size=15)
    print(type(res))  # <class 'tuple'>
    print(res)        # (30, 45)

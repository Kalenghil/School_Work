from functools import lru_cache
def moves(a, b):
    return (a - 1, b), (a * 4, b), (a, b - 1), (a, b * 4)


@lru_cache(None)
def check()
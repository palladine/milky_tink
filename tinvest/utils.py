import functools
import time


def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        res = func(*args, **kwargs)
        total = time.monotonic() - start
        print(f'{func.__name__}: {total:.4f} sec')
        return res
    return wrapper



def async_timed():
    def wrapper(func):
        @functools.wraps(func)
        async def wrapped(*args, **kwargs):
            start = time.monotonic()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.monotonic()
                total = end - start
                print(f'{func.__name__}: {total:.4f} sec')
        return wrapped
    return wrapper
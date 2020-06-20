from concurrent.futures.thread import ThreadPoolExecutor
from typing import Any, Callable


def run_in_threadpool(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any):
        with ThreadPoolExecutor(1) as executor:
            future = executor.submit(func, *args, **kwargs)
            while not future.done():
                pass
            return future.result()

    return wrapper

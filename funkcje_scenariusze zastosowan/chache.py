import time
import functools
@functools.lru_cache(100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time.time()
for n in range(3300):
    result = fib(n)
    print('{0:2d}  {1}, time = {2:3.2f}'.format(n, result, time.time() - start))

print(fib.cache_info())

import math
import timeit
from concurrent.futures import as_completed
from concurrent.futures import ProcessPoolExecutor
from functools import partial

def func(x):
    return float(math.cos(x) + math.sin(x))
def integrate(f, a, b, *, n_iter = 10000):
    h = (b - a) / n_iter
    i = a + h
    sum = 0
    while i <= b-h:
        sum += f(i)
        i += h
    sum += (f(b) + f(a)) / 2
    sum *= h
    return float(sum)
def integrate_async(f, a, b, job, *, n_iter=10000):
    ex = ProcessPoolExecutor(max_workers = job)
    sp = partial(ex.submit, integrate, f, n_iter = n_iter // job)
    st = (b - a) / job
    fs = [sp(a + i * st, a + (i + 1) * st) for i in range(job)]
    return sum(f.result() for f in as_completed(fs))

if __name__ == "__main__":
    print("Res: ", integrate(func, 0, 20))
    print("Time: ", timeit.timeit('integrate(func, 0, 20)', globals = globals(), number = 100), "\n")
    print("2 Threads: ", integrate_async(func, 0, 20, 2))
    print("Time: " ,timeit.timeit('integrate_async(func, 0, 20, 2)', globals = globals(), number = 100), "\n")
    print("4 Threads: ", integrate_async(func, 0, 20, 4))
    print("Time: " ,timeit.timeit('integrate_async(func, 0, 20, 4)', globals = globals(), number = 100), "\n")
    print("6 Threads: ", integrate_async(func, 0, 20, 6))
    print("Time: " ,timeit.timeit('integrate_async(func, 0, 20, 2)', globals = globals(), number = 100), "\n")

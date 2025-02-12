import time
import random
import numpy as np

# Methods are purely focused on computation. Printing is removed entirely so to not interfere with benchmarking.
def loop_method(n):
    numbers = []
    for _ in range(n):
        numbers.append(round(random.uniform(0, 100), 2))
    return numbers

def numpy_method(n):
    return np.round(np.random.uniform(0, 100, size=n), 2)

def benchmark(sizes):
    print(f"{'Size':>10} {'Loop':>12} {'NumPy':>12} {'Loop/NumPy':>12}")
    print("-" * 48)
    
    for n in sizes:
        loop_times = []
        numpy_times = []
        
        for _ in range(3):
            start = time.perf_counter()
            _ = loop_method(n)
            loop_times.append(time.perf_counter() - start)

            start = time.perf_counter()
            _ = numpy_method(n)
            numpy_times.append(time.perf_counter() - start)
        
        loop_avg = sum(loop_times) / len(loop_times)
        numpy_avg = sum(numpy_times) / len(numpy_times)
        ratio = loop_avg / numpy_avg

        print(f"{n:10d} {loop_avg:12.6f} {numpy_avg:12.6f} {ratio:12.2f}")

# Test with exponentially increasing sizes
sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
benchmark(sizes)

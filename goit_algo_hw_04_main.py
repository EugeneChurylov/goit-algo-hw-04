import timeit
import random

from goit_algo_hw_04_merge_sort import merge_sort
from goit_algo_hw_04_insertion_sort import insertion_sort

if __name__ == '__main__':
    small_list = [random.randint(0, 1000) for _ in range(1000)]
    big_list = [random.randint(0, 10000) for _ in range(10000)]

    time_small_insertion_sort = timeit.timeit(lambda: insertion_sort(small_list[:]), number=10)
    time_small_merge_sort = timeit.timeit(lambda: merge_sort(small_list[:]), number=10)
    time_small_timsort_sorted = timeit.timeit(lambda: sorted(small_list[:]), number=10)
    time_small_timsort_sort = timeit.timeit(lambda: small_list[:].sort(), number=10)

    time_big_insertion_sort = timeit.timeit(lambda: insertion_sort(big_list[:]), number=10)
    time_big_merge_sort = timeit.timeit(lambda: merge_sort(big_list[:]), number=10)
    time_big_timsort_sorted = timeit.timeit(lambda: sorted(big_list[:]), number=10)
    time_big_timsort_sort = timeit.timeit(lambda: big_list[:].sort(), number=10)

    print(f"{'| Algorithm': <20} | {'Small list time': <20} | {'Big list time': <20}")
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}")

    print(f"{'| Insertion sort': <20} | {time_small_insertion_sort:<20.5f} | {time_big_insertion_sort:<20.5f}")
    print(f"{'| Merge sort': <20} | {time_small_merge_sort:<20.5f} | {time_big_merge_sort:<20.5f}")
    print(f"{'| Tim sort sorted': <20} | {time_small_timsort_sorted:<20.5f} | {time_big_timsort_sorted:<20.5f}")
    print(f"{'| Tim sort sort': <20} | {time_small_timsort_sort:<20.5f} | {time_big_timsort_sort:<20.5f}")
    
# python -m cProfile -s cumulative profiling_example.py

import random

NUM_ITEMS = 10000


def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(f"Number of Comparisons ==> {comparisons}")


def main():
    arr = [random.randint(1, 100) for _ in range(NUM_ITEMS)]
    insertion_sort(arr)


main()

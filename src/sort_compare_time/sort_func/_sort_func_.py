import timeit
import random
import matplotlib.pyplot as plt


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def tim_sort(arr):
    arr.sort()


def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]


def run_sorting_algorithm(algorithm, size):
    setup_code = f"from _sort_func_ import {algorithm}, generate_random_data; data = generate_random_data({size});"
    stmt = f"{algorithm}(data)"
    time = timeit.timeit(stmt, setup=setup_code, number=10)
    return time


def main(data_sizes):
    algorithms = {
        "Merge Sort": "merge_sort",
        "Insertion Sort": "insertion_sort",
        "TimSort": "tim_sort",
    }

    results = {alg: [] for alg in algorithms}

    for size in data_sizes:
        for title, algorithm in algorithms.items():
            execution_time = run_sorting_algorithm(algorithm, size)
            results[title].append(execution_time)
    return results


if __name__ == "__main__":
    data_sizes = [100, 500, 1000, 3000]
    main(data_sizes)

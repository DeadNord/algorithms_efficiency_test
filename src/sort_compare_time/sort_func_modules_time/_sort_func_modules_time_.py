import random
import sys
import importlib

module_path = "src/helper/time_measurer"
if module_path not in sys.path:
    sys.path.append(module_path)
time_measurer_module = importlib.import_module("time_measurer")
TimeMeasurer = time_measurer_module.TimeMeasurer


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
    if algorithm == "merge_sort":
        func = merge_sort
    elif algorithm == "insertion_sort":
        func = insertion_sort
    elif algorithm == "tim_sort":
        func = tim_sort
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    data = generate_random_data(size)

    time_measurer = TimeMeasurer()
    _, execution_time = time_measurer.measure_time(func, data)

    return execution_time


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

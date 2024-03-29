import timeit
import random
import matplotlib.pyplot as plt
import importlib.util


def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]


def run_sorting_algorithm(module_name, algorithm, size):
    module = importlib.import_module(module_name)
    func = getattr(module, algorithm)
    data = generate_random_data(size)

    setup_code = f"from {module_name} import {algorithm}"

    stmt = f"{algorithm}(data)"

    time = timeit.timeit(
        stmt=stmt, setup=setup_code, number=10, globals={"data": data, algorithm: func}
    )
    return time


def main(data_sizes):
    algorithms = {
        "Merge Sort": ("merge_sort", "merge_sort"),
        "Insertion Sort": ("insertion_sort", "insertion_sort"),
        "TimSort": ("tim_sort", "tim_sort"),
    }

    results = {alg: [] for alg in algorithms}

    for size in data_sizes:
        for title, (module_name, algorithm) in algorithms.items():
            execution_time = run_sorting_algorithm(module_name, algorithm, size)
            results[title].append(execution_time)
    return results


if __name__ == "__main__":
    data_sizes = [100, 500, 1000, 3000]
    main(data_sizes)

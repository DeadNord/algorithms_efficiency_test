import random
import sys
import importlib

module_path = "src/helper/time_measurer"
if module_path not in sys.path:
    sys.path.append(module_path)
time_measurer_module = importlib.import_module("time_measurer")
TimeMeasurer = time_measurer_module.TimeMeasurer


def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]


def run_sorting_algorithm(module_name, algorithm, size):
    # Динамический импорт модуля и функции
    module = importlib.import_module(module_name)
    func = getattr(module, algorithm)
    data = generate_random_data(size)

    # Использование TimeMeasurer для измерения времени выполнения функции
    time_measurer = TimeMeasurer()
    _, execution_time = time_measurer.measure_time(func, data)
    return execution_time


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

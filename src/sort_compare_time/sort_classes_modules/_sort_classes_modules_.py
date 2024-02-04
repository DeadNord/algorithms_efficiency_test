import random
import matplotlib.pyplot as plt
import sys
import importlib.util
from tabulate import tabulate

module_path = "src/helper/time_measurer"
if module_path not in sys.path:
    sys.path.append(module_path)
time_measurer_module = importlib.import_module("time_measurer")
TimeMeasurer = time_measurer_module.TimeMeasurer


class SortingAlgorithm:
    def __init__(self):
        self.sort_func = None

    def sort(self, data):
        if self.sort_func:
            return self.sort_func(data)
        else:
            raise NotImplementedError("Sort function not defined")


class MergeSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        from merge_sort import merge_sort

        self.sort_func = merge_sort


class InsertionSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        from insertion_sort import insertion_sort

        self.sort_func = insertion_sort


class TimSort(SortingAlgorithm):
    def __init__(self):
        super().__init__()
        from tim_sort import tim_sort

        self.sort_func = tim_sort


class SortingHandler:
    def __init__(self):
        self.algorithms = {
            "Merge Sort": MergeSort(),
            "Insertion Sort": InsertionSort(),
            "TimSort": TimSort(),
        }

    def perform_sorting(self, algorithm_name, data):
        algorithm = self.algorithms.get(algorithm_name)
        if not algorithm:
            raise ValueError(f"Algorithm {algorithm_name} not found")
        return algorithm.sort(data)


class ResultHandler:
    @staticmethod
    def display_table(data_sizes, results):
        headers = ["Data Size"] + list(results.keys())
        table_data = [
            [size] + [results[algorithm][i] for algorithm in results]
            for i, size in enumerate(data_sizes)
        ]
        print(tabulate(table_data, headers=headers, tablefmt="pipe"))

    @staticmethod
    def plot_results(data_sizes, results):
        for algorithm, execution_times in results.items():
            plt.plot(data_sizes, execution_times, label=algorithm)
        plt.xlabel("Data Size")
        plt.ylabel("Execution Time (seconds)")
        plt.title("Sorting Algorithm Comparison")
        plt.legend()
        plt.show()


class MainProgram:
    def __init__(self, data_sizes):
        self.sorter = SortingHandler()
        self.measurer = TimeMeasurer()
        self.data_sizes = data_sizes
        self.results = {alg: [] for alg in self.sorter.algorithms}

    def run(self):
        for size in self.data_sizes:
            data = generate_random_data(size)

            for title in self.sorter.algorithms:
                _, execution_time = self.measurer.measure_time(
                    self.sorter.perform_sorting, title, data
                )
                self.results[title].append(execution_time)

        return self.results

    # ResultHandler.display_table(self.data_sizes, self.results)
    # ResultHandler.plot_results(self.data_sizes, self.results)


def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]


if __name__ == "__main__":
    data_sizes = [100, 500, 1000, 3000]
    program = MainProgram(data_sizes)
    program.run()

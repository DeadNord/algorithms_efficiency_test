from tabulate import tabulate
import matplotlib.pyplot as plt
from greedy_change_maker import GreedyChangeMaker
from dynamic_change_maker import DynamicChangeMaker
import sys
import importlib.util

module_path = "src/helper/time_measurer"
if module_path not in sys.path:
    sys.path.append(module_path)
time_measurer_module = importlib.import_module("time_measurer")
TimeMeasurer = time_measurer_module.TimeMeasurer


class ChangeMakerHandler:
    def __init__(self, denominations):
        self.greedy_maker = GreedyChangeMaker(denominations)
        self.dynamic_maker = DynamicChangeMaker(denominations)

    def find_coins_greedy(self, amount):
        return self.greedy_maker.find_coins(amount)

    def find_coins_dynamic(self, amount):
        return self.dynamic_maker.find_coins(amount)


class ResultHandler:
    @staticmethod
    def plot_results(test_amounts, greedy_times, dynamic_times):
        plt.plot(test_amounts, greedy_times, label="Greedy Algorithm", marker="o")
        plt.plot(test_amounts, dynamic_times, label="Dynamic Algorithm", marker="o")
        plt.xlabel("Amount")
        plt.ylabel("Time (s)")
        plt.title("Algorithm Performance Comparison")
        plt.legend()
        plt.show()

    @staticmethod
    def display_tables(algorithm_results, times):
        result_headers = ["Amount", "Greedy Result", "Dynamic Result"]
        result_table = tabulate(
            algorithm_results, headers=result_headers, tablefmt="pipe"
        )
        print(result_table + "\n")

        time_headers = [
            "Amount",
            "Greedy Algorithm Time (s)",
            "Dynamic Algorithm Time (s)",
        ]
        time_table = tabulate(times, headers=time_headers, tablefmt="pipe")
        print(time_table + "\n")


def main(denominations, test_amounts):
    handler = ChangeMakerHandler(denominations)
    measurer = TimeMeasurer()

    greedy_times = []
    dynamic_times = []
    results = []
    algorithm_results = []

    for amount in test_amounts:
        greedy_result, greedy_time = measurer.measure_time(
            handler.find_coins_greedy, amount
        )
        dynamic_result, dynamic_time = measurer.measure_time(
            handler.find_coins_dynamic, amount
        )

        greedy_times.append(greedy_time)
        dynamic_times.append(dynamic_time)
        results.append([amount, greedy_time, dynamic_time])
        algorithm_results.append([amount, greedy_result, dynamic_result])

    ResultHandler.display_tables(algorithm_results, results)
    ResultHandler.plot_results(test_amounts, greedy_times, dynamic_times)


if __name__ == "__main__":
    denominations = [50, 25, 10, 5, 2, 1]
    test_amounts = [87, 143, 289, 498, 1023, 3764]
    main(denominations, test_amounts)

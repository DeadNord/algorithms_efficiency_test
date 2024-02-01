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


def main(denominations, test_amounts):
    greedy_maker = GreedyChangeMaker(denominations)
    dynamic_maker = DynamicChangeMaker(denominations)

    measurer = TimeMeasurer()

    greedy_times = []
    dynamic_times = []

    results = []
    algorithm_results = []

    for amount in test_amounts:
        greedy_result, greedy_time = measurer.measure_time(
            greedy_maker.find_coins, amount
        )
        dynamic_result, dynamic_time = measurer.measure_time(
            dynamic_maker.find_coins, amount
        )

        greedy_times.append(greedy_time)
        dynamic_times.append(dynamic_time)

        results.append([amount, greedy_time, dynamic_time])
        algorithm_results.append([amount, greedy_result, dynamic_result])

    result_headers = ["Amount", "Greedy Result", "Dynamic Result"]
    result_table = tabulate(algorithm_results, headers=result_headers, tablefmt="pipe")
    print(result_table + "\n")

    time_headers = ["Amount", "Greedy Algorithm Time (s)", "Dynamic Algorithm Time (s)"]
    time_table = tabulate(results, headers=time_headers, tablefmt="pipe")
    print(time_table + "\n")

    plt.plot(test_amounts, greedy_times, label="Greedy Algorithm", marker="o")
    plt.plot(test_amounts, dynamic_times, label="Dynamic Algorithm", marker="o")
    plt.xlabel("Amount")
    plt.ylabel("Time (s)")
    plt.title("Algorithm Performance Comparison")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    denominations = [50, 25, 10, 5, 2, 1]
    test_amounts = [87, 143, 289, 498, 1023, 3764]
    main(denominations, test_amounts)

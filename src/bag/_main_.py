import time
from tabulate import tabulate
import matplotlib.pyplot as plt
from greedy_change_maker import GreedyChangeMaker
from dynamic_change_maker import DynamicChangeMaker


def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time


def main(denominations, test_amounts):
    greedy_maker = GreedyChangeMaker(denominations)
    dynamic_maker = DynamicChangeMaker(denominations)

    greedy_times = []
    dynamic_times = []

    results = []

    for amount in test_amounts:
        greedy_result, greedy_time = measure_time(greedy_maker.find_coins, amount)
        dynamic_result, dynamic_time = measure_time(dynamic_maker.find_coins, amount)

        greedy_times.append(greedy_time)
        dynamic_times.append(dynamic_time)

        results.append([amount, greedy_time, dynamic_time])

        print(
            f"Amount: {amount}, Greedy Result: {greedy_result}, Dynamic Result: {dynamic_result}"
        )

    headers = ["Amount", "Greedy Algorithm Time (s)", "Dynamic Algorithm Time (s)"]
    table = tabulate(results, headers=headers, tablefmt="pipe")
    print(f"{table}\n")

    plt.plot(test_amounts, greedy_times, label="Greedy Algorithm", marker="o")
    plt.plot(test_amounts, dynamic_times, label="Dynamic Algorithm", marker="o")
    plt.xlabel("Amount")
    plt.ylabel("Time (s)")
    plt.title("Algorithm Performance Comparison")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    denominations = [50, 25, 10, 5, 2, 1]
    test_amounts = [113]
    main(denominations, test_amounts)

    denominations = [50, 25, 10, 5, 2, 1]
    test_amounts = [87, 143, 289, 498, 1023, 3764]
    main(denominations, test_amounts)

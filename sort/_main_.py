def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]


def run_sorting_algorithm(algorithm, size):
    setup_code = f"from __main__ import {algorithm}, generate_random_data; data = generate_random_data({size});"
    stmt = f"{algorithm}(data)"
    time = timeit.timeit(stmt, setup=setup_code, number=10)
    return time


def plot_results(data_sizes, results):
    for algorithm, execution_time in results.items():
        plt.plot(data_sizes, execution_time, label=algorithm)

    plt.xlabel("Data Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Comparison")
    plt.legend()
    plt.show()


def main():
    data_sizes = [100, 500, 1000, 3000]
    algorithms = {
        "Merge Sort": "merge_sort",
        "Insertion Sort": "insertion_sort",
        "TimSort": "tim_sort",
    }

    results = {alg: [] for alg in algorithms}

    for size in data_sizes:
        print(f"\nData Size: {size}")
        for title, algorithm in algorithms.items():
            execution_time = run_sorting_algorithm(algorithm, size)
            results[title].append(execution_time)
            print(f"{title}: {execution_time} seconds")

    plot_results(data_sizes, results)


if __name__ == "__main__":
    main()

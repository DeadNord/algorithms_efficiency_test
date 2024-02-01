from tabulate import tabulate
import matplotlib.pyplot as plt
import sys
import importlib.util

data_sizes = [100, 500, 1000, 3000]

# Sort Function
module_path = "src/sort_compare/sort_func"
if module_path not in sys.path:
    sys.path.append(module_path)
sort_func_module = importlib.import_module("_sort_func_")
sort_func = sort_func_module.main
sort_func_results = sort_func(data_sizes)

# Sort Function with import Algorithms
module_path = "src/sort_compare/sort_func_modules_algs"
if module_path not in sys.path:
    sys.path.append(module_path)
sort_func_modules_algs_module = importlib.import_module("_sort_func_modules_algs_")
sort_func_modules_algs = sort_func_modules_algs_module.main
sort_func_modules_algs_results = sort_func_modules_algs(data_sizes)

# Sort Function with import TimeMeasurer
module_path = "src/sort_compare/sort_func_modules_time"
if module_path not in sys.path:
    sys.path.append(module_path)
sort_func_modules_time_module = importlib.import_module("_sort_func_modules_time_")
sort_func_modules_time = sort_func_modules_time_module.main
sort_func_modules_time_results = sort_func_modules_time(data_sizes)

# Sort Function with import Algorithms & TimeMeasurer
module_path = "src/sort_compare/sort_func_modules_all"
if module_path not in sys.path:
    sys.path.append(module_path)
sort_func_modules_all_module = importlib.import_module("_sort_func_modules_all_")
sort_func_modules_all = sort_func_modules_all_module.main
sort_func_modules_all_results = sort_func_modules_all(data_sizes)

# Sort Classes
module_path = "src/sort_compare/sort_classes"
if module_path not in sys.path:
    sys.path.append(module_path)
sort_classes_module = importlib.import_module("_sort_classes_")
SortClasses = sort_classes_module.MainProgram(data_sizes)
sort_classes_results = SortClasses.run()

# Sort Classes with Modules
module_path = "src/sort_compare/sort_classes_modules"
if module_path not in sys.path:
    sys.path.append(module_path)
sort_classes_modules_module = importlib.import_module("_sort_classes_modules_")
SortClassesModules = sort_classes_modules_module.MainProgram(data_sizes)
sort_classes_modules_results = SortClassesModules.run()


algorithms = ["Merge Sort", "Insertion Sort", "TimSort"]
headers = ["Data Size"] + [
    "Sort Function",
    "Sort Func imported TimeMeasurer",
    "Sort Func imported Algs",
    "Sort Func imported Algs & TimeMeasurer",
    "Sort Classes",
    "Sort Classes Modules",
]

for alg in algorithms:
    table_data = []
    for i, size in enumerate(data_sizes):
        row = [size]
        row.append(sort_func_results[alg][i])
        row.append(sort_classes_results[alg][i])
        row.append(sort_classes_modules_results[alg][i])
        row.append(sort_func_modules_algs_results[alg][i])
        row.append(sort_func_modules_time_results[alg][i])
        row.append(sort_func_modules_all_results[alg][i])
        table_data.append(row)
    print(f"Results for {alg}:")
    print(tabulate(table_data, headers=headers, tablefmt="pipe"))
    print("\n")


for alg in algorithms:
    plt.figure(figsize=(10, 6))
    plt.plot(data_sizes, sort_func_results[alg], label="sort_func")
    plt.plot(data_sizes, sort_classes_results[alg], label="sort_classes")
    plt.plot(
        data_sizes, sort_classes_modules_results[alg], label="sort_classes_modules"
    )
    plt.plot(
        data_sizes,
        sort_func_modules_algs_results[alg],
        label="sort_func_modules_algs_results",
    )
    plt.plot(
        data_sizes,
        sort_func_modules_time_results[alg],
        label="sort_func_modules_time_results",
    )
    plt.plot(
        data_sizes,
        sort_func_modules_all_results[alg],
        label="sort_func_modules_all_results",
    )
    plt.xlabel("Data Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title(f"Comparison of {alg}")
    plt.legend()
    plt.show()

from tabulate import tabulate
import matplotlib.pyplot as plt
import sys
import importlib.util

module_path = "src/helper/time_measurer"
if module_path not in sys.path:
    sys.path.append(module_path)
time_measurer_module = importlib.import_module("time_measurer")
TimeMeasurer = time_measurer_module.TimeMeasurer


class StringSearchAlgorithm:
    def __init__(self):
        self.search_func = None

    def search(self, text, pattern):
        if self.search_func:
            return self.search_func(text, pattern)
        else:
            raise NotImplementedError("Search method not implemented")


class BoyerMoore(StringSearchAlgorithm):
    def __init__(self):
        super().__init__()
        from boyer_moore import boyer_moore

        self.search_func = boyer_moore


class KnuthMorrisPratt(StringSearchAlgorithm):
    def __init__(self):
        super().__init__()
        from knuth_morris_pratt import knuth_morris_pratt

        self.search_func = knuth_morris_pratt


class RabinKarp(StringSearchAlgorithm):
    def __init__(self):
        super().__init__()
        from rabin_karp import rabin_karp

        self.search_func = rabin_karp


class StringSearch(StringSearchAlgorithm):
    def __init__(self):
        from string_search import (
            string_search as ss_search,
        )

        self.search_func = ss_search

    def search(self, text, pattern):
        return self.search_func(text, pattern)


class StringSearchHandler:
    def __init__(self):
        self.algorithms = {
            "Boyer_Moore": BoyerMoore(),
            "Knuth_Morris_Pratt": KnuthMorrisPratt(),
            "Rabin_Karp": RabinKarp(),
            "String_Search": StringSearch(),
        }

    def perform_search(self, algorithm_name, text, pattern):
        algorithm = self.algorithms.get(algorithm_name)
        if not algorithm:
            raise ValueError(f"Algorithm {algorithm_name} not found")
        return algorithm.search(text, pattern)


class ResultHandler:
    @staticmethod
    def display_table(data, headers):
        print(tabulate(data, headers=headers, tablefmt="pipe"))

    @staticmethod
    def plot_results(algorithms, real_times, fake_times, title):
        plt.figure(figsize=(10, 6))
        x = range(len(algorithms))
        width = 0.4

        real_times_list = (
            [real_times[alg][0] for alg in algorithms if real_times[alg]]
            if real_times
            else []
        )
        fake_times_list = (
            [fake_times[alg][0] for alg in algorithms if fake_times[alg]]
            if fake_times
            else []
        )

        if real_times_list and fake_times_list:
            plt.bar(x, real_times_list, width=width, label="Real Data", align="center")
            plt.bar(
                [i + width for i in x],
                fake_times_list,
                width=width,
                label="Fake Data",
                align="center",
            )
        elif real_times_list:
            plt.bar(x, real_times_list, width=width, label="Real Data", align="center")
        elif fake_times_list:
            plt.bar(x, fake_times_list, width=width, label="Fake Data", align="center")

        plt.xticks(
            [i + width / 2 for i in x] if real_times_list and fake_times_list else x,
            algorithms,
        )
        plt.xlabel("Algorithms")
        plt.ylabel("Execution Time (seconds)")
        plt.title(title)
        plt.legend()
        plt.show()


class MainProgram:
    def __init__(self, text_file1, text_file2):
        self.text1 = self.read_text_file(text_file1)
        self.text2 = self.read_text_file(text_file2)
        self.searcher = StringSearchHandler()
        self.measurer = TimeMeasurer()

    def read_text_file(self, file_path):
        with open(file_path, "rb") as file:
            return file.read().decode("utf-8", "replace")

    def run(self, real_data=True, fake_data=True):
        algorithms = [
            "Boyer_Moore",
            "Knuth_Morris_Pratt",
            "Rabin_Karp",
            "String_Search",
        ]

        real_times_text1, real_times_text2 = {alg: [] for alg in algorithms}, {
            alg: [] for alg in algorithms
        }
        fake_times_text1, fake_times_text2 = {alg: [] for alg in algorithms}, {
            alg: [] for alg in algorithms
        }

        real_pattern_text1 = self.text1[200:205] if real_data else ""
        real_pattern_text2 = self.text2[300:305] if real_data else ""
        fake_pattern = "abcdefgh" if fake_data else ""

        for algorithm in algorithms:
            if real_data:
                _, time_text1 = self.measurer.measure_time(
                    self.searcher.perform_search,
                    algorithm,
                    self.text1,
                    real_pattern_text1,
                )
                _, time_text2 = self.measurer.measure_time(
                    self.searcher.perform_search,
                    algorithm,
                    self.text2,
                    real_pattern_text2,
                )
                real_times_text1[algorithm].append(time_text1)
                real_times_text2[algorithm].append(time_text2)

            if fake_data:
                _, time_text1 = self.measurer.measure_time(
                    self.searcher.perform_search, algorithm, self.text1, fake_pattern
                )
                _, time_text2 = self.measurer.measure_time(
                    self.searcher.perform_search, algorithm, self.text2, fake_pattern
                )
                fake_times_text1[algorithm].append(time_text1)
                fake_times_text2[algorithm].append(time_text2)

        table_data = []
        for algorithm in algorithms:
            row = [
                algorithm,
                f"{real_times_text1[algorithm][0]:.6f} sec"
                if real_times_text1[algorithm]
                else "-",
                f"{fake_times_text1[algorithm][0]:.6f} sec"
                if fake_times_text1[algorithm]
                else "-",
                f"{real_times_text2[algorithm][0]:.6f} sec"
                if real_times_text2[algorithm]
                else "-",
                f"{fake_times_text2[algorithm][0]:.6f} sec"
                if fake_times_text2[algorithm]
                else "-",
            ]
            table_data.append(row)

        headers = [
            "Algorithm",
            "Real Substring (Text 1)",
            "Fake Substring (Text 1)",
            "Real Substring (Text 2)",
            "Fake Substring (Text 2)",
        ]
        ResultHandler.display_table(table_data, headers)

        if real_data or fake_data:
            ResultHandler.plot_results(
                algorithms,
                real_times_text1 if real_data else [],
                fake_times_text1 if fake_data else [],
                "Performance in Text 1",
            )
            ResultHandler.plot_results(
                algorithms,
                real_times_text2 if real_data else [],
                fake_times_text2 if fake_data else [],
                "Performance in Text 2",
            )


if __name__ == "__main__":
    program = MainProgram(
        "./src/search/data/article_1.txt", "./src/search/data/article_2.txt"
    )
    program.run(real_data=True, fake_data=True)
    program.run(real_data=True, fake_data=False)
    program.run(real_data=False, fake_data=True)

import timeit
from tabulate import tabulate
import matplotlib.pyplot as plt


class StringSearchAlgorithm:
    def search(self, text, pattern):
        raise NotImplementedError("Search method not implemented")


class BoyerMoore(StringSearchAlgorithm):
    def __init__(self):
        from boyer_moore import (
            boyer_moore as bm_search,
        )

        self.search_func = bm_search

    def search(self, text, pattern):
        return self.search_func(text, pattern)


class KnuthMorrisPratt(StringSearchAlgorithm):
    def __init__(self):
        from knuth_morris_pratt import (
            knuth_morris_pratt as kmp_search,
        )

        self.search_func = kmp_search

    def search(self, text, pattern):
        return self.search_func(text, pattern)


class RabinKarp(StringSearchAlgorithm):
    def __init__(self):
        from rabin_karp import (
            rabin_karp as rk_search,
        )

        self.search_func = rk_search

    def search(self, text, pattern):
        return self.search_func(text, pattern)


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


class TimeMeasurer:
    @staticmethod
    def measure_time(func, *args):
        start_time = timeit.default_timer()
        result = func(*args)
        end_time = timeit.default_timer()
        return result, end_time - start_time


class ResultPlotter:
    @staticmethod
    def plot_results(algorithms, real_times, fake_times, title):
        plt.figure(figsize=(10, 6))
        x = range(len(algorithms))
        width = 0.4

        if real_times and fake_times:
            # Оба набора данных доступны
            plt.bar(x, real_times, width=width, label="Real Data", align="center")
            plt.bar(
                [i + width for i in x],
                fake_times,
                width=width,
                label="Fake Data",
                align="center",
            )
            plt.xticks([i + width / 2 for i in x], algorithms)
        elif real_times:
            # Только реальные данные
            plt.bar(x, real_times, width=width, label="Real Data", align="center")
            plt.xticks(x, algorithms)
        elif fake_times:
            # Только фейковые данные
            plt.bar(x, fake_times, width=width, label="Fake Data", align="center")
            plt.xticks(x, algorithms)

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
        self.plotter = ResultPlotter()

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
        real_pattern_text1 = self.text1[200:205] if real_data else ""
        real_pattern_text2 = self.text2[300:305] if real_data else ""
        fake_pattern = "abcdefgh" if fake_data else ""

        real_times_text1, real_times_text2, fake_times_text1, fake_times_text2 = (
            [],
            [],
            [],
            [],
        )

        for algorithm in algorithms:
            if real_data:
                _, real_time_text1 = self.measurer.measure_time(
                    self.searcher.perform_search,
                    algorithm,
                    self.text1,
                    real_pattern_text1,
                )
                _, real_time_text2 = self.measurer.measure_time(
                    self.searcher.perform_search,
                    algorithm,
                    self.text2,
                    real_pattern_text2,
                )
                real_times_text1.append(real_time_text1)
                real_times_text2.append(real_time_text1)

            if fake_data:
                _, fake_time_text1 = self.measurer.measure_time(
                    self.searcher.perform_search, algorithm, self.text1, fake_pattern
                )
                _, fake_time_text2 = self.measurer.measure_time(
                    self.searcher.perform_search, algorithm, self.text2, fake_pattern
                )
                fake_times_text1.append(fake_time_text1)
                fake_times_text2.append(fake_time_text2)

        # Формування та виведення таблиць результатів з урахуванням наявності реальних та фейкових даних
        table = [
            [
                "Algorithm",
                "Real Substring (Text 1)",
                "Fake Substring (Text 1)",
                "Real Substring (Text 2)",
                "Fake Substring (Text 2)",
            ],
            [
                "Boyer-Moore",
                f"{real_times_text1[0]:.6f} sec" if real_times_text1 else "-",
                f"{fake_times_text1[0]:.6f} sec" if fake_times_text1 else "-",
                f"{real_times_text2[0]:.6f} sec" if real_times_text2 else "-",
                f"{fake_times_text2[0]:.6f} sec" if fake_times_text2 else "-",
            ],
            [
                "Knuth-Morris-Pratt",
                f"{real_times_text1[1]:.6f} sec" if real_times_text1 else "-",
                f"{fake_times_text1[1]:.6f} sec" if fake_times_text1 else "-",
                f"{real_times_text2[1]:.6f} sec" if real_times_text2 else "-",
                f"{fake_times_text2[1]:.6f} sec" if fake_times_text2 else "-",
            ],
            [
                "Rabin-Karp",
                f"{real_times_text1[2]:.6f} sec" if real_times_text1 else "-",
                f"{fake_times_text1[2]:.6f} sec" if fake_times_text1 else "-",
                f"{real_times_text2[2]:.6f} sec" if real_times_text2 else "-",
                f"{fake_times_text2[2]:.6f} sec" if fake_times_text2 else "-",
            ],
            [
                "String-Search",
                f"{real_times_text1[3]:.6f} sec" if real_times_text1 else "-",
                f"{fake_times_text1[3]:.6f} sec" if fake_times_text1 else "-",
                f"{real_times_text2[3]:.6f} sec" if real_times_text2 else "-",
                f"{fake_times_text2[3]:.6f} sec" if fake_times_text2 else "-",
            ],
        ]

        print()
        print(tabulate(table, headers="firstrow", tablefmt="github"))

        if real_data or fake_data:
            self.plotter.plot_results(
                algorithms,
                real_times_text1 if real_data else [],
                fake_times_text1 if fake_data else [],
                "Performance in Text 1",
            )
            self.plotter.plot_results(
                algorithms,
                real_times_text2 if real_data else [],
                fake_times_text2 if fake_data else [],
                "Performance in Text 2",
            )


if __name__ == "__main__":
    program = MainProgram("./search/data/article_1.txt", "./search/data/article_2.txt")
    program.run(real_data=True, fake_data=True)
    program.run(real_data=True, fake_data=False)
    program.run(real_data=False, fake_data=True)

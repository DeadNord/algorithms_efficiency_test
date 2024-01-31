import timeit


class TimeMeasurer:
    @staticmethod
    def measure_time(func, *args):
        start_time = timeit.default_timer()
        result = func(*args)
        end_time = timeit.default_timer()
        return result, end_time - start_time

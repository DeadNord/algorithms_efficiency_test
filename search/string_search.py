def string_search(text, pattern):
    index = text.find(pattern)
    iterations = 1

    while index != -1:
        index = text.find(pattern, index + 1)
        iterations += 1

    return iterations, index if iterations > 1 else None

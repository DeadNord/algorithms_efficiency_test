def knuth_morris_pratt(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    prefix_function = [0] * m
    j = 0
    iterations = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_function[j - 1]

        iterations += 1
        if pattern[i] == pattern[j]:
            j += 1

        prefix_function[i] = j

    j = 0
    i = 0

    while i < n:
        iterations += 1
        if text[i] == pattern[j]:
            if j == m - 1:
                return iterations, i - j
            else:
                i += 1
                j += 1
        else:
            if j > 0:
                j = prefix_function[j - 1]
            else:
                i += 1

    return iterations, None

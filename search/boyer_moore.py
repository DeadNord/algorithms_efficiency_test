def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return 0

    last_occurrence = {pattern[i]: i for i in range(m)}
    i = m - 1
    j = m - 1
    iterations = 0

    while i < n:
        iterations += 1
        if text[i] == pattern[j]:
            if j == 0:
                return iterations, i
            else:
                i -= 1
                j -= 1
        else:
            last_occ = last_occurrence.get(text[i], -1)
            i = i + m - min(j, 1 + last_occ)
            j = m - 1

    return iterations, None

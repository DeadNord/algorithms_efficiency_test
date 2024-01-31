def rabin_karp(text, pattern):
    d = 256
    q = 101
    m, n = len(pattern), len(text)
    h_pattern, h_text = 0, 0
    h = 1
    iterations = 0

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        h_pattern = (d * h_pattern + ord(pattern[i])) % q
        h_text = (d * h_text + ord(text[i])) % q
        iterations += 1

    for i in range(n - m + 1):
        iterations += 1
        if h_pattern == h_text:
            if text[i : i + m] == pattern:
                return iterations, i

        if i < n - m:
            h_text = (d * (h_text - ord(text[i]) * h) + ord(text[i + m])) % q
            if h_text < 0:
                h_text += q

    return iterations, None

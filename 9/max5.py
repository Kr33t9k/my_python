def max5(a):
    n = 0
    k = 5
    max_sum = sum(a[n:k])
    while k <= len(a):
        if sum(a[n:k]) > max_sum:
            max_sum = sum(a[n:k])
        n += 1
        k += 1
    return max_sum
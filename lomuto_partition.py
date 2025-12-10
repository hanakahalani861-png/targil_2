def lomuto_partition(a, key=lambda x: x):
    i = -1
    j = 0
    n = len(a)
    if n==1:
        return 0
    while j<n:
        if key(a[n-1]) >= key(a[j]):
            i += 1
            a[i], a[j] = a[j], a[i]
        j += 1
    return i
def hoare_partition(a, key=lambda x: x):
    i = 0
    n = len(a)
    j = n-1
    pivot = 0
    while i<j:
        while i<n and a[i]<a[pivot]:
            i += 1
        while j>-1 and a[j]>=a[pivot]:
            j -= 1
        if i<j:
            a[i], a[j] = a[j], a[i]
            if i == pivot:
                pivot = j
            elif j == pivot:
                pivot = i
    return pivot
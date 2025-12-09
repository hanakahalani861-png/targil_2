def is_sorted(a, key=lambda x: x):
    i = 1
    n = len(a)
    while i<n:
        if key(a[i-1])>key(a[i]):
            return False
        i += 1
    return True

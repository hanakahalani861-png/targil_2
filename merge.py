def merge(a, b, key=lambda x: x):
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    s = []
    while (i<n or j<m):
        if (i==n or (j<m and key(a[i])>key(b[j]))):
            s.append(b[j])
            j += 1
        else:
            s.append(a[i])
            i += 1
    return s

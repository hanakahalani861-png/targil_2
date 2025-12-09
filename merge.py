def merge(a, b, key=lambda x: x):
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    s = []
    while (i<n or j<m):
        if (i==n or (j<m and a[i]>b[j])):
            s.append(b[j])
            j += 1
        else:
            s.append(a[i])
            i += 1
    return s

a = [2,4,6]
b = [1,3,5]
s = merge(a, b)
for i in s:
    print(i)
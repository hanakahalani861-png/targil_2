def is_sorted(a, key=lambda x: x):
    i = 1
    n = len(a)
    while i<n:
        if key(a[i-1])>key(a[i]):
            return False
        i += 1
    return True

a = [3,5,4,8]
if (is_sorted(a, lambda x: 1-x%2)):
    print('true')
else:
    print('false')
def create_random_tuples(n, k, types=None):
    import random
    import string

    if types is None:
        types = [int] * k

    if len(types) != k:
        raise ValueError("Length of types must be equal to k")

    def random_element(t):
        if t == int:
            return random.randint(0, 1000)
        elif t == float:
            return random.uniform(0.0, 1000.0)
        elif t == str:
            return ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        else:
            raise ValueError(f"Unsupported type: {t}")

    result = []
    for _ in range(n):
        tuple_elements = tuple(random_element(t) for t in types)
        result.append(tuple_elements)

    return result

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

a = create_random_tuples(5, 2, [int, str])
b = create_random_tuples(5, 1, [str])
c = create_random_tuples(5, 1, [int])
a_lomuto, a_hoare = a, a
b_lomuto, b_hoare = b, b
c_lomuto, c_hoare = c, c

print('a:')
for i in a:
    print(i)
print()

print('b:')
for i in b:
    print(i)
print()

print('c:')
for i in c:
    print(i)
print()

print('---------------------')

print(lomuto_partition(a_lomuto))
print()
for i in a_lomuto:
    print(i)
print()

print(lomuto_partition(b_lomuto))
print()
for i in b_lomuto:
    print(i)
print()

print(lomuto_partition(c_lomuto))
print()
for i in c_lomuto:
    print(i)
print()

print('------------------------')

print(hoare_partition(a_hoare))
print()
for i in a_hoare:
    print(i)
print()

print(hoare_partition(b_hoare))
print()
for i in b_hoare:
    print(i)
print()

print(hoare_partition(c_hoare))
print()
for i in c_hoare:
    print(i)
print()
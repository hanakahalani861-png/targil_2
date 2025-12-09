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


a = create_random_tuples(6, 3, [int, float, str])

a_sorted_by_int = sorted(a, key=lambda x: x[0])

for i in a_sorted_by_int:
    print(i)
print()

a_sorted_by_flout = sorted(a, key=lambda x: x[1])

for i in a_sorted_by_flout:
    print(i)
print()

a_sorted_by_str = sorted(a, key=lambda x: x[2])

for i in a_sorted_by_str:
    print(i)
print()
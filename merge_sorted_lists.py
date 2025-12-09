def merge_sorted_lists(lists, key=lambda x: x):
    s = []
    n = len(lists)
    sizes = []
    now = []
    i = 0
    sum = 0
    while i < n:
        now.append(0)
        sum += len(lists[i])
        sizes.append(len(lists[i]))
        i += 1
    j = 0
    while j < sum:
        k = -1
        i = 0
        while i < n:
            if(now[i]<sizes[i] and (k == -1 or key(lists[i][now[i]])<key(lists[k][now[k]]))):
                k = i
            i += 1
        s.append(lists[k][now[k]])
        now[k] += 1
        j += 1
    return s

lists = [[1,2],[3,4],[1,4]]
a = merge_sorted_lists(lists, lambda x: 1-x%2)
for i in a:
    print(i)
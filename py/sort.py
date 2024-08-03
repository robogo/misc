# [4, 1, 9, 12, 3, 8]
def my_sorted(a):
    n = len(a) - 1
    for i in range(0, n):
        for j in range(0, n):
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
        n -= 1
    return a

print(my_sorted([4, 1, 9, 12, 3, 1, 8]))

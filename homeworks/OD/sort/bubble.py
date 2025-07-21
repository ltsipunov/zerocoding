def sort(a):
    for n in range(len(a) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if a[i] > a[i + 1]:
               a[i], a[i + 1] = a[i + 1], a[i]
               swapped = True
        if not swapped:  break
    return a

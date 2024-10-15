n, k = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# n, k = 5, 5
# arr1 = [1, 3, 5, 7, 9]
# arr2 = [2, 4, 8, 1, 6]

for el in arr2:
    result = []

    l = -1
    r = len(arr1)
    while r - l > 1:
        m = (r + l) // 2
        if arr1[m] < el:
            l = m
        else:
            r = m
    if l != -1:
        result.append(l)
    else:
        result.append(l + 1)

    l = -1
    r = len(arr1)
    while r - l > 1:
        m = (r + l) // 2
        if arr1[m] <= el:
            l = m
        else:
            r = m

    if r != len(arr1):
        result.append(r)
    else:
        result.append(r - 1)

    if result[-1] - result[0] == 2:
        print(el)
    elif el - arr1[result[0]] <= arr1[result[-1]] - el:
        print(arr1[result[0]])
    else:
        print(arr1[result[-1]])

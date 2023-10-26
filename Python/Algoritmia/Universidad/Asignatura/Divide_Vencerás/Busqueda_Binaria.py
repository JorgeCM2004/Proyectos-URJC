def binary_search(array, i, j, num):
    k = (i + j) // 2
    if i == j:
        return i
    else:
        if array[k] >= num:
            return binary_search(array, i, k, num)
        else:
            return binary_search(array, k + 1, j, num)

arr = [1, 5, 7, 7, 8, 10, 12, 15]
i = 0
j = len(arr) - 1
n = 9
print(binary_search(arr, i, j, n))

def mergesort(l, i, j):
    if i == j:
        return [l[i]]
    else:
        k = (i + j) // 2
        out = []
        l1 = mergesort(l, i, k)
        l2 = mergesort(l, k + 1, j)
        count1 = 0
        count2 = 0
        while len(out) < len(l1) + len(l2):
            if count1 < len(l1) and (count2 >= len(l2) or l1[count1] < l2[count2]):
                out.append(l1[count1])
                count1 += 1
            else:
                out.append(l2[count2])
                count2 += 1
        return out

arr = [10, 12, 15, 11, 5, 7, 37, 8]
i = 0
j = len(arr) - 1
print(mergesort(arr, i, j))

def maxarray(array):
    # return max(array)
    out = int(array[0])
    for i in range(len(array)):
        if out < array[i]:
            out = array[i]
    return out

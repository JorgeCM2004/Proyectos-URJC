def minArrayRotadaAux(l, i, n):
	k = (i + n) // 2
	if (k + 1 > n or l[k] < l[k + 1]) and (k - 1 < i or l[k] < l[k - 1]):
		return l[k]
	else:
		if l[i] > l[k]:
			return minArrayRotadaAux(l, i, k)
		elif l[k] > l[n]:
			return minArrayRotadaAux(l, k + 1, n)
		else:
			return l[i]

def minArrayRotada(l):
	i = 0
	n = len(l) - 1
	return minArrayRotadaAux(l, i, n)

print(minArrayRotada([9, 1, 2, 3, 4, 5, 6, 7, 8]))
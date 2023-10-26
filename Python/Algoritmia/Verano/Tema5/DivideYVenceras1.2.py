def oneSpecial(l):
	i = 0
	n = len(l) - 1
	return oneSpecialAux(l, i, n)

def oneSpecialAux(l, i, n):
	k = (i + n) // 2
	if (k + 1 > n or l[k] != l[k + 1]) and (k - 1 < i or l[k] != l[k - 1]):
		return l[k]
	else:
		if k + 1 <= n and l[k] == l[k + 1]:
			if (k - 1 - i) % 2 == 0: 
				return oneSpecialAux(l, i, k - 1)
			else: 
				return oneSpecialAux(l, k + 2, n)
		else:
			if (k - 2 - i) % 2 == 0: 
				return oneSpecialAux(l, i, k - 2)
			else: 
				return oneSpecialAux(l, k + 1, n)
	
print(oneSpecial([1, 1, 2, 2, 3, 3, 7, 7, 8, 8, 9]))
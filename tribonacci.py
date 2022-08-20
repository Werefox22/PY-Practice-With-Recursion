def trib(n):
	if n <= 2:
		return max((n - 1, 0))
	else:
		return trib(n-1) + trib(n-2) + trib(n-3)

print(trib(7))
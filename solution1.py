# Write code for algorithm 1 below
def count_down(n):
	print(n)
	# base case
	if (n == 0):
		return
	# recursive case
	else:
		count_down(n-1)

count_down(5)
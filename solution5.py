# Write code for algorithm 5 below
def is_palindrome_short(string):
	return string == string[::-1]


def is_palindrome_interation(string):
	for i in range(0, len(string) // 2):
		if string[i] != string[0 - i - 1]:
			return False
	return True

def is_palindrome_recursion(string):
	print(string)
	# base case
	if len(string) <= 2:
		return string[0] == string[-1]
	# recursive case
	else:
		val = is_palindrome_recursion(string[1:-1])
		print(val)
		return val

strings = ["racecar", "madam", "panama", "tacocat", "shrek"]
for i in strings:
	print(f"short: {i} is {('not ', '')[is_palindrome_short(i)]}a palindrome")
	print(f"iteration: {i} is {('not ', '')[is_palindrome_interation(i)]}a palindrome")
	print(f"recursion: {i} is {('not ', '')[is_palindrome_recursion(i)]}a palindrome\n")

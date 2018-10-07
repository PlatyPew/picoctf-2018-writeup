def calc(n):
	if n <= 4:
		x = n * n + 0x2345
	else:
		x = calc(n - 5) * 0x1234 + (calc(n - 1) - calc(n - 2) - calc(n - 3) - calc(n - 3))
	return x


print calc(5)

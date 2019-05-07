def fib(n):
	""" computes the nth term of the fibbonaci sequence """
	if n < 1:
		return -1
	elif n == 1 or n == 2:
		return 1
	else:
		return fib(n-1) + fib(n-2)

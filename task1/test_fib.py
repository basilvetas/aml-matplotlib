from fib import fib

def test_fib():
	""" tests various input values for the fib() function """
	assert fib(0) == -1
	assert fib(1) == 1
	assert fib(2) == 1
	assert fib(3) == 2
	assert fib(4) == 3
	assert fib(5) == 5
	assert fib(6) == 8
	assert fib(7) == 13
	assert fib(8) == 21
	assert fib(9) == 34
	assert fib(10) == 55
	assert fib(11) == 89
	assert fib(12) == 144

if __name__ == '__main__':
	test_fib()
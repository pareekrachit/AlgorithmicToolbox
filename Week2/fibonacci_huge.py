def pisanoPeriod(n):
	a, b = 0, 1
	i = 0

	while(True):
		a, b = b, a+b
		i = i + 1
		if (a%n == 0 and b%n == 1):
			return i

def fibonacci(m):
	if(m <= 1):
		return m
	a, b = 0, 1
	i = 1

	while(i < m):
		a, b = b, a+b
		i = i + 1
	return b


if __name__ == '__main__':
	m, n = map(int, input().split())
	print(fibonacci(m))
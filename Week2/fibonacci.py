def fibonacci(n):
    fib = [0] * n
    fib[1] = 1

    for i in range(2,n):
        fib[i] = fib[i-1] + fib[i-2]
        
    return(fib[n-1])

if __name__ == '__main__':
    n = int(input())
    if (n <= 1):
        print(n)
    else:
        print(fibonacci(n+1))

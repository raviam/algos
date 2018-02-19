def fib(n):
    a,b = 0,1
    while b<n:
        print(b,end=" ")
        a,b = b,a+b
    print()

def fib2(n):
    a,b = 0,1
    fibs = []
    while b<n:
        fibs.append(b)
        a,b=b,a+b
    return fibs
if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))
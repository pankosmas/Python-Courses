# Implementation of fibonacci function with recursive and non-recursive methods.

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])

    return fib[n]


def main():
    for i in range(11):
        print(f"fibonacci({i}) = {fib_iterative(i)}")
        print(f"fibonacci({i}) = {fib_recursive(i)}")


main()

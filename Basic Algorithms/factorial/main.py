# This is a recursive function that calculates the factorial of a given number n.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


def main():
    for i in range(1,11):
        print(f"factorial({i}) = {factorial(i)}")


main()
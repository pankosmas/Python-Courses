# This is a recursive function that implements the well-known Euclidean algorithm of MKD.

def euclid(a, b):
    if a == b:
        return a
    elif a < b:
        return euclid(a, b-a)
    else:
        return euclid(a-b, b)


def main():
    n1 = 255
    n2 = 155
    print(f"MKD of {n1} and {n2} is {euclid(n1, n2)} !")


main()

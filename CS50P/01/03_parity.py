def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")


def is_even(n):
    """as the expression it-self if returning a boolean we can just return the expression it-self"""
    return n % 2 == 0


"""
def is_even(n):
    return True if n % 2 == 0 else False
"""

"""
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
"""

main()

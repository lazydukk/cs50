# Defs
"""
def hello(to):
    print("Hello, ", to)


# output using my own function
name = input("What's your name? ")
hello(name)
"""


def main():
    # output using my function
    name = input("what's your name? ")
    hello(name)

    # output without passing the expected arguments
    hello()


# my own function
# sets the default value to be "world" if no argument is given
def hello(to="world"): 
    print("hello", to)

main()


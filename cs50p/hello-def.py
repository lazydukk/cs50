# defining a main function for better organizing
def main():
    name = input("What's your name? ")
    hello(name)

# to is already pre-assigned to world so if the hello doesnt get called,
# still it will output `hello, world`
# scope
def hello(to="world"):
    print("hello,", to)

# calling the main function
main()
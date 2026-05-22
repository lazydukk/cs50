# Ask the user for their name
# input gets a string from the stdio and stores it in a variable called "name"
name = input("Hello, What's your name? ")

print("Hello, " + name)

# multiple arugments to the print func leads to automatic whitespace addition
print("Hello,", name)

""" Named Parameters """
# in official python documentation we find:
#       print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# so it may receive many parameters and some of them are optional and
# others are the so-called named parameters.
# Those named parameters have a default value e.g., the end default value is
# the '\n' so that the print function adds everytime the '\n' at its end!

print("Hello,", end="")  # no new line
print(name)
print("Hello,", name, sep="_")

# addint quotes to the output
print('hello, "friend"')

# formatting strings
# special string // format string or f-string
print(f"hello, {name}")

# remove whitespaces from the str
# name = name.strip()
# capitalize the first letter of each words
# name = name.title()

name = name.strip().title()
print(f"Hello, {name}")

doggo = input("What's your Dog's name? ").strip().title()
print(f"Your dog's name is, {doggo}")



# defining a variable to input user name
# .strip to remove white space
# .title to capitalize the name as a TITLE
# .split to split the name in two as in first and last
name = input("What's your name?: ").strip().title()
first_name, last_name = name.split(" ")

# f is a fstr 
print(f"howdy, {first_name}")
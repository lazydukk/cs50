# While Loops (3 different methods to implement a while loop)
i = 3
while i != 0:
    print("meow")
    i = i -1

n = 1
while n <= 3:
    print("meow1")
    n += 1

m = 0
while m < 3:
    print("meow2")
    m += 1

# For Loops 
# range is used to define the range rather than manually typing the values
for _ in range(3):      
    print("meow")

# the geek way 😂
print("geekmeow\n" * 3, end="")


# paradigms 
# when to do something again and again expecting something specific 
while True:
    x = int(input("What's x? "))
    if x > 0:
        break

for _ in range (x):
    print("meowparadigms")


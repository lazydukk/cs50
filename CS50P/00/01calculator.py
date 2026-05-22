x = input("What's x? ")  # stdio register this as a string not as an integer
y = input("What's y? ")

# thus this will out put "1" + "2" => "12"
# z = x + y

z = int(x) + int(y)
print(z)

# now, stdio registers the inputs as integers
a = int(input("What's a? "))
b = int(input("What's b? "))
print(a + b)

# nested functions
# print(int(input("What's q?")) + int(input("What's w? ")))

# Floats

s = float(input("What's s? "))
t = float(input("What's t? "))

u = round(s + t)
print(f"{u:,}")

h = round(s / t, 2)  # rounds to the nearest 2 decimal points
print(h)
print(f"{h:.3f}")  # rounds to the nearest 3 decimal points

# type conversion
# str to int
# int is used for whole numbers 
# float is used for deciaml numbers 
x = int(input("value: "))
y = float(input("value: "))

# round function to round the decimals;
# can be used to show an exact amount of decimal points
z = round(x + y ,3)
# devision 
q = x /y 

# formatting the output
print(f"{z:,}")

# formatting: used to display upto 2 (this value can vary) deciaml points
print(f"{z:.2f}")
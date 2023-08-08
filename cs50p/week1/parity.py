def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# uses a function as a boolean expression to pass a value
def is_even(n):
    # modulo operato: to find the remainder
    if n % 2 == 0:
        return True
    else:
        return False

main()

vowels = ["a", "e", "i", "o", "u"]

def main():
    usr_in = input("Input: ").strip()
    print(f"Output: {rmv(usr_in)}")

def rmv(input):
    new_str = ""
    for letter in input:
        if letter.lower() not in vowels:
            new_str += letter
    return new_str

main()


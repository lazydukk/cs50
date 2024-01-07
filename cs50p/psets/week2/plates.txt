ill_char = [".", " ", "!", "?"]

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    validate = ""
    numchk = 0

    if len(s) >= 2 and len(s) <=6:
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:
                if ch not in ill_char:
                    if ch.isnumeric() and numchk == 0 and ch != "0":
                        numchk += 1
                        validate += ch
                    elif ch.isnumeric() and numchk > 0:
                        numchk += 1
                        validate += ch
                    elif ch.isalpha() and numchk < 1:
                        validate += ch
            if validate == s:
                return True
            else:
                return False

main()

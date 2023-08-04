def main():
    usrInp = str(input(""))
    print(convert(usrInp))

def convert(usrText):
    usrText = usrText.replace(":)", "🙂")
    usrText = usrText.replace(":(", "🙁")
    return usrText

main()
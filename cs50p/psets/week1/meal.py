def main():
    time = input("What time is it? ").strip()
    tconv = convert(time)
    if 7 <= tconv <=8:
        print("breakfast time")
    elif 12 <= tconv <= 13:
        print("lunch time")
    elif 18 <= tconv <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    if time.find(" ") != -1:
        t, p = time.split()
        hour, mins = t.split(":")
    else:
        hour, mins = time.split(":")
        p = "not set"
    try:
        hour = int(hour)
        mins = int(mins)
    except ValueError:
        quit("Invalid Format")
    else:
        if p == "p.m.":
            return 12 + hour + mins / 60
        return hour + mins / 60

if __name__ == "__main__":
    main()
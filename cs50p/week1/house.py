# using `match` keyword

name = input("What's your name? ")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Drace":
        print("Slytherin")
    case _:
        print("Who? ")
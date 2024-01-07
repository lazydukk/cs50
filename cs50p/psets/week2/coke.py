def main():
    
    valid = [25, 10, 5]
    amnt_due = 50 
    owed = 0

    while owed < amnt_due:
        print(f"Amount Due: {amnt_due - owed}")
        coin = int(input("Insert Coin: "))
        if coin in valid:
            owed += coin
        else:
            continue
    print(f"Change Owed: {owed - amnt_due}")


main()

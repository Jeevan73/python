print("""
\t press 1 for namakkal
\t press 2 for salem
\t press 3 for trichy
""")
destination=int(input("enter the destination:"))
passengers=int(input("how many passengers:"))
if destination==1:
    totalcost=passengers*50
    amount=int(input(f"give {totalcost}:"))
    if amount > totalcost or amount == totalcost:
        remainingcost=amount-totalcost
        print(remainingcost)
        print(f"""
               \t namakkal
               \t {passengers} ${totalcost}
               \t enjoy the travel
            """)

    else:
        print("oops you dont have enough amount to travel")

# destiation 2 starts here

if destination==2:
    totalcost=passengers*100
    amount=int(input(f"give {totalcost}:"))
    if amount > totalcost or amount == totalcost:
        remainingcost=amount-totalcost
        print(remainingcost)
        print(f"""
               \t salem
               \t {passengers} ${totalcost}
               \t enjoy the travel
            """)

    else:
        print("oops you dont have enough amount to travel")

# destination 3 starts here

if destination==3:
    totalcost=passengers*150
    amount=int(input(f"give {totalcost}:"))
    if amount > totalcost or amount == totalcost:
        remainingcost=amount-totalcost
        print(remainingcost)
        print(f"""
               \t trichy
               \t {passengers} ${totalcost}
               \t enjoy the travel
            """)

    else:
        print("oops you dont have enough amount to travel")

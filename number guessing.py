import random

random_number = random.randint(1, 100)

attempt=0
while True:
    user_number=int(input("enter numbr 1 to 100:"))
    attempt+=1
    if random_number>user_number:
        print("you are too high")
    elif random_number<user_number:
        print("you are too low")
    else:
        print("you won",attempt)

import random
low=int(input("Enter a low number: "))
hight=int(input("Enter a hight number: "))
print(f"You should guess a number between {low} and {hight}.")

random_num=random.randint(low,hight)
# print(random_num)
max_guess=10
num_guess=0

while max_guess > num_guess:

    num=int(input(f"Enter a number to find the random number. You have {max_guess - num_guess} chances to guess the number."))
    num_guess +=1

    if num == random_num:
        print(f"Congrats you find it in your {num_guess} tried.The number was {random_num}.")
        break
    elif num > random_num:
        print("You guess hight. Try again.")
    elif num < random_num :
        print("You guess low.Try again")
    elif num_guess >= max_guess and num != random_num:
        print(f"Sorry you could not find the number.The number was {random_num}.")



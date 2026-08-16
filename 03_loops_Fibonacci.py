#1
user_range= int(input("Enter a number: "))

if user_range== 0:
    print("[0]")
elif user_range == 1:
    print("[1]")
elif user_range > 1:
    num=[0 , 1]
    for i in range(user_range - 2):
       fib_num= num[-1]+num[-2]
       num.append(fib_num)
    print(num)

else:
    print("Please input a positive number.")



#2
user_range= int(input("Enter a number: "))

if user_range > 0:
    num=[0,1]
    for i in range(user_range):
        fib_num= num[-1]+num[-2]
        num.append(fib_num)

    print(num[:user_range])

elif user_range <= 0:
    print("Please input a positive number.")


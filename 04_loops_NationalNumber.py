#2
nums="0123456789"

while True:

    national_number=input("Enter your national number: ")


    digit=True
    for i in national_number:
        if i not in nums:
            digit= False
            break

    if len(national_number) != 10:
        print("Not Valid! Length must be 10 digits.")
        national_number
    elif not digit :
        print("Not Valid! Must contain only numbers.")
    elif len(set(national_number)) ==1:
        print("Not Valid! Cannot be all identical digits.")
    else:
        print("Valid structure!")
        break
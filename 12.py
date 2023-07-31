print("It's the practice of 'for loop'.")
while True :
    a=input("Say Yes or No to continue for loop : ")
    if a=="yes" or a=="Yes" :
        x=["Arts","Commerce","Science",1,2,3]
        for value in x :
            print("It's",value)
    elif a=="no" or a=="No" :
        print("Okay,It's fine")
        break
    else :
        print("It's not the required answer ")
        continue
print("Thank you for using for loop .")

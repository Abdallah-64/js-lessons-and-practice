# while True:
#     number_1= int(input("enter the f number : "))
#     sign = input("rnter the sign: ")
#     number_2= int(input("enter the s number : "))

#     if sign == "+":
#         print( number_1 + number_2)
#     elif sign == "-" :
#         print( number_1 - number_2 )
#     elif sign == "*" :
#         print( number_1 * number_2 )
#     elif sign == "/" :
#         print( number_1 / number_2 )
#     else:
#         print("this number is not defined!")
#     print("thanks hae a nice day!")
#     break

# banking system

def show_balence():
    print(f"my balence amount is ${balence}")

def deposit():
    amount = float(input("enter th amount that u want to deposit:"))
    if amount < balence:
        print("is not deposid this amount pls enter the posible amount!")
        return 0
    else:
        print(f"you deposit amount is {amount} and the real balence is {balence} ")
        return amount

def withdrow():
    amount = float(input("enter the amount that want to withdrow: "))

    if balence < amount:
        print("unfacient amount")
        return 0
    elif amount < 0 :
        print("is it withdoral")
    else:
        print("done")



balence = 0
menu = True

while menu:
    print("\n== welcome in our banking ==\n")

    print("1. show balence ")
    print("2. deposit ")
    print("3. withdrow ")
    print("4. exit")

    chioce = input("enter the num (1-4) : ")

    if chioce == 1 :

        show_balence ()

    elif chioce == 2 :

        balence += deposit ()

    elif chioce == 3 :

        balence -= withdrow ()

    elif chioce == 4 :

        menu = False

        print ("thanks have a nice day!")
        break
    
    # else:
    #     print("is not defined!")
    #     break


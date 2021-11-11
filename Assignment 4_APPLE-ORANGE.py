print(f"\nWelcome valued customer!\nOur apples are on sale at 20 pesos each, while our oranges are 25 pesos each.\n")

def getFruits():
    global appleAmount
    global orangeAmount
    appleAmount = int(input("How many apples do you want to purchase? \n= "))
    orangeAmount = int(input("\nHow many oranges do you want to purchase? \n= "))
    return appleAmount, orangeAmount

def totalPrice():
    applePrice = 20
    orangePrice = 25
    apple = applePrice*appleAmount
    orange = orangePrice*orangeAmount
    totalAmount = (apple+orange)
    return totalAmount

def display(totalF):
    print(f"\nThe total amount of your purchase is {totalF} pesos.\n")

getFruits()
total = totalPrice()
display(total)
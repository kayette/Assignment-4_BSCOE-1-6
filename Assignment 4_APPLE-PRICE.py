def get_MoneyPrice():
    global myMoney
    global applePrice
    myMoney=float(input("\nEnter the amount of money you have: \n= "))
    applePrice=float(input("\nEnter your desired price for one apple: \n= "))
    return myMoney, applePrice

def getAll(myMoneyF, applePriceF):
    global maxApple
    global changeTotal
    global neededAmount
    maxApple=int(myMoneyF/applePriceF)
    totalPrice=float(maxApple*applePriceF)
    changeTotal=float(myMoneyF-totalPrice)
    neededAmount=float(applePriceF-myMoneyF)
    return maxApple, changeTotal, neededAmount

def finalTotal(maxAppleF, changeTotalF, neededAmountF):
    if (maxAppleF > 1) and (changeTotalF > 1):
        return print(f"\nYou can buy {maxAppleF} apples and your change is {changeTotalF:,.2f} pesos.\n")
    elif (maxAppleF> 1) and (changeTotalF == 1):
        return print(f"\nYou can buy {maxAppleF} apples and your change is {changeTotalF:,.2f} peso.\n")
    elif (maxAppleF == 1) and (changeTotalF > 1):
        return print(f"\nYou can buy {maxAppleF} apple and your change is {changeTotalF:,.2f} pesos.\n")
    elif (maxAppleF == 1) and (changeTotalF == 1):
        return print(f"\nYou can buy {maxAppleF} apple and your change is {changeTotalF:,.2f} peso.\n")
    elif (maxAppleF > 1) and (changeTotalF == 0):
        return print(f"\nYou can buy {maxAppleF} apples and you have no more change.\n")
    elif (maxAppleF == 1) and (changeTotalF == 0):
        return print(f"\nYou can buy {maxAppleF} apple and you have no more change.\n")
    else:
        return print(f"\nYou cannot buy any apples. You need {neededAmountF:,.2f} more peso to complete a purchase.\n")

get_MoneyPrice()
money=myMoney
apple=applePrice
getAll(money, apple)
finalTotal(maxApple, changeTotal, neededAmount)
#Stock portfolio problem

#Function to find the total price the stock owner paid
def total_Price(Portfolio):
    Total = []
    for i in Portfolio:
        shares = i[2]
        purchPrice = i[1]
        Total += [shares * purchPrice]
    return Total
#the total price of the current value of the stocks
def total_currentPrice(Portfolio):
    currentTotal = 0
    for i in Portfolio:
        currentTotal += i[4]
    return currentTotal
#how many stocks won or lost
def Total_winOrloss(Portfolio):
    Win = 0
    Loss = 0
    for i in Portfolio:
        Total = (i[1] * i[2]) - (i[2] * i[4])
        if Total < 0:
            Loss += 1
        else:
            Win += 1
    print("You have won on", Win,"Stocks and lost on", Loss,"Stocks.")
#how much was won or how much was lost
def Winnings(Portfolio):
    Winnings = 0
    for i in Portfolio:
        purchDate = i[0]
        purchPrice = i[1]
        shares = i[2]
        symbol = i[3]
        currentPrice = i[4]
        Winnings += (purchPrice - currentPrice) * shares
    return Winnings

#Display the portfolio in a tuple showing
#purchase date, purchase price, shares, symbol, Current price
stockPort = [('2010-Feb-03', 35.43, 50, 'EVM', 40.32),
             ('2010-Mar-01', 85.97, 10, 'SSJ', 82.24),
             ('2010-Mar-23', 40.38, 25, 'JIY', 50.39),
             ('2010-Jun-15', 75.43, 20, 'LIB', 78.98),
             ('2010-Aug-28', 50.86, 25, 'TYY', 49.68)]

print("Your Total cost was", total_Price(stockPort))
print("The total current price of the stocks are", total_currentPrice(stockPort))
Total_winOrloss(stockPort)
print("Your total winnings is", Winnings(stockPort))

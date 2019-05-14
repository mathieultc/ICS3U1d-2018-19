print("{0:>10} {01:>10}".format("Price","You Pay"))
print("{0:25}".format("--------------------------"))

#compute the discount and output the table
for price in range(10,151,10):
    if price < 20:
        cost = price-(price*0.1)
    elif price >= 20 and price < 50:
        cost = price-(price*0.2)
    elif price >= 50 and price < 100:
        cost = price-(price*0.3)
    else:
        cost = price-(price*0.4)

    print("{0:10.2f} {1:10.2f}".format(price,cost))


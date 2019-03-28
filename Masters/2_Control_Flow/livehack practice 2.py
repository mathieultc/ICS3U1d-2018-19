#get the mark and the earnings
mark = float(input("Enter your average here: "))
earnings_before_summer = float(input("Enter your earnings here to see your fate: "))

#compute whether he will go to vacation or not
if mark >= 80 and earnings_before_summer >= 500:
    print("You can go to Europe")
elif mark >= 80:
    print("you can go to california")
else:
    print("you cannot go")
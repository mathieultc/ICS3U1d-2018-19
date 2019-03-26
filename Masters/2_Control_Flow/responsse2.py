you = int(input("Please enter your stylishness of your clothes here: "))
date = int(input("Please enter the stylishness of your date clothes here: "))

if you > 8 or date > 8:
    print(2)
if you < 2 or date < 2 :
    print(0)
else :
    print(1)
#get the values for the triangle
num_1 = float(input("Please enter the value of a length here: "))
num_2 = float(input("please enter the a second value: "))
num_3 = float(input("Please enter a third value here: "))

#square the values
a = num_1**2
b = num_2**2
c = num_3**2

#compute if it is a right-angled triangle or not
if ((a+b)==c) or ((a+c)==b) or ((b+c)==a) :
    print("The triangle is right angled")
else:
    print("The triangle is not right angled")
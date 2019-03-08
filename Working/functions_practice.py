import math

def volume(r,h):
    return math.pi * (r**2 * h)

radius = int(input("Enter the radius of the cylinder here: "))
height = int(input("Enter the height of the cylinder here: "))

def main():
    print("The volume of the cylinder is", volume(radius,height))

main()

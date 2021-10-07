

#1

#1 1) Takes in input
#2) Stores user input into a dictionary or list
#3) The User can add or delete items
#4) The User can see current shopping list
#5) The program Loops until user 'quits'
#6) Upon quiting the program, print out all items in the user's list


my_items=[]
while True:
    
        response = input("What do you want to do with your shopping cart add or remove or quit? ")
   
        if response == 'quit' :
            break      #loop is over

        elif response == 'add':
            item=input("What do you want to add to your shopping cart? ").strip()
            my_items.append(item)


        elif response == 'remove':
            item=input("what do you want to remove? ").strip()
            my_items.remove(item)
        print("your shopping cart items: ",my_items)















#2) Has a function to calculate the square footage of a house
#Reminder of Formula: Length X Width == Area

import my_mod
length = int(input("What is the length of the House in feet? "))
width = int(input("What is the width of the House in feet? "))
result = length * width


print("You entered dimensions of " + str(length) + str(" feet by ") + str(width) +str(" feet."))
print("The area is " + str(result) + " square feet.")

#3 Has a function to calculate the circumference of a circle

import my_mod
import math
r = int(input(' Please Enter the radius of a circle: '))

circumference = 2 * math.pi * r
print(" Circumference Of a Circle = %.2f" %circumference)


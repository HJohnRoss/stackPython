num1 = 42  # this is a int
num2 = 2.3  # this is a float
boolean = True  # boolean = true or false
string = 'Hello World'  # var of string with "Hello World"
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos',
                  'Cheese', 'Olives']  # List and or array
person = {'name': 'John', 'location': 'Salt Lake',  # Dictionary
          'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')  # tuple ?
print(type(fruit))  # variable
print(pizza_toppings[1])  # prints string of Sausage
pizza_toppings.append('Mushrooms')  # .append() = .push() in javascript
# goes to the dictionary of person and output is = John (my name lel)
print(person['name'])
# goes to the dictionary of person and sets the output of "name" = "George"
person['name'] = 'George'
# goes to the dictionary of person and sets the output of "eye_color" = "blue"
person['eye_color'] = 'blue'
print(fruit[2])  # prints from the tuple of fruit "banana"

if num1 > 45:  # if statement
    print("It's greater")
else:  # else statement
    print("It's lower")

if len(string) < 5: # len() = string.length
    print("It's a short word!")
elif len(string) > 15: # else if
    print("It's a long word!")
else: # else uses ":" now instead of {}
    print("Just right!")

for x in range(5): # x will print 0, 1, 2, 3, 4
    print(x)
for x in range(2, 5): # x will print 2, 3, 4
    print(x)
for x in range(2, 10, 3): # x will print 2, 5, 8
    print(x)
x = 0
while (x < 5): # will pring 0, 1, 2, 3, 4
    print(x)
    x += 1

pizza_toppings.pop() # takes off the "Olives" (stores it within pop() so you can set a variable = pizza_toppings.pop())
pizza_toppings.pop(1) # take out sausage out of pizza_toppings

print(person) # prints var of person
person.pop('eye_color') # pops the string of eye_color from the var of person
print(person)

for topping in pizza_toppings: # will run as long as theres var topping in pizza_toppings
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break


def print_hello_ten_times(): 
    for num in range(10):
        print('Hello')


print_hello_ten_times() # calling the function + printing "Hello" 10 times


def print_hello_x_times(x):  
    for num in range(x):
        print('Hello')


print_hello_x_times(4) # setting paramater of x = 4, "Hello" will pring 4 times


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times() # prints "Hello" 10 times
print_hello_x_or_ten_times(4) # prints "Hello" 4 times


"""
Bonus section
"""

# print(num3) no var num3 so error?
# num3 = 72 sets num3 = 72
# fruit[0] = 'cranberry' error? because you cant change or manipulate a tuple
# print(person['favorite_team']) error doesnt exist in the dictionary
# print(pizza_toppings[7])  prints if it exsists (not sure if it does wasnt really keeping track of the index's)
#   print(boolean)
# fruit.append('raspberry') add rasberry to pop
# fruit.pop(1) removes the index of 1 of fruit

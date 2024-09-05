# loops and functions
# 1. Loops.
# for loops
import math

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

# for loop that will square and print all values between 1 and 10

for i in range(10):
    i = i**2
    print("The square of i is:", i)


# for loop neste in for loop to manipulate list within list

myMatrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in myMatrix:
    for j in i:
        print(i,j)

for i in range(3):
    for j in range(3):
        print(f"({i}, {j}), {myMatrix[i][j]**2}")


'''functions are more useful to build a reusable codes'''
# function to return the product of two numbers

def product(a, b):
    pro = a*b
    return pro
a = 2
b = 5
myPro = product(a,b)
print(f"the product of{a} and {b}, is, {myPro}")
'''write a function to calculate the are of circle with given value of r. '''

def area_circle(r):
    area = 3.14 * int(r**2)
    return area
r = 8
area = area_circle(r)
print(f"the area of circle of radius {r} is {area}")

# function to calculate the factorial of number
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n-1)


# create a loop that add 4 and multiply all numbers by 2 and save the new values in list myLoop2
myLoop2 = []
while i < 20:
    for i in range(1, 21):
        myLoop2.append((i+4) * 2)
        print(myLoop2)

# create a  function that return the square root on number n
def square_root(n):
    sqroot = math.sqrt(n)
    return sqroot
print(square_root( 6))


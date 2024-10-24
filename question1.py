# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).

#formular: distance ((x2-x1))
import math


def calculate_distance(a1, b1, a2, b2):
    distance = math.sqrt((a2 - a1)*2 + (b2 - b1)*2)
    return distance

#for the distance
a1, b1 = map(float, input("Enter coordinates of point 1 (a1 b1): ").split())
a2, b2 = map(float, input("Enter coordinates of point 2 (a2 b2): ").split())
distance = calculate_distance(a1, b1, a2, b2)
print(f"The distance between the points is: {distance}")






# Question 1(ii)
# Write a Python program to find maximum between three numbers.

def maximum_between_three_numbers(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

#calling the function
maximum = maximum_between_three_numbers(num1, num2, num3)
print(f"The maximum number among {num1}, {num2}, and {num3} is {maximum}.")



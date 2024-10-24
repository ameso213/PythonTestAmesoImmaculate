# Question 3(i)
#  Write a Python program that prompts a user to enter numbers. The process will repeat until
#  the user enters 0. Finally, the program prints sum of the numbers entered by the user.
def sum_numbers():
    total = 0
    #on entering 0, the program stops
    while True:
        number = int(input("Enter a number (0 to stop): "))
    
        if number == 0:
            break
        total += number
    print("Sum of the numbers entered:", total)

sum_numbers()










# Question 3(ii)
# Write a Python program to print all the numbers from 1 to 100 that are not divisible by 2

def numbers_non_divisible_by_2():
    for number in range(1, 101):
        if number % 2 != 0:
            print(number)
            
#calling the function
numbers_non_divisible_by_2()


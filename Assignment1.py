


# #List is given below:
# numbers = [12, 75, 150, 180, 145, 525, 50]
# Write a program to display only those numbers from a list that satisfy the following
# conditions
# i. The number must be divisible by five
# ii. If the number is greater than 150, then skip it and move to the next number
# iii. If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number % 5 == 0:
    
        if number > 150:
            continue
        
        if number > 500:
            break
        
        print(number)

#  Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers. The next number is found by adding
# up the two numbers before it. The first two numbers are 0 and 1.


def generate_fibonacci(n):
    fibonacci_series = [0, 1]
    
    for _ in range(2, n):
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)
    
    return fibonacci_series

n_terms = 10
fibonacci_series = generate_fibonacci(n_terms)

print(f"Fibonacci series up to {n_terms} terms:")
print(fibonacci_series)


# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number
#down to 1.

def calculate_factorial(number):
    factorial = 1
    
    
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    
    for i in range(1, number + 1):
        factorial *= i
    
    return factorial

num = int(input("Enter a number to find its factorial: "))

result = calculate_factorial(num)

if result is not None:
    print(f"The factorial of {num} is {result}.")


# Write a program to iterate a given list and count the occurrence of each element and
# print to show the count of each element.
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

element_count = {}

for element in sample_list:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

print("Count of each element:")
for element, count in element_count.items():
    print(f"{element}: {count} times")

# Given two lists, l1 and l2, write a program to create a third list l3 by picking an
# odd-index element from the list l1 and even index elements from the list l2.
# Given:
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

for i in range(1, len(l1), 2):
    l3.append(l1[i])

for i in range(0, len(l2), 2):
    l3.append(l2[i])

print("List l3 created by picking odd-index elements from l1 and even-index elements from l2:")
print(l3)

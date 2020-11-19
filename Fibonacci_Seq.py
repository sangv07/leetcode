
list_num = int(input("Please Enter Number: "))
num1 = 0
num2 = 1
count = 0
l_num = []

while count <= list_num:
    if count <= 1:
        l_num.append(count)
        count += 1
    else:
        sum1 = num1 + num2
        num1 = num2
        num2 = sum1
        count += 1
        l_num.append(sum1)

print(l_num)

'''
"""Python Program to Write Fibonacci Sequence Using Recursion
Recursion is the basic Python programming technique in which a function calls itself directly or indirectly. 
The corresponding function is called a recursive function. Using a recursive algorithm, certain problems can be solved quite easily. 
Let’s see how to use recursion to print first ‘n’ numbers of the Fibonacci Series in Python.
"""

def FibRecursion(n):
    if n <= 1:
        return n
    else:
        return (FibRecursion(n - 1) + FibRecursion(n - 2))


nterms = int(input("Enter the terms? "))  # take input from the user
l_num = []
if nterms <= 0:  # check if the number is valid
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(i)
        l_num.append(FibRecursion(i))

print(l_num)

"""Explanation: In the above Python program, we use recursion to generate the Fibonacci sequence. 
The function FibRecursion is called recursively until we get the output. In the function, we first check if the number n is zero or one. 
If yes, we return the value of n. If not, we recursively call fibonacci with the values n-1 and n-2.
"""

'''

dr
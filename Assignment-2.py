#1.What are the two values of the Boolean data type? How do you write them?
"""
The two values are True and False
a = True
b = False

"""
#2. What are the three different types of Boolean operators?
"""
The three different types of boolean operators:
AND, OR and NOT 
"""
#3. Make a list of each Boolean operators truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
"""

AND:
A B Out
0 0  0
0 1  0
1 0  0
1 1  1


OR:
A B Out
0 0  0
0 1  1
1 0  1
1 1  1


NOT:
A  Out
0   1
1   0

"""

#4. What are the values of the following expressions?
"""
    (5 > 4) and (3 == 5) : False
    not (5 > 4) : False
    (5 > 4) or (3 == 5) : True
    not ((5 > 4) or (3 == 5)) : False
    (True and True) and (True == False) : False
    (not False) or (not True) : True
"""
#5. What are the six comparison operators?

"""
1. == 
2. !=
3. >
4. <
5. >=
6. <=

"""

# 6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.
"""
Assignment operator:
This operator assigns a value to the variable
Ex: a=1

Equal to:
This operator compares 2 values.
a =8
b =9
if (a == b):
    return True
"""

#7. Identify the three blocks in this code:
"""
spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')

"""

#8.Write code that prints Hello if 1 is stored in spam,# prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

"""
spam = int(input("Enter the value:"))
if spam == 1:
    print("Hello")
if spam == 2:
    print("Howdy")
else:
    print("Greetings!!")
"""

#9.If your programme is stuck in an endless loop, what keys you’ll press?

"""Ctrl + C"""

#10. How can you tell the difference between break and continue?

"""break : This keyword is used when you want to stop the loop at a particular condition"""
"""
a = input("Enter a:")
b = 22
while a > b:
    if a == 10:
        break
"""


#11.In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10
"""
There is no difference in the output of any three of them
range(10) :  The loop prints 0 to 9( takes initial value as o by default)
range(0,10) : The loop prints from 0 to 9
range(0,10,1) : The loop prints 0 to 9 with the interval/jump of 1 which provides the same output
"""

#12.Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

"""
For loop:

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i = i+1

"""

#13.If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
"""
import spam
spam.bacon()
"""
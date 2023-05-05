"""
https://www.w3resource.com/python-exercises/collections/index.php

. Write a Python program to create a deque and append few elements to the left and right, then remove some elements from the left, right sides and reverse the deque. Go to the editor
Sample Output:
deque(['Red', 'Green', 'White'])
Adding to the left:
deque(['Pink', 'Red', 'Green', 'White'])
Adding to the right:
deque(['Pink', 'Red', 'Green', 'White', 'Orange'])
Removing from the right:
deque(['Pink', 'Red', 'Green', 'White'])
Removing from the left:
deque(['Red', 'Green', 'White'])
Reversing the deque:
deque(['White', 'Green', 'Red'])
"""
from collections import deque
first_deque= deque()
first_deque.appendleft('Pink')
first_deque.appendleft('Red')
first_deque.appendleft('Green')
first_deque.appendleft('White')
first_deque.append('Orange')
print(first_deque)
first_deque.pop()
print(first_deque)
first_deque.pop()
print(first_deque)
first_deque.reverse()
#print(first_deque)
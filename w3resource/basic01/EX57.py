# 57. Write a Python program to get execution time for a Python method.

import time
import random

start = time.time()

lowerCase = 'abcdefghijklmnopqrstuvwxyz'
upperCase= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number= '0123456789'
symbols='@#$%&*/\?'

UseFor= lowerCase + upperCase + number + symbols
lenghtForPass= 10

password=''.join(random.sample(UseFor, lenghtForPass ))

print("Your Generated Password is: ",password)

end = time.time()
print(end-start)

# Alternative Soln

import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 5
print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

# Alternative soln 2
import timeit
def sum():
    for i in range(1, 10000000):
        i += i
    return i
print(timeit.repeat(lambda: sum(), repeat=3, number=1)) # get a list of exec time (size is set with repeat)
print(timeit.timeit(lambda: sum(), number=1))

# Alternative soln 3
# Using decorators:
import time

def timer(fn):
    def decorator(*args, **kwargs):
        start = time.time();
        fn(*args, **kwargs)
        end = time.time()
        print("Total: {0:.2f} ms".format(end - start))
        return decorator

class MyClass:
    def __init__(self, data):
        self.data = dat
        @timer
        
    def method(self): # in a class definition should the method be on the same level as the init or under?
            print(self.data)
            for i in range(0, 10000000):
                pass

my_instance = MyClass('mydata')

my_instance.method()
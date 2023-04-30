# def spam():
# 	eggs = 99
# 	bacon()
# 	print(eggs)

# def bacon():
# 	ham = 101
# 	eggs = 0

# spam()
# bacon()

# readglobal.py
# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)

# localGlobalSameName.py
# def spam():
#     eggs = 'spam local'
#     print(eggs)    # prints 'spam local'

# def bacon():
#     eggs = 'bacon local'
#     print(eggs)    # prints 'bacon local'
#     spam()
#     print(eggs)    # prints 'bacon local'

# eggs = 'global'
# bacon()
# print(eggs)        # prints 'global'

# globalStatement.py
# def spam():
#     global eggs
#     eggs = 'spam'

# eggs = 'global'
# spam()
# print(eggs)

# sameNameLocalGlobal.py
# def spam():
#     eggs = 'spam' # this is the global
# def bacon():
#     eggs = 'bacon' # this is a local
# def ham():
#     print(eggs) # this is the global
# eggs = 42 # this is the global
# spam()
# print(eggs)

# sameNameError.py
# def spam():
#     print(eggs)# ERROR!
#     eggs = 'spam local'
# eggs = 'global'
# spam()

# zeroDivide.py
# def spam(divideBy):
#     return 42 / divideBy

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# tryexceptzerodivide.py
# def spam(divideBy):
#     try:
#         return 42/ divideBy

#     except ZeroDivisionError:
#         print('Error: Invalid argument.')

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

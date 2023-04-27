# 68. Write a Python program to calculate sum of digits of a number.
user_input = input("Enter a number with more than 1 digit eg 234: ")
sepa_input = []
for char in user_input:
    sepa_input.append(char)
print(sepa_input)

num_list = []
for num in sepa_input:
    num_list.append(int(num))
print(num_list)
total_char_sum = sum(num_list)
print(total_char_sum)


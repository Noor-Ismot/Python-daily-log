#Problem Solving: Loops (10 Problems)
#Date: 20 December 2025
#Learned how to use loops effectively to solve various problems, including counting, summing, generating multiplication tables, reversing numbers, checking for palindromes, and calculating factorials. I also learned how to handle negative numbers and leading zeros in string manipulations.

#My Solution: Problem 1 ------------------------------------------

user_input = int(input("Enter the number:"))
i = 1
while i<= user_input:
    print(i)
    i +=1


#My Solution: Problem 2 ------------------------------------------

user_input = int(input("Enter the number:"))
i = 1
while i<= user_input:
    if(i%2 == 0):
            print(i)
    i +=1


#My Solution: Problem 3 ------------------------------------------

user_input = int(input("Enter the number:"))
i = 1
total = 0
while i<= user_input:
    total = total + i
    i +=1
print(total)



#My Solution: Problem 4 ------------------------------------------

user_input = int(input("Enter the number:"))
for i in range(1,11):
    print(f"{user_input} x {i} = {user_input * i}")


#My Solution: Problem 5 ------------------------------------------ 

user_input = input("Enter the number:")
count_digit = 0

for i in range(0, len(user_input)):
    
    if user_input[i] == '-':
        continue
    else:
        count_digit += 1
print(count_digit)

#Suggested solution by chatGPT
user_input = input("Enter the number: ")
count_digits = 0

for ch in user_input:
    if ch.isdigit():
        count_digits += 1

print(count_digits)



#My Solution: Problem 6 : ------------------------------------------

def find_reverse_number(output_text, end_point, txt):
    i = len(txt) - 1
    while i >= end_point :
        output_text = output_text + (txt[i])
        i -=1
    return output_text.lstrip('0')

user_input = input("Enter the number:")


if user_input[0] == '-':
    print(find_reverse_number('-', 1, user_input))
else:
    print(find_reverse_number('', 0, user_input))


#Suggested Solution by chatGPT:

def reverse_number(num_str):
    is_negative = num_str[0] == '-'
    
    digits = num_str[1:] if is_negative else num_str
    reversed_digits = digits[::-1].lstrip('0')
    
    return '-' + reversed_digits if is_negative else reversed_digits


user_input = input("Enter the number: ")
print(reverse_number(user_input))



#My Solution: Problem 7 : ------------------------------------------

def reverse_number(txt):
    output_text = ""
    i = len(txt) - 1
    while i >= 0 :
        output_text = output_text + (txt[i])
        i -=1
    return output_text.lstrip('0')

user_input = input("Enter the number:")

if user_input[0] == '-' or user_input != reverse_number(user_input):
    print("Not Palindrome")
else:
    print("Palindrome")


#Suggested Solution by chatGPT

def is_palindrome(num_str):
    if num_str[0] == '-':
        return False
    
    return num_str == num_str[::-1]


user_input = input("Enter the number: ")

if is_palindrome(user_input):
    print("Palindrome")
else:
    print("Not Palindrome")



#My Solution: Problem 8: ------------------------------------------
user_input = input("Enter the number:")
fac_num = 1
for i in range(1,int(user_input)+1):
    fac_num = fac_num * i
print(fac_num)



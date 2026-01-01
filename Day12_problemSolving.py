#Problem Solving: Loops (10 Problems)
#Date: 19-20 December 2025
#Focused on how to use loops effectively to solve various problems, including counting, summing, generating multiplication tables, reversing numbers, checking for palindromes, and calculating factorials. I also learned how to handle negative numbers and leading zeros in string manipulations.
"""
P1. Goal: Print numbers from 1 to N.<br> 
Input: integer N<br>
Output: numbers from 1 to N (one per line)<br>
Constraints: N ≥ 1<br>

Test cases:<br>
5 → 1 2 3 4 5<br>
1 → 1<br>
3 → 1 2 3<br>

P2. Goal: Print all even numbers between 1 and N.<br>
Input: integer N<br>
Output: even numbers ≤ N<br>
Constraints:N ≥ 2<br>

Test cases:<br>
10 → 2 4 6 8 10<br>
5 → 2 4<br>
2 → 2

P3. Goal: Calculate the sum of numbers from 1 to N.<br>
Input: integer N<br>
Output: integer sum<br>
Constraints:N ≥ 1

Test cases:<br>
5 → 15<br>
1 → 1<br>
10 → 55


P4. Goal: Print multiplication table of a number up to 10.<br>
Input: integer N<br>
Output: N x i = result for i = 1..10<br>
Constraints: N between 1 and 20

Test cases:<br>
3 → 3 x 1 = 3 ... 3 x 10 = 30<br>
5 → ...

P5. Goal: Count digits in a number.<br>
Input: integer<br>
Output: number of digits<br>
Constraints: Negative numbers allowed

Test cases:<br>
123 → 3<br>
0 → 1<br>
-4567 → 4

P6. Goal: Reverse a number.<br>
Input: integer<br>
Output: reversed integer<br>
Constraints: No string conversion

Test cases:<br>
123 → 321<br>
100 → 1<br>
-456 → -654<br>

P7. Goal: Check if a number is a palindrome.<br>
Input: integer<br>
Output: "Palindrome" or "Not Palindrome"<br>
Constraints:No string usage

Test cases:<br>
121 → Palindrome<br>
123 → Not Palindrome<br>
0 → Palindrome

P8. Goal: Find factorial of a number.<br>
Input: integer N<br>
Output: factorial value<br>
Constraints:N ≥ 0

Test cases:<br>
5 → 120<br>
0 → 1<br>
3 → 6

P9. Goal: Print Fibonacci sequence up to N terms.
Input: integer N<br>
Output: first N Fibonacci numbers<br>
Constraints:N ≥ 1<br>

Test cases:<br>
5 → 0 1 1 2 3<br>
1 → 0<br>
2 → 0 1

P10. Goal: Find sum of digits of a number.
Input: integer<br>
Output: sum of digits<br>
Constraints:No string conversion<br>

Test cases:<br>
123 → 6<br>
0 → 0<br>
-456 → 15

"""

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



#My Solution: Problem 9: ------------------------------------------
n = int(input("Enter the number of terms: "))

if n <= 0:
    print([])
elif n == 1:
    print([0])
else:
    fib = [0, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    print(fib)



#My Solution: Problem 10: ------------------------------------------
num = int(input("Enter the number: "))
num = abs(num)

digit_sum = 0

while num > 0:
    print(num)
    digit_sum += num % 10
    num //= 10
    print(num)

print(digit_sum)


    




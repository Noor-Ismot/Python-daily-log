#Problem Solving: Lists
#Date: 26 - 27 December 2025
"""
1. Goal: Create a list and print its elements.

Inputs / Outputs:

Input: list of integers

Output: each element on a new line

Constraints:

At least one element

Test cases:

[1, 2, 3] → 1 2 3

[5] → 5

[0, -1] → 0 -1
"""

#my solution : 1 ----------------------------------

user_input = input("Enter your list of integers:").split()
for i in user_input:
    print(i)


"""
2. Goal: Find the sum of all elements in a list.

Inputs / Outputs:

Input: list of integers

Output: integer sum

Constraints:

No built-in sum()

Test cases:

[1, 2, 3] → 6

[5] → 5

[0, -1, 1] → 0
"""

#my solution : 2 ----------------------------------

user_input = input("Enter your list of integers:").split()
sum = 0

for i in user_input:
    sum += int(i)

print(sum)



"""
3. Goal: Find the largest element in a list.

Inputs / Outputs:

Input: list of integers

Output: largest value

Constraints:

No built-in max()

Test cases:

[1, 5, 3] → 5

[-1, -5, -3] → -1

[7] → 7
"""

#my solution : 3 ----------------------------------

user_input = input("Enter your list of integers:").split()

largest_val = int(user_input[0])

for i in range(1,len(user_input)):
    if int(user_input[i]) > largest_val:
        largest_val = int(user_input[i])

print(largest_val)



"""
4. Goal: Reverse a list.

Inputs / Outputs:

Input: list

Output: reversed list

Constraints:

Do not use slicing or .reverse()

Test cases:

[1, 2, 3] → [3, 2, 1]

[] → []

[5] → [5]
"""


#my solution : 4 ----------------------------------

user_input = input("Enter your list of integers:").split()
list_len = len(user_input)
reversed_list = []

i = list_len - 1
while i>=0:
    reversed_list.append(user_input[i])
    i-= 1

print(reversed_list)


"""
5. Goal: Remove duplicates from a list.

Inputs / Outputs:

Input: list

Output: list without duplicates (preserve order)

Constraints:

Do not use set() directly

Test cases:

[1, 2, 2, 3] → [1, 2, 3]

[5, 5, 5] → [5]

[] → []

"""

#my solution : 5 ----------------------------------
user_input = input("Enter your list of integers:").split()
list_len = len(user_input)
new_list = []

i = 0
while i< list_len:
    if user_input[i] not in new_list:
        new_list.append(user_input[i])
    i+= 1

print(new_list)



"""
6. Goal: Count occurrences of a target element.

Inputs / Outputs:

Input: list, target

Output: integer count

Constraints:

No .count()

Test cases:

[1, 2, 2, 3], 2 → 2

[5, 5, 5], 5 → 3

[1, 2], 3 → 0
"""

#my solution : 6 ----------------------------------
user_input = input("Enter your list of integers:").split()
target_input = input("Enter the target integer:")
count_target = 0

for i in user_input:
    if i == target_input:
        count_target +=1

print(count_target)

"""
7. Goal: Separate even and odd numbers.

Inputs / Outputs:

Input: list of integers

Output: two lists → evens, odds

Constraints:

Maintain original order

Test cases:

[1, 2, 3, 4] → [2, 4], [1, 3]

[2, 4] → [2, 4], []

[] → [], []
"""


#my solution : 7 ----------------------------------------
user_input = input("Enter your list of integers:").split()
odd_list = []
even_list = []

for i in user_input:
    if int(i) % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list, odd_list)


"""

8. Goal: Find the second largest number.

Inputs / Outputs:

Input: list of integers

Output: second largest integer

Constraints:

List length ≥ 2

No sorting

Test cases:

[1, 3, 2] → 2

[5, 5, 3] → 5

[-1, -2, -3] → -2

"""

#my solution : 8 ---------------------------------------
user_input = input("Enter your list of integers:").split()
numbers = []
for i in user_input:
    numbers.append(int(i))

if numbers[0] > numbers[1]:
    largest_val = int(user_input[0])
    second_largest = numbers[1]
else:
    largest_val = numbers[1]
    second_largest = numbers[0]

if len(user_input)> 2:
    for i in range(2,len(user_input)):
        if int(numbers[i]) > largest_val:
            second_largest = largest_val
            largest_val = numbers[i]
        else:
            if second_largest < numbers[i] <= largest_val:
                second_largest = numbers[i]

print(second_largest)


"""

9. Goal: Rotate list to the right by K steps.

Inputs / Outputs:

Input: list, integer K

Output: rotated list

Constraints:

K ≥ 0

K may be larger than list length

Test cases:

[1, 2, 3, 4], 1 → [4, 1, 2, 3]

[1, 2, 3], 4 → [3, 1, 2]

[], 3 → []

"""

#my solution : 9 : To be Completed ----------------------------------
user_input = input("Enter your list of integers:").split()

k_val = int(input("Inter step value:"))
len_list = len(user_input)
new_list = []


step = abs(len_list - k_val)
i = len_list
while i >=0:
        for i in range(len_list): 
            new_list.insert(i,user_input[i-k_val])
            i -=1
        print(new_list)

"""


10. Goal: Check if list is sorted in ascending order.

Inputs / Outputs:

Input: list of integers

Output: True or False

Constraints:

Allow equal elements

Test cases:

[1, 2, 3] → True

[1, 3, 2] → False

[2, 2, 2] → True
"""


#my solution : 10 ----------------------------------
user_input = input("Enter your list of integers:").split()
new_list = user_input.copy()
new_list.sort()
print(user_input == new_list)








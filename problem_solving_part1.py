"""
#Challenge #1 — Basic Input, Processing, and Output

#My solution:
name = input("name:")
age = int(input("age:")) + 1
print("Hello, " + name + "! Next year you will be "+ str(age) +" years old.")

#---------------------------------------------------------

#Challenge #2 — Even or Odd Checker
#My solution:

num = int(input())
print(f"{num} is even") if num%2 == 0 else print(f"{num} is odd")

#---------------------------------------------------------

#Challenge #3 — List Filter: Only Positive Numbers
#MySolution:
pos_num_list =[]
for i in range(5):
    num = int(input())
    if num > 0:
        pos_num_list.append(num)
print(pos_num_list)

#---------------------------------------------------------

#Challenge 4: 
# My solution
small_vowel_list = ['a', 'e', 'i', 'o', 'u']
capital_vowel_list = ['A', 'E', 'I', 'O', 'U']
small_count_vowel = 0
capital_count_vowel = 0

user_input_str = input("Enter a string:")


for i in range(len(user_input_str)):
    for j in range(5):
        if user_input_str[i] == small_vowel_list[j]: small_count_vowel = small_count_vowel + 1
            

for i in range(len(user_input_str)):
    for j in range(5):
        if user_input_str[i] == capital_vowel_list[j]: capital_count_vowel = capital_count_vowel + 1  
            

print(small_count_vowel + capital_count_vowel)


#My solution 2:

small_vowel_list = ['a', 'e', 'i', 'o', 'u']
capital_vowel_list = ['A', 'E', 'I', 'O', 'U']


def count_vowel_func(user_text, vowel_list):
    count_vowel = 0
    for i in range(len(user_text)):
        for j in range(5):
            if user_text[i] == vowel_list[j]: count_vowel = count_vowel + 1
    return count_vowel

user_input_str = input("Enter a string:")
print(count_vowel_func(user_input_str,small_vowel_list) + count_vowel_func(user_input_str,capital_vowel_list))

#---------------------------------------------------------



#Challenge 5: 
# My solution

user_text = input("Enter a sentence: ").lower()
replacements = str.maketrans({",": "", ".":"", "!":""})
user_text = user_text.translate(replacements)
word_list = user_text.split()

count_dic = {}
for i in range(len(word_list)):
     x = word_list.count(word_list[i])
     count_dic.update({word_list[i] : x})

for x, y in count_dic.items():
  print(f"{x} -> {y}")

#---------------------------------------------------------


#Challenge 6: 
# My solution

user_text = input("Enter a sentence: ").lower()

replacements = str.maketrans({",": "", ".": "", "!": "", "?": ""})
user_text = user_text.translate(replacements)

word_list = user_text.split()

count_dict = {}

for word in word_list:
    count_dict[word] = count_dict.get(word, 0) + 1

for word, count in count_dict.items():
    if count == 1: print(f"{word} -> {count}")

#---------------------------------------------------------


#Challenge 7: 
# My solution
# Comment: the solution fails with the input: Wow!!! Python---is... amazing???
#It compares only neighbors, It overwrites longest_word every iteration, It does not remember the previous maximum

import string 
user_sentence = input("Enter your sentence: ") 
user_sentence = ''.join(filter(lambda x: x not in string.punctuation, user_sentence)) 
user_sentence = user_sentence.split(" ") 
i = 0 
while i != len(user_sentence)-1: 
    if len(user_sentence[i]) >= len(user_sentence[i+1]): 
        longest_word = user_sentence[i] 
    else: 
        longest_word = user_sentence[i+1] 
    i +=1 
print(longest_word)


#Suggested solution: 
import string

user_sentence = input("Enter your sentence: ")

cleaned = ''.join(
    ch for ch in user_sentence if ch not in string.punctuation
)

words = cleaned.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

if longest_word:
    print(longest_word)


#---------------------------------------------------------


#Challenge 8: Find the second largest word in a sentence

import string

def finding_longest_word(words):
    longest_word = ""
    second_longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            second_longest_word = longest_word
            longest_word = word
    
        elif len(word) > len(second_longest_word) and len(word) < len(longest_word):
                second_longest_word = word
        
    return longest_word, second_longest_word


user_sentence = input("Enter your sentence: ")

if len(user_sentence) == 0: 
    print("No second longest word")
else:
    user_sentence = user_sentence.lower()
    cleaned = ''.join(
    ch for ch in user_sentence if ch not in string.punctuation
)
    words = cleaned.split()
    longest_word, second_longest_word = finding_longest_word(words)

    if len(second_longest_word) == 0: 
        print("No second longest word")
   
    else:
        print(f"Second longest word:",second_longest_word)

"""





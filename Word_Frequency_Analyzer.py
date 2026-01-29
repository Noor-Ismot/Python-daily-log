def passage_format(passage):
    passage = passage.lower()
    punctuation_list = ('.',',',';','-','!','?','""','{','}','[',']',':','...',':','#','(',')')

    for mark in punctuation_list:
        if mark in passage:
            passage = passage.replace(mark,"")

    passage = passage.split()
    return passage


def word_frequency(word_list):
    word_count = {}
    max_frequency = 0
    most_frequent_word = ""

    for word in word_list:
        word_count[word] = word_list.count(word)
        if word_count[word] >= max_frequency:
            max_frequency = word_count[word]
            most_frequent_word = word

    return word_count , most_frequent_word, max_frequency


user_paragraph = input("Enter your passage: ")
word_list = passage_format(user_paragraph)

if len(word_list) == 0:
    print("No Word Found!")
else:
    word_dic,  max_word, frequency = word_frequency(word_list)
    
    print("\n Word List from user input:\n------------------------------")
    for word, word_frequency in word_dic.items():
        print(f" {word}:{word_frequency}")
    
    print(f"\nMost frequent word: {max_word}, Frequency: {frequency}")




    


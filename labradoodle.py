# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

dict_amount = get_number()
dict_words = get_number()

def reverseString(string: str):
    return string[::-1]

def createDictionary(amount):
    words = []
    reversedWords = []

    for _ in range(amount):
        word = get_word()
        words.append(word)
        reversedWords.append(reverseString(word))
    
    return words, reversedWords

words, reversedWords = createDictionary(dict_amount)


def examineWord(word, words, reversedWords):
    init_words = []
    finit_words = []
    for entry in words:
        different = False
        i = 0
        count = 0
        while not different and i<len(entry):
            if entry[i] == word[i]:
                i += 1
                count += 1
            else:
                different = True
        if count >= 3:
            init_words.append(entry)
    for entry in reversedWords:
        i = len(word) - 1
        j = 0
        different = False
        count = 0
        while not different:
            if entry[j] == word[i]:
                i -= 1
                j += 1
                count += 1
            else:
                different = True
        
        if count >= 3:
            finit_words.append(words[reversedWords.index(entry)])
    
    return init_words, finit_words


for _ in range(dict_words):
    word = get_word()
    init_words, finit_words = examineWord(word, words, reversedWords)

    if len(init_words) > 1 or len(finit_words) > 1:
        print("ambiguous")	
    elif len(init_words) == 0 or len(finit_words) == 0:
        print("none")
    else:
        print(init_words[0], finit_words[0])
        
            


    

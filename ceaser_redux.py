# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        data.append("100")
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



def caesar_redux():    
    amount = get_number()
    shift = get_number()
    next_shift = shift
    encrypt = -1
    alfb_minus = ['a', 'b', 'c', "d", 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in range(amount):
        finish = False
        phrase = []
        shift = next_shift
        
        while finish == False:
            word = get_word()

            if word == "the":
                shift *= encrypt

            if word.isdigit():
                finish = True
                next_shift = int(word)
            else:
                phrase.append(word)
        

        answer = []
        for word in phrase:
            new_word = ""
            for letter in word:
                index = alfb_minus.index(letter)
                new_index = (index + shift)%26
                new_word += alfb_minus[new_index]
            answer.append(new_word)

        print(" ".join(answer))

        
        


    return 0


caesar_redux()
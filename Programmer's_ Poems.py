# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   
                
def parser_frase():
    while 1:
        data = list(input().split(' '))
        yield(data)   

input_parser = parser()
input_parser_frase = parser_frase()

def get_word():
    global input_parser
    return next(input_parser)
    
def get_frase():
    global input_parser
    return next(input_parser_frase)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

rimas_N = get_number()
frases_N = get_number()
rimas =[]
palabras = []
v_dicc= {}

i = 0
while i < rimas_N:
    rimas.append(get_frase())
    i+= 1
    
get_frase()
i = 0
while i < frases_N:
    palabras.append(get_frase())
    i+= 1
    
print(rimas)
print(palabras)





        
        
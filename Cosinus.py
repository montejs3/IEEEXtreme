# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        yield(data[0])   

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

def coseno (num):
    contador = 1
    
    if num < 0:
        num += 360
    centinela = True
    while centinela:
        if ((num * contador)%91 == 90 or (num * contador)%271 == 270) :
            print(contador)
            centinela = False
        if contador > 500:
            print("Muy largo")
            centinela = False
        contador += 1
            
    

resultados = get_number()
for i in range(0,resultados):
    numero = get_number()
    coseno(numero)
    
    

    

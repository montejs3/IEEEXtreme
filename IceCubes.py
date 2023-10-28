# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   
                
def parser_linea():
    while 1:
        data = list(input().split(' '))
        yield(data)   

input_parser = parser()
input_parser_linea = parser_linea()

def get_word():
    global input_parser
    return next(input_parser)

def get_linea():
    global input_parser
    return next(input_parser_linea)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

resultados = int(get_number())
matrices =[]
for resultado in range(0,resultados):
    variables = list(get_linea())
    N = int(variables[0])
    M = int(variables[1])
    K = int(variables[2])
    B = int(variables[3])
    matriz = []
    for filas in range(0,N):
        matriz.append(list(get_linea()))
    matrices.append(matriz)
        
print(matrices)

# print(resultados)
# print("\n\n")
# print(b)
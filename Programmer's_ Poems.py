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
parrafo = []
v_dicc= {}
alfabeto = [letra for letra in 'ABCDEFGHIJKLMNOPQRSTUVWYZ']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']


i = 0
while i < rimas_N:
    rimas.append(get_frase())
    i+= 1
    
get_frase()
i = 0
while i < frases_N:
    parrafo.append(get_frase())
    i+= 1
    
    
for palabras in parrafo:
        for rima in rimas:
            for palabra in palabras:
                if palabra in rima and rima[0] not in v_dicc:
                    numero = numeros.pop(0)
                    for p_rima in rima:
                        if p_rima not in v_dicc:
                            v_dicc[p_rima] = numero
                            
rta = ""         
                    
for palabras in parrafo:
    i = 0
    centinela = True
    while i < len(palabras):
        palabra = palabras[i].lower()
        nueva = ""
        if palabra in v_dicc:
            nueva = v_dicc[palabra]
            centinela = False
        i+= 1
    rta += nueva
    if centinela == True:
        rta += "0"
            
# for llave,valor in v_dicc.items():
#     print(llave, valor)

i = 0
while i <= len(rta)-1:
    if rta[i] != rta[i+1]:
        rta = rta[:i] + "0" + rta[i + 1:]
        rta = rta[:i+1] + "0" + rta[i + 2:]
    i += 2

lista_rta =[]

for caracter in rta:
    lista_rta.append(int(caracter))
    

usados = [0]
indices = {0 : "X"}
for i in lista_rta:
    if i not in usados:
        usados.append(i)
        letra = alfabeto.pop(0)
        indices[i] = letra
        
for i in range(len(lista_rta)):
    lista_rta[i] = indices[lista_rta[i]]
    
print("".join(lista_rta))
        

    
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



def generate_happy_numbers(numero):
    encontrados = [1]
    while numero > 0:
        if len(str(numero))> 1:
            pass
    pass

a, b = get_number(), get_number()
numero = max(a, b)

happy_numbers = generate_happy_numbers(numero)


print(len(happy_numbers))





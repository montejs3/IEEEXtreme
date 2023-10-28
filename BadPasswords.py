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


amount_sequences = get_number()


def get_sequences(amount: int):
    list_sequences = []
    
    for _ in range(amount):

        amount_words = int(get_word())
        print(amount_words)
        sequence = []
        for j in range(amount_words):
            sequence.append(get_word())
        list_sequences.append(sequence)
    
    return list_sequences

listSequences = get_sequences(amount_sequences)
amountPasswords = get_number()


def obtainPasswords(amount: int):
    listPasswords = []
    for _ in range(amount):
        oldPassword = get_word()
        newPassword = get_word()
        listPasswords.append((oldPassword,newPassword))
    return listPasswords

listPasswords = obtainPasswords(amountPasswords)
print(listPasswords)

def validation(listPasswords: list, listSequences: list):
    for couple in listPasswords:
        print(obtainPasswordElements(couple, listSequences))
    

def obtainPasswordElements(passwords: tuple, listSequences: list):
    print(listSequences)
    oldPassword = passwords[0]
    newPassword = passwords[1]

    

#     return obtainParts(oldPassword, listSequences), obtainParts(newPassword, listSequences)
      
                

# def obtainParts(password: str, listSequences: list):
#     lookingForSequence = True
    
#     sequenceIndex = 0
#     wordIndex = 0
#     while lookingForSequence:
#         sequence = listSequences[sequenceIndex]
#         lookingForWord = True
#         while lookingForWord:
#             if sequence[wordIndex] in password:
#                 if password.count(sequence[wordIndex]) > 1:
#                     prefix, sequence_word, suffix = findCentralSequence(password, sequence[wordIndex])
#                 else:
#                     ocurrence_index = password.find(sequence[wordIndex])
#                     prefix = password[:ocurrence_index]
#                     sequence_word = password[ocurrence_index:ocurrence_index + len(sequence[wordIndex])]
#                     suffix = password[ocurrence_index + len(sequence[wordIndex]):]
#             else:
#                 wordIndex += 1
#                 if wordIndex == len(sequence):
#                     lookingForWord = False
#                     wordIndex = 0
#         sequenceIndex += 1

# #%%
# def findCentralSequence(password, sequence):            
#     ocurrence_index = []
#     i = 0
#     del_password = password

#     while i < len(password):
#         i = del_password.find(sequence, i)
#         if i == -1:
#             break
#         ocurrence_index.append(i)
#         i += 1

#     center_index = ocurrence_index[(len(ocurrence_index)//2)]
#     prefix = password[:center_index]
#     sequence_word = password[center_index:center_index + len(sequence)]
#     suffix = password[center_index + len(sequence):]

#     return prefix, sequence_word, suffix
    
 

#%%

    
    
    
        
validation(listPasswords, listSequences)

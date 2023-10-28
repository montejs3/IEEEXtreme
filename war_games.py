# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        line = input().strip()
        if line:
            yield line.split()

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

def get_line():
    return list(get_word())

games = (get_line())[0]
cardValues = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]


def add_cart(winner, card):
    winner.append(card)

def popCard(player):
    return player.pop(0)

def examineInfinity(player1, player2):
    return set(player1) == set(player2)

def valueCard(card):
    return cardValues.index(card)

for _ in range(int(games)):
    player1 = get_line()
    player2 = get_line()
    winner = None
    infinity = False
    while not infinity:
        infinity = examineInfinity(player1, player2)
        card1 = popCard(player1)
        card2 = popCard(player2)
        if valueCard(card1) > valueCard(card2):
            add_cart(player1, card2)
        elif valueCard(card1) < valueCard(card2):
            add_cart(player2, card1)
        else:
            add_cart(player1, card1)
            add_cart(player2, card2)
        if len(player2) == 0:
            winner = player1
            break
        elif len(player1) == 0:
            winner = player2
            break
        
        infinity = examineInfinity(player1, player2)
    
    if infinity:
        print("draw")

    if winner == player1:
        print("player 1")
    elif winner == player2:
        print("player 2")
    
# numpy and scipy are available for use



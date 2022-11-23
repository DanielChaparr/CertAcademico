from time import *

import random

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

random.shuffle(deck)

print(f'{"*"*58} \n Bienvenido,¿Listo para empezar? ! \n{"*"*58}')
sleep(2)
print("Probemos tu suerte")
sleep(2)
d_cards = []  
p_cards = []  
sleep(2)
while len(d_cards) != 2:
    random.shuffle(deck)
    d_cards.append(deck.pop())
    if len(d_cards) == 2:
        print("Las cartas del dealer son X ", d_cards[1])

# Displaying the Player's cards
while len(p_cards) != 2:
    random.shuffle(deck)
    p_cards.append(deck.pop())
    if len(p_cards) == 2:
        print("El total del jugador es ", sum(p_cards))
        print("Las cartas que tiene el jugador son ", p_cards)

if sum(p_cards) > 21:
    print(f"Perdiste!\n  {'*'*14}Gana el dealer !!{'*'*14}\n")
    exit()

if sum(d_cards) > 21:
    print(f"El dealer perdio!\n   {'*'*14} Eres el ganador !!{'*'*18}\n")
    exit()

if sum(d_cards) == 21:
    print(f"{'*'*24}Gana el dealer!!{'*'*14}")
    exit()

if sum(d_cards) == 21 and sum(p_cards) == 21:
    print(f"{'*'*17}Empate !!{'*'*25}")
    exit()



def dealer_choice():
    if sum(d_cards) < 17:
        while sum(d_cards) < 17:
            random.shuffle(deck)
            d_cards.append(deck.pop())

    print("El dealer tiene un total de " + str(sum(d_cards)) + "Con las cartas ", d_cards)

    if sum(p_cards) == sum(d_cards):
        print(f"{'*'*15}Empate !!{'*'*15}")
        exit()

    if sum(d_cards) == 21:
        if sum(p_cards) < 21:
            print(f"{'*'*23}Gana el dealer !!{'*'*18}")
        elif sum(p_cards) == 21:
            print(f"{'*'*20}Empate !!{'*'*26}")
        else:
            print(f"{'*'*23}Gana el dealer !!{'*'*18}")

    elif sum(d_cards) < 21:
        if sum(p_cards) < 21 and sum(p_cards) < sum(d_cards):
            print(f"{'*'*23}Gana el dealer !!{'*'*18}")
        if sum(p_cards) == 21:
            print(f"{'*'*22}Ganaste !!{'*'*22}")
        if 21 > sum(p_cards) > sum(d_cards):
            print(f"{'*'*22}Ganaste !!{'*'*22}")

    else:
        if sum(p_cards) < 21:
            print(f"{'*'*22}Ganaste !!{'*'*22}")
        elif sum(p_cards) == 21:
            print(f"{'*'*22}Ganaste !!{'*'*22}")
        else:
            print(f"{'*'*23}Gana el dealer!!{'*'*18}")


while sum(p_cards) < 21:

    
    k = input("¿Planta o sigue?\n Presione 1 para plantar y 0 para seguir ")
    if k == 1:
        random.shuffle(deck)
        p_cards.append(deck.pop())
        print("Tienes un total de" + str(sum(p_cards)) + "Con las cartas", p_cards)
        if sum(p_cards) > 21:
            print(f'{"*"*13}Perdiste!{"*"*13}\n Gana el dealer !!')
        if sum(p_cards) == 21:
            print(f'{"*"*19}Ganaste !!{"*"*29}')

    else:
        dealer_choice()
        break

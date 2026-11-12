import random

valores = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
naipes = ['♠', '♥', '♦', '♣']

def criarBaralho():
    baralho = [(v, n) for v in valores for n in naipes]
    random.shuffle(baralho)
    return baralho
print(criarBaralho())
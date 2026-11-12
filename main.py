import random
from estruturas import Queue

valores = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
naipes = ['♠', '♥', '♦', '♣']

def criarBaralho():
    baralho = [(v, n) for v in valores for n in naipes]
    random.shuffle(baralho)
    return baralho

def pontuar(mao):
    total = sum(valores[v] for v, _ in mao)
    ases = sum(1 for v, _ in mao if v == 'A')
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total

def sacar(baralho, cartasUsadas):
    carta = baralho.pop()
    cartasUsadas.add(carta)
    return carta

def mostrar(mao):
    return ' '.join(f'{v}{n}' for v, n in mao)

def turnoJogador(baralho, mao, usadas):
    while pontuar(mao) < 21:
        print('=' * 100)
        print(f'Sua mão: {mostrar(mao)} ({pontuar(mao)})')
        if input('[p] pedir   [s] parar   ').strip().lower() == 'p':
            mao.append(sacar(baralho, usadas))
        else:
            break
    print(f'Mão final: {mostrar(mao)} ({pontuar(mao)})')
    print('=' * 100)
        
def turnoDealer(baralho, mao, usadas):
    while pontuar(mao) < 21:
        mao.append(sacar(baralho, usadas))
    print(f'Mão do dealer: {mostrar(mao)} ({pontuar(mao)})')
    
def definirGanhador(j, d):
    if j > 21:
        return 'Dealer'
    if d > 21 or j > d:
        return 'Jogador'
    if d > j:
        return 'Dealer'
    return 'Empate'

def main():
    baralho = []
    usadas = set()
    
    while True:
        if len(baralho) < 15:
            baralho[:] = criarBaralho()
            usadas.clear()
            
        maos = {'Jogador': [], 'Dealer': []}
        for _ in range(2):
            for nome in maos:
                maos[nome].append(sacar(baralho, usadas))
                
        fila = Queue()
        fila.enqueue('Jogador')
        fila.enqueue('Dealer')
        
        while not fila.isEmpty():
            vez = fila.dequeue()
            if vez == 'Jogador':
                turnoJogador(baralho, maos['Jogador'], usadas)
                print(f'Sua pontuação: {pontuar(maos['Jogador'])}')
            else:
                if pontuar(maos['Jogador']) <= 21:
                    turnoDealer(baralho, maos['Dealer'], usadas)
                
        vencedor = definirGanhador(pontuar(maos['Jogador']), pontuar(maos['Dealer']))
        print(f'Resultado: {vencedor}')
            
        if input('\nJogar de novo? [s] sim [n] não   ').strip().lower() != 's':
            print('Até logo ^^/')
            break
        
print(main())    
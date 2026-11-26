from estruturas import Stack   
from logos import VERDE, VERMELHO, AMARELO, AZUL, CIANO, RESET, NEGRITO
import cartas

import random

valores = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
naipes = {'♠': 'e', '♥': 'c', '♦': 'o', '♣': 'p' }

def desenharCartas(carta):
    v, n = carta
    num = '1' if v == 'A' else v.lower()
    funcao = getattr(cartas, f'c{num}{naipes[n]}')
    return [l.rstrip().ljust(15) for l in funcao().split('\n') if l.strip()]

def desenharMao(mao):
    desenhos = [desenharCartas(c) for c in mao]
    return '\n'.join(' '.join(d[i] for d in desenhos) for i in range(len(desenhos[0])))

def criarBaralho():
    baralhoCompleto = [(v, n) for v in valores for n in naipes]
    random.shuffle(baralhoCompleto)
    baralho = Stack()
    
    for carta in baralhoCompleto:
        baralho.push(carta)
    return baralho

def embaralhar(baralho, descarte):
    baralhoCompleto = []
    
    while not baralho.isEmpty():
        baralhoCompleto.append(baralho.pop())
    while not descarte.isEmpty():
        baralhoCompleto.append(descarte.pop())
        
    random.shuffle(baralhoCompleto)
    for carta in baralhoCompleto:
        baralho.push(carta)
        
def descartar(usadas, descarte):
    for carta in usadas:
        descarte.push(carta)
    usadas.clear()

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

def turnoJogador(baralho, mao, usadas):
    while pontuar(mao) < 21:
        print(AZUL + '=' * 100 + RESET)
        print(CIANO + f'Sua mão ({pontuar(mao)}):' + RESET)
        print(desenharMao(mao))
        
        opcao = input(AMARELO + '[p] pedir   [s] parar   ' + RESET).strip().lower()
        
        if opcao == 'p':
            mao.append(sacar(baralho, usadas))
        elif opcao == 's':
            break
        else:
            print('Opção inválida')
            
    print(NEGRITO + AZUL + f'Mão final ({pontuar(mao)}):' + RESET)
    print(desenharMao(mao))
    print(AZUL + '=' * 100 + RESET)
        
def turnoDealer(baralho, mao, usadas):
    while pontuar(mao) < 17:
        mao.append(sacar(baralho, usadas))
    print(VERMELHO + f'Mão do dealer ({pontuar(mao)}):' + RESET)
    print(desenharMao(mao))
    
def definirGanhador(j, d):
    if j > 21:
        return 'Dealer'
    if d > 21 or j > d:
        return 'Jogador'
    if d > j:
        return 'Dealer'
    return 'Empate'

def pedirAposta(fichas):
    pilha = Stack()
    aposta = 0
    
    while True:
        print(AMARELO + f'Fichas disponíveis: {fichas - aposta} \n\nEscolha o valor da ficha: \n[5] [10] [25] [50]\n' + RESET)
        
        valor = input(CIANO + 'Valor: ' + RESET).strip()
        
        if not valor.isdigit() or int(valor) not in [5, 10, 25, 50]:
            print(VERMELHO + 'Valor inválido' + RESET)
            continue
        
        valor = int(valor)
        
        if aposta +  valor > fichas:
            print(VERMELHO + 'Você não possui fichas suficientes.' + RESET)
            continue
        
        pilha.push(valor)
        aposta += valor
        
        while True:
            print(AMARELO + f'\nAposta atual: {aposta} fichas' + RESET)
            resposta = input(CIANO + '[a] adicionar outra ficha [d] desfazer última ficha [c] confirmar  ' + RESET).strip().lower()
            
            if resposta == 'c':
                return aposta
            elif resposta == 'a':
                break
            
            elif resposta == 'd':
                aposta -= pilha.pop()
                print(VERMELHO + 'Última ficha removida.' + RESET)
                if pilha.isEmpty():
                    break
            
            else:
                print(VERMELHO + 'Resposta inválida! Digite a, d ou c.' + RESET)
    
def atualizarFichas(fichas, aposta, vencedor):
    if vencedor == 'Jogador':
        print(VERDE + f'Você ganhou {aposta} fichas!' + RESET)
        return fichas + aposta
    
    if vencedor == 'Dealer':
        print(VERMELHO + f'Você perdeu {aposta} fichas.' + RESET)
        return fichas - aposta
    
    print(AMARELO + 'Empate: suas fichas foram devolvidas' + RESET)
    return fichas

def mostrarPlacar(placar, fichas):
    print('=' * 40)
    
    print(f"PLACAR Jogador {placar['Jogador']} x  {placar['Dealer']} Dealer  (empates: {placar['Empate']})")
    print(f'Fichas: {fichas}')
    
    print('=' * 40)
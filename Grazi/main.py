import sys
from pathlib import Path # Função para importar arquivos de outros diretórios

sys.path.insert(0, str(Path(__file__).resolve().parent.parent)) # Caminho da pasta principal do projeto

from logos import logo_21
from estruturas import Queue, Stack
from funcoes import *

fichasIniciais = 200
baralhoMinimo = 30

def main():
    logo_21()
    
    baralho = criarBaralho()
    usadas = set()
    descarte = Stack()
    fichas = fichasIniciais
    placar = {'Jogador': 0, 'Dealer': 0, 'Empate': 0}
    
    while fichas > 0:
        if baralho.size() < baralhoMinimo:
            print('Embaralhando cartas...')
            embaralhar(baralho, descarte)
            
        aposta = pedirAposta(fichas)
            
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
                print(f"Sua pontuação: {pontuar(maos['Jogador'])}")
            else:
                if pontuar(maos['Jogador']) <= 21:
                    turnoDealer(baralho, maos['Dealer'], usadas)
                
        vencedor = definirGanhador(pontuar(maos['Jogador']), pontuar(maos['Dealer']))
        print(f'Resultado: {vencedor}')
        
        fichas = atualizarFichas(fichas, aposta, vencedor)
        placar[vencedor] += 1
        descartar(usadas, descarte)
        mostrarPlacar(placar, fichas)
        
        if fichas == 0:
            print('Você ficou sem fichas! Fim de jogo.')
            break
            
        resposta = input('\nJogar de novo? [s] sim [n] não  ').strip().lower()
        
        while resposta not in ['s', 'n']:
            print('Resposta inválida! Digite s ou n')
            resposta = input('\nJogar de novo? [s] sim [n] não  ').strip().lower()
            
        if resposta == 'n': 
            print(f'Você saiu com {fichas} fichas. Até logo ^^/')
            break    
        
if __name__ == '__main__':
    main()
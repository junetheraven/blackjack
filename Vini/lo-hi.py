from cartas import *
from Estruturas import *
import random
print("Sejam bem vindo(s) ao jogo LO-HINI\n Um jogo de batata quente com cartas!!\n Se divirtam!!")
x = int(input("Quantos jogadores serão? "))
if x >= 2:
    jogadores = {}
    fila = Queue()
    for i in range(x):
        y = input(f"Qual o nome do {i+1}° jogador(a)? ")
        fila.enqueue(y)
        jogadores[y] = {"Créditos": 500}
    limpar_tela()
    while fila.size()>1:
        random.shuffle(fila.items)
        baralhomesa = None
        mesa = 10
        baralho = embaralhar()
        for i in fila.items:
            jogadores[i]["Créditos"] -= 10
        baralhomesa = baralho.pop()
        print("Todos os jogadores pagaram 10 créditos de entrada!")
        input("\nPodemos começar? ENTER ")
        limpar_tela()
        while True:
            if baralho.isEmpty():
                baralho = embaralhar()
            jog = fila.dequeue()
            print(f"Vez de {jog} | Valendo {mesa} créditos")
            print("Carta:")
            imgcarta([baralhomesa], mostrar_indices=False)
            while True:
                esc = input("\nA próxima carta será [1] Maior,  [2] Menor ou [3] igual? ").strip()
                if esc in ("1", "2", "3"):
                    break
                print("Opção inválida! Digite apenas 1, 2 ou 3.")
            novacarta = baralho.pop()
            print("A próxima carta é:")
            imgcarta([novacarta], mostrar_indices=False)
            cartaant = valores[baralhomesa[0]]
            cartanov = valores[novacarta[0]]
            if (cartaant<cartanov and esc == '1') or (cartanov<cartaant and esc=='2') or (cartaant==cartanov and esc == '3'):
                mesa +=10
                print("Acertou!!")
                input("Aperte ENTER para ser a vez do próximo")
                limpar_tela()
                baralhomesa = novacarta
            else:
                print("Errou!!")
                jogadores[jog]["Créditos"] -= mesa
                for i in fila.items:
                    jogadores[i]["Créditos"] += mesa
                    print(f"{i} ganhou {mesa} créditos!")
                fila.enqueue(jog)
                break
            fila.enqueue(jog)
        input("\nAperte ENTER para ver os créditos atualizados ")
        limpar_tela()
        print("=" * 40)
        print("CRÉDITOS ATUALIZADOS".center(40))
        print("=" * 40)
        for i in range(fila.size()):
            jog = fila.dequeue()
            print(f"{jog}: {jogadores[jog]['Créditos']} créditos")
            fila.enqueue(jog)
        for i in range (fila.size()):
            jog = fila.dequeue()
            if jogadores[jog]["Créditos"] > 0:
                fila.enqueue(jog)
            else:
                print("\n")
                print(f"\033[31mJogador {jog} ficou sem créditos e foi eliminado!\033[0m")
        p = input("\nPressione ENTER para próxima partida (ou 'p' e ENTER para parar): ").strip().lower()
        if p == 'p':
            break
        limpar_tela()
    limpar_tela()
    print("\n" + "=" * 40)
    print("FIM DE JOGO - RANKING FINAL".center(40))
    print("=" * 40)
    ranking = []
    while not fila.isEmpty():
        jog = fila.dequeue()
        ranking.append((jogadores[jog]["Créditos"], jog))
    heapSort(ranking)
    ranking.reverse()
    pos = 1
    for creditos, nome in ranking:
        print(f"{pos}° lugar: {nome} - {creditos} créditos")
        pos += 1
else:
    print("")
import random
import cartas
import os
from Estruturas import *
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def imgcarta(mao, naipes):
    cartas_fatiadas = []
    for valor, naipe in mao:
        if valor == 'A':
            num = '1'
        else:
            num = valor.lower()
        nome = f'c{num}{naipes[naipe]}'
        funcao = getattr(cartas, nome)
        desenho = funcao()
        fatias = []
        for linha in desenho.split('\n'):
            if linha.strip() != "":
                fatias.append(linha.rstrip().ljust(15))
        cartas_fatiadas.append(fatias)
    carta1 = cartas_fatiadas[0]
    carta2 = cartas_fatiadas[1]
    carta3 = cartas_fatiadas[2]
    for i in range(len(carta1)):
        print(carta1[i], carta2[i], carta3[i])
    print("      [1]      ", "      [2]      ", "      [3]      ")

print("Bem vindo ao jogo PASS\n Para jogar esse jogo tem que ter no mínimo 3 jogadores e no máximo 8.\n Se divirtam!!")
x = int(input("Quantos jogadores serão? "))
if x<3:
    print("Necessita-se de mais jogadores")
elif x>8:
    print("Se excedeu o número máximo de jogadores")
else:
    cassino = 0
    jogadores = {}
    fila = Queue()
    cartasj = []
    valores = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13
    }
    naipes = {
        '♠': 'e', '♥': 'c', '♦': 'o', '♣': 'p'
    }
    for v in valores:
        for n in naipes:
            cartasj.append((v, n))
    for i in range(x):
        y = input(f"Qual o nome do {i+1}° jogador(a)? ")
        fila.enqueue(y)
        jogadores[y] = {"Créditos": 100}
    random.shuffle(fila.items)
    while fila.size()>2:
        mesa = 0
        baralho = Stack()
        random.shuffle(cartasj)
        for i in cartasj:
            baralho.push(i)
        for i in fila.items:
            jogadores[i]["Créditos"] -= 10
            mesa += 10
            jogadores[i]["Pass"] = 1
            jogadores[i]["Mão"] = [baralho.pop(), baralho.pop(), baralho.pop()]
        for i in range(fila.size()):
            cartamesa = True
            descarte = None
            rodadas = fila.size()
            for a in range(rodadas):
                print(f"=== RODADA {i+1} de {rodadas} ===")
                jog = fila.dequeue()
                input(f"Vez de {jog}\n Quando você estiver seguro(a) que seus adversários não possam olhar sua carta, aperte ENTER")
                limpar_tela()
                print(f"=== RODADA {i+1} de {rodadas} ===")
                mao = jogadores[jog]["Mão"]
                print(f"\nVez de {jog} | Passes restantes: {jogadores[jog]['Pass']}")
                print(f"Sua mão: ")
                imgcarta(mao, naipes)
                if jogadores[jog]["Pass"] > 0:
                    while True:
                        esc = input("Qual carta deseja descartar [1, 2 ou 3]? Ou deseja usar o Pass? [p] ").strip().lower()
                        if esc in ("1", "2", "3", "p"):
                            break
                        print("Opção inválida! Digite apenas 1, 2, 3 ou p.")
                else:
                    while True:
                        esc = input("Qual carta deseja descartar [1, 2 ou 3]? ").strip()
                        if esc in ("1", "2", "3"):
                            break
                        print("Opção inválida! Digite apenas 1, 2 ou 3.")
                if esc == "p":
                    jogadores[jog]["Pass"] -= 1
                    print("Pass usado! Sua mão permanece a mesma!!")
                else:
                    esc = int(esc)
                    if cartamesa:
                        mao.append(baralho.pop())
                        cartamesa = False
                    else:
                        mao.append(descarte)
                    descarte = mao.pop(esc-1)
                    print("Sua mão agora é: ")
                    imgcarta(mao, naipes)
                input("Aperte ENTER para passar para o próximo jogador")
                limpar_tela()
                fila.enqueue(jog)
            fila.enqueue(fila.dequeue())
        print("\n" + "=" * 40)
        print("RESULTADO DA PARTIDA".center(40))
        print("=" * 40)
        sobreviventes= {}
        for i in fila.items:
            mao = jogadores[i]["Mão"]
            pontos = 0
            for v, n in mao:
                pontos += valores[v]
            if pontos<=21:
                sobreviventes[i]= pontos
                print(f"Seu total de pontos {i}: {pontos}")
                imgcarta(mao, naipes)
                print("\n")
            else:
                print(f"Adoramos ter você aqui {i} :3")
                imgcarta(mao, naipes)
                print(f"{pontos} pontos")
                print("\n")
        if len(sobreviventes) != 0:
            vencedores = []
            maior = max(sobreviventes.values())
            for nome, pnts in sobreviventes.items():
                if pnts==maior:
                    vencedores.append(nome)
            if len(vencedores)>1:
                naipesvencedor = {}
                for nome in vencedores:
                    contador = {}
                    for v, n in jogadores[nome]["Mão"]:
                        if n in contador:
                            contador[n] += 1
                        else:
                            contador[n] = 1
                    naipesvencedor[nome] = max(contador.values())
                maior = max(naipesvencedor.values())
                vencedores = []
                for nome, qntd in naipesvencedor.items():
                    if qntd == maior:
                        vencedores.append(nome)
                if len(vencedores)>1:
                    realeza = {}
                    for nome in vencedores:
                        peso = 0
                        for v, n in jogadores[nome]["Mão"]:
                            if v == "J":
                                peso += 1
                            if v == "Q":
                                peso +=2
                            if v == "K":
                                peso += 3
                        realeza[nome] = peso
                    maior = max(realeza.values())
                    vencedores = []
                    for nome, peso in realeza.items():
                        if peso == maior:
                            vencedores.append(nome)
                    if len(vencedores)>1:
                        dupla = {}
                        for nome in vencedores:
                            valor = []
                            for v, n in jogadores[nome]["Mão"]:
                                valor.append(valores[v])
                            heapSort(valor)
                            dupla[nome] = valor[0] + valor[1]
                        maior = max(dupla.values())
                        vencedores = []
                        for nome, qntd in dupla.items():
                            if qntd==maior:
                                vencedores.append(nome)
                        if len(vencedores)>1:
                            print("Como houve um empate definitivo, os créditos ficarão para nós o DGRV!")
                            cassino += mesa
                        else:
                            print(f"O vencedor {vencedores[0]} ganhou por pela soma das 2 menores cartas serem maiores!!")
                    else:
                        print(f"O vencedor {vencedores[0]} ganhou por ter a maior carta de realeza!!")
                else:
                    print(f"O vencedor {vencedores[0]} ganhou por ter mais naipes iguais!!")
            if len(vencedores) == 1:
                jogadores[vencedores[0]]["Créditos"] += mesa
                print(f"O ganhador dessa partida foi {vencedores[0]}!!")
        else:
            print("Todos passaram de 21!")
            cassino += mesa
        print("Créditos de jogadores atualizados!!")
        for i in range(fila.size()):
            jog = fila.dequeue()
            print(f"{jog}: {jogadores[jog]['Créditos']} créditos")
            if jogadores[jog]["Créditos"]>0:
                fila.enqueue(jog)
            else:
                print(f"Jogador {jog} por falta de créditos foi eliminado!")
        print(f"Cassino DGRV: {cassino} créditos")
        input("\nPressione ENTER para começar outra partida!")
        limpar_tela()
    print("\n" + "=" * 40)
    print("FIM DE JOGO - RANKING FINAL".center(40))
    print("=" * 40)
    ranking = [(cassino, "Cassino DGRV")]
    while not fila.isEmpty():
        jog = fila.dequeue()
        ranking.append((jogadores[jog]["Créditos"], jog))
    heapSort(ranking)
    ranking.reverse()
    pos = 1
    for creditos, nome in ranking:
        print(f"{pos}° lugar: {nome} - {creditos} créditos")
        pos += 1 

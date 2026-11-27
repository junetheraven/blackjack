import random
import sys
from pathlib import Path
from cartas import *
from Estruturas import *
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from logos import logo_vini_1

logo_vini_1()

print("Bem vindo ao jogo VINI-ONE\n Para jogar esse jogo tem que ter no mínimo 3 jogadores e no máximo 8.\n Se divirtam!!")
x = int(input("Quantos jogadores serão? "))
if x < 3:
    print("Necessita-se de mais jogadores")
elif x > 8:
    print("Se excedeu o número máximo de jogadores")
else:
    cassino = 0
    jogadores = {}
    fila = Queue()
    for i in range(x):
        y = input(f"Qual o nome do {i+1}° jogador(a)? ")
        h = 500
        '''while True:
            h = int(input("Quantos créditos você quer comprar? (mínimo 10): "))
            if h >= 10:
                break
            print("Valor inválido! Você precisa de pelo menos 10 créditos para entrar na mesa.")'''
        fila.enqueue(y)
        jogadores[y] = {"Créditos": h, "Pass": 0}
    random.shuffle(fila.items)
    limpar_tela()
    while fila.size() > 2:
        baralho = embaralhar()
        apostareal = 0
        apostas = 0
        mesa = 0
        mesaaposta = 0
        print("Todos os jogadores pagaram 10 de créditos")
        print("\n")
        for i in fila.items:
            jogadores[i]["Aposta"] = 0
            jogadores[i]["Créditos"] -= 10
            mesa += 10
            if jogadores[i]["Pass"] < 2:
                jogadores[i]["Pass"] += 1
            jogadores[i]["Mão"] = [baralho.pop(), baralho.pop(), baralho.pop()]
            print(f"{i} atualmente tem: {jogadores[i]['Créditos']} de créditos")
        input("Podemos começar? ENTER ")
        limpar_tela()
        for i in range(fila.size()):
            cartamesa = True
            descarte = None
            rodadas = fila.size()
            for a in range(rodadas):
                print(f"=== RODADA {i+1} de {rodadas} ===")
                jog = fila.dequeue()
                input(f"Vez de {jog}\n Quando você estiver seguro(a) que seus adversários não possam olhar sua carta, aperte ENTER ")
                limpar_tela()
                print(f"=== RODADA {i+1} de {rodadas} ===")
                mao = jogadores[jog]["Mão"]
                print(f"\nVez de {jog} | Passes restantes: {jogadores[jog]['Pass']}")
                print("Sua mão: ")
                imgcarta(mao)
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
                    descarte = mao.pop(esc - 1)
                    print("Sua mão agora é: ")
                    imgcarta(mao)
                if i == (rodadas - 1):
                    if jogadores[jog]["Créditos"] > 0:
                        print(f"Seus créditos: {jogadores[jog]['Créditos']}")
                        print(f"Apostas registradas: {apostas}")
                        if apostas > 0:
                            for v in fila.items:
                                if jogadores[v]["Aposta"] == 0:
                                    continue
                                else:
                                    print(f"{v} apostou {jogadores[v]['Aposta']} créditos")
                        while True:
                            print("\n")
                            s = input("Deseja fazer alguma aposta? [s/n] ").strip().lower()
                            if s in ('s', 'n'):
                                break
                            print("Opção inválida! Digite a opção correta!")
                        if s == 's':
                            while True:
                                p = int(input("Quanto você vai apostar? "))
                                if 0 <= p <= jogadores[jog]["Créditos"]:
                                    break
                                print(f"Valor inválido! Digite entre 0 e {jogadores[jog]['Créditos']} créditos.")
                            if p > 0:
                                apostas += 1
                                if p>=50:
                                    apostareal += 1
                            jogadores[jog]["Créditos"] -= p
                            jogadores[jog]["Aposta"] += p
                            mesaaposta += p
                input("Aperte ENTER para passar para o próximo jogador ")
                limpar_tela()
                fila.enqueue(jog)
            if apostareal == 1:
                mesaaposta *= 2
                print(f"O pote de apostas dobrou para {mesaaposta} créditos!")
            fila.enqueue(fila.dequeue())
        print("\n" + "=" * 40)
        print("RESULTADO DA PARTIDA".center(40))
        print("=" * 40)
        sobreviventes = {}
        for i in fila.items:
            mao = jogadores[i]["Mão"]
            pontos = 0
            for v, n in mao:
                pontos += valores[v]
            if pontos <= 21:
                sobreviventes[i] = pontos
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
                if pnts == maior:
                    vencedores.append(nome)
            if len(vencedores) > 1:
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
                if len(vencedores) > 1:
                    realeza = {}
                    for nome in vencedores:
                        peso = 0
                        for v, n in jogadores[nome]["Mão"]:
                            if v == "J":
                                peso += 1
                            if v == "Q":
                                peso += 2
                            if v == "K":
                                peso += 3
                        realeza[nome] = peso
                    maior = max(realeza.values())
                    vencedores = []
                    for nome, peso in realeza.items():
                        if peso == maior:
                            vencedores.append(nome)
                    if len(vencedores) > 1:
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
                            if qntd == maior:
                                vencedores.append(nome)
                        if len(vencedores) > 1:
                            print("Como houve um empate definitivo, os créditos ficarão para nós o DGRV!")
                            cassino += (mesa + mesaaposta)
                        else:
                            print(f"O vencedor {vencedores[0]} ganhou pela soma das 2 menores cartas ser maior!!")
                    else:
                        print(f"O vencedor {vencedores[0]} ganhou por ter a maior carta de realeza!!")
                else:
                    print(f"O vencedor {vencedores[0]} ganhou por ter mais naipes iguais!!")
            if len(vencedores) == 1:
                jogadores[vencedores[0]]["Créditos"] += (mesa + mesaaposta)
                print(f"O ganhador dessa partida foi {vencedores[0]}!!")
        else:
            print("Todos passaram de 21!")
            cassino += (mesa + mesaaposta)
        print("Créditos de jogadores atualizados!!")
        for i in range(fila.size()):
            jog = fila.dequeue()
            print(f"{jog}: {jogadores[jog]['Créditos']} créditos")
            if jogadores[jog]["Créditos"] > 0:
                while True:
                    c = input("Deseja continuar? [s/n] ").strip().lower()
                    if c in ('s', 'n'):
                        break
                    print("Opção inválida! Digite s/n.")
                if c == 's':
                    fila.enqueue(jog)
                print("Perfeito!")
            else:
                print(f"Jogador {jog} por falta de créditos foi eliminado!")
        print(f"Cassino DGRV: {cassino} créditos")
        if fila.size()<=2:
            p = 'p'
            input("Vamos ao ranking!!! [ENTER]")
        else:
            p = input("\nPressione ENTER para próxima partida (ou 'p' e ENTER para parar): ").strip().lower()
        if p == 'p':
            break
        limpar_tela()
    limpar_tela()
    print("\n" + "=" * 40)
    print("FIM DE JOGO - RANKING FINAL".center(40))
    print("=" * 40)
    ranking = [(cassino, "Cassino DGRV")]
    for nome, dados in jogadores.items():
        ranking.append((dados["Créditos"], nome))
    heapSort(ranking)
    ranking.reverse()
    pos = 0
    anterior = None
    for i in range(len(ranking)):
        creditos, nome = ranking[i]
        if creditos != anterior:
            pos = i + 1
        print(f"{pos}° lugar: {nome} - {creditos} créditos")
        anterior = creditos
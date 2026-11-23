import random
import time
from estrutura import Pilha, Fila
from dados import cores, faces_dado

ODDS_TIE = {
    2: 88.0, 12: 88.0,
    3: 25.0, 11: 25.0,
    4: 10.0, 10: 10.0,
    5: 6.0,  9: 6.0,
    6: 4.0,  7: 4.0,  8: 4.01
}

def colorir(texto, chave):
    cor = cores.get(chave, "")
    return f"{cor}{texto}{cores['Reset']}"

def desenhar_dados(lista_valores, lado):
    desenhos = [faces_dado[valor] for valor in lista_valores]
    for linhas_lado_a_lado in zip(*desenhos):
        print(colorir("  ".join(linhas_lado_a_lado), lado))

def fase_de_apostas(saldo):
    print(f"\nSaldo atual: \033[1;32mR$ {saldo:.2f}\033[m")
    print("Escolha sua aposta:")
    print("\033[1;34m[1] Player - Paga 2x\033[m")
    print("\033[1;31m[2] Banker - Paga 2x\033[m")
    print("\033[1;33m[3] Tie (Empate) - Paga de 4x até 88x\033[m")

    opcoes = {"1": "Player", "2": "Banker", "3": "Tie"}
    escolha = ""
    while escolha not in opcoes:
        escolha = input("Opção (1/2/3): ").strip()
    lado_apostado = opcoes[escolha]
    pilha_fichas = Pilha()

    while True:
        print(f"\nApostando em: \033[1m{lado_apostado}\033[m | Total na mesa: \033[1;32mR$ {pilha_fichas.total():.2f}\033[m | Saldo restante: \033[1;32mR$ {saldo:.2f}\033[m")
        print("Compre uma ficha \033[1;31;40m[5]\033[m +R$5 | \033[1;31;40m[10]\033[m +R$10 | \033[1;31;40m[25]\033[m +R$25 | \033[1;31;40m[50]\033[m +R$50 | [D] Desfazer última ficha | [C] Confirmar")
        acao = input("Sua ação: ").strip().upper()

        if acao in ("5", "10", "25", "50"):
            valor = float(acao)
            if valor <= saldo:
                pilha_fichas.push(valor)
                saldo -= valor
            else:
                print(">> Saldo insuficiente para essa ficha.")
        elif acao == "D":
            ficha_removida = pilha_fichas.pop()
            if ficha_removida is not None:
                saldo += ficha_removida
                print(f">> Ficha de \033[1;32mR$ {ficha_removida:.2f}\033[m removida.")
            else:
                print(">> Nenhuma ficha na mesa para desfazer.")
        elif acao == "C":
            if pilha_fichas.total() > 0:
                break
            else:
                print(">> Coloque pelo menos uma ficha antes de confirmar.")
        else:
            print(">> Comando inválido.")

    return lado_apostado, pilha_fichas.total(), saldo


def rodar_dados():
    fila_turnos = Fila()

    fila_turnos.enqueue(("Player", (random.randint(1, 6), random.randint(1, 6))))
    fila_turnos.enqueue(("Banker", (random.randint(1, 6), random.randint(1, 6))))

    tupla_player = ()
    tupla_banker = ()

    while not fila_turnos.is_empty():
        lado, dados = fila_turnos.dequeue()

        print(colorir(f"\nAgitando os dados do {lado}...", lado))
        time.sleep(1.5)

        desenhar_dados(dados, lado)
        print(f" Dados do {lado}: {dados[0]} + {dados[1]} = {sum(dados)}")

        if lado == "Player":
            tupla_player = dados
        else:
            tupla_banker = dados

    return tupla_player, tupla_banker


def liquidar_rodada(lado_apostado, valor_aposta, tupla_player, tupla_banker, saldo):
    soma_player = sum(tupla_player)
    soma_banker = sum(tupla_banker)

    time.sleep(1.5)
    print("\n\033[1m--- RESULTADO FINAL ---\033[m")
    print(f"\033[1;34mPlayer: {tupla_player[0]} + {tupla_player[1]} = {soma_player}\033[m")
    print(f"\033[1;31mBanker: {tupla_banker[0]} + {tupla_banker[1]} = {soma_banker}\033[m")

    if soma_player > soma_banker:
        vencedor = "Player"
        print(f"\033[1mVencedor da rodada: \033[1;34m{vencedor.upper()}\033[m")
    elif soma_banker > soma_player:
        vencedor = "Banker"
        print(f"\033[1mVencedor da rodada: \033[1;31m{vencedor.upper()}\033[m")
    else:
        vencedor = "Tie"
        print(f"\033[1mVencedor da rodada: \033[1;33m{vencedor.upper()}\033[m")


    if vencedor == "Tie":
        if lado_apostado == "Tie":
            multiplicador = ODDS_TIE[soma_player]
            premio = valor_aposta * multiplicador
            saldo += premio
            print(f"\033[1;32m EMPATE EM {soma_player}! Odd de {multiplicador:.0f}x! Você ganhou R$ {premio:.2f}!")
        else:
            reembolso = valor_aposta * 0.90
            saldo += reembolso
            print(f"\033[1;33mDeu Empate! Regra dos 90%: R$ {reembolso:.2f} devolvidos para sua carteira.\033[m")
    elif lado_apostado == vencedor:
        premio = valor_aposta * 2.0
        saldo += premio
        print(f"\033[1;32mVocê venceu apostando em {lado_apostado}! Recebeu R$ {premio:.2f}.\033[m")
    else:
        print(f"\033[1;31mVocê perdeu a aposta de R$ {valor_aposta:.2f}.\033[m")

    return saldo


def iniciar_bac_bo():
    saldo = 100.0
    print("\n\033[1;40m=== BEM-VINDO AO BAC BO ===\033[m")

    while saldo >= 5.0:
        lado, valor_aposta, saldo = fase_de_apostas(saldo)
        tupla_player, tupla_banker = rodar_dados()
        saldo = liquidar_rodada(lado, valor_aposta, tupla_player, tupla_banker, saldo)

        print(f"\nSaldo atualizado: \033[1;32mR$ {saldo:.2f}\033[m")
        if saldo < 5.0:
            print("Saldo insuficiente para continuar jogando (aposta mínima R$ 5,00).")
            break

        continuar = input("Jogar outra rodada? (S/N): ").strip().upper()
        if continuar != "S":
            break

    print(f"\nFim de jogo! Você saiu da mesa com \033[1;32mR$ {saldo:.2f}.\033[m")


if __name__ == "__main__":
    iniciar_bac_bo()
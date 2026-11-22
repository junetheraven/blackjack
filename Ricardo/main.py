import random
import sys
from fila import Queue

from pathlib import Path # Função para importar arquivos de outros diretórios
sys.path.insert(0, str(Path(__file__).resolve().parent.parent)) # Caminho da pasta principal do projeto
from logos import logo_roleta


# Tuplas de valores da roleta
VERMELHOS = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
PRETOS = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)


def cor_do_numero(numero: int) -> str:
    if numero == 0:
        return "verde"
    if numero in VERMELHOS:
        return "vermelho"
    if numero in PRETOS:
        return "preto"
    raise ValueError("Número da roleta deve estar entre 0 e 36.")


def jogar_roleta():
    saldo = 100.0
    historico = Queue() # Fila para armazenar os últimos números sorteados
    logo_roleta() 

    while saldo > 0:
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        tipo = input(
            "Apostar em 'cor' ou 'numero', ver 'historico' ou 'sair'? "
        ).strip().lower()

        if tipo == "sair":
            break
        if tipo == "historico":
            numeros = historico.to_list() # Funcão para obter os últimos números sorteados em ordem
            if numeros:
                print("Últimos números sorteados: " + ", ".join(map(str, numeros)))
            else:
                print("Ainda não há números sorteados.")
            continue
        if tipo not in {"cor", "numero"}:
            print("Opção inválida.")
            continue

        try:
            aposta = float(input("Valor da aposta: R$ "))
        except ValueError:
            print("Digite um valor numérico válido.")
            continue

        if aposta <= 0 or aposta > saldo:
            print("Valor de aposta inválido ou saldo insuficiente.")
            continue

        if tipo == "cor":
            escolha = (
                input("Escolha a cor (vermelho, preto ou verde): ").strip().lower()
            )
            if escolha not in {"vermelho", "preto", "verde"}:
                print("Cor inválida.")
                continue
        else:
            try:
                escolha = int(input("Escolha um número (0 a 36): "))
            except ValueError:
                print("Digite um número inteiro.")
                continue
            if escolha < 0 or escolha > 36:
                print("Número fora do intervalo de 0 a 36.")
                continue

        sorteado = random.randint(0, 36)
        cor_sorteada = cor_do_numero(sorteado)
        print(f"Resultado: {sorteado} ({cor_sorteada})")
        historico.enqueue(sorteado)
        if historico.size() > 3:
            historico.dequeue()

        if tipo == "cor" and escolha == cor_sorteada:
            multiplicador = 14 if escolha == "verde" else 2
            ganho = aposta * multiplicador
            saldo += ganho - aposta
            print(f"Você ganhou R$ {ganho:.2f}!")
        elif tipo == "numero" and escolha == sorteado:
            ganho = aposta * 36
            saldo += ganho - aposta
            print(f"Acertou em cheio! Você ganhou R$ {ganho:.2f}!")
        else:
            saldo -= aposta
            print(f"Você perdeu R$ {aposta:.2f}.")

    print(f"\nJogo encerrado. Saldo final: R$ {saldo:.2f}")


if __name__ == "__main__":
    jogar_roleta()

import random
import sys
from fila import Queue

from pathlib import Path # Função para importar arquivos de outros diretórios
sys.path.insert(0, str(Path(__file__).resolve().parent.parent)) # Caminho da pasta principal do projeto
from logos import logo_roleta

c_verm = '\033[91m'
c_verde = '\033[92m'
c_amarelo = '\033[93m'
c_azul = '\033[94m'
c_roxo = '\033[95m'
c_fim = '\033[0m'
f_branco = '\033[1;107m'


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
        print(f"\nSaldo atual: {c_amarelo}R$ {saldo:.2f}{c_fim}\n{100*'-'}\n")
        tipo = int(input("Apostar em: \n[1] Cor \n[2] Número\n\n Ou \n\n[3] Histórico\n[0] Sair? \n\nDigite a opção desejada: "))

        if tipo == 0:
            break
        if tipo == 3:
            resultados = historico.to_list() # Obtém os últimos números sorteados em ordem
            if resultados:
                historico_formatado = ", ".join(
                    f"{resultado['numero']} ({resultado['cor']})"
                    for resultado in resultados
                )
                print(f"{c_roxo}\n{100*'-'}\nÚltimos resultados: {historico_formatado}{c_fim}")
            else:
                print(f"{c_roxo}\n{100*'-'}\nAinda não há resultados sorteados.{c_fim}")
            continue
        if tipo not in {1, 2, 3, 0}:
            print("Opção inválida.")
            continue

        try:
            aposta = float(input(f"\n{100*'-'}\nValor da aposta: R$ "))
        except ValueError:
            print("Digite um valor numérico válido.")
            continue

        if aposta <= 0 or aposta > saldo:
            print("Valor de aposta inválido ou saldo insuficiente.")
            continue

        if tipo == 1:
            escolha_cor = (input(f"\n{100*'-'}\nEscolha a cor : \n {c_verm}[1] Vermelho{c_fim}\n {f_branco}[2] Preto{c_fim}\n {c_verde}[3] Verde{c_fim}\nDigite a opção desejada:"))
            cores = {
                "1": "vermelho",
                "2": "preto",
                "3": "verde"
            }
            if escolha_cor not in cores:
                print("Cor inválida.")
                continue
            escolha = cores[escolha_cor]
        else:
            try:
                escolha = int(input(f"\n{100*'-'}\nEscolha um número (0 a 36): "))
            except ValueError:
                print("Digite um número inteiro.")
                continue
            if escolha < 0 or escolha > 36:
                print("Número fora do intervalo de 0 a 36.")
                continue

        sorteado = random.randint(0, 36)
        cor_sorteada = cor_do_numero(sorteado)
        print(f"\n\n{c_roxo}Resultado: {sorteado} ({cor_sorteada}){c_fim}")
        resultado = {
            "numero": sorteado,
            "cor": cor_sorteada
        }
        historico.enqueue(resultado) # Adiciona o número e a cor sorteados à fila
        if historico.size() > 3: # Se a fila tiver mais de 3 elementos, remove o mais antigo
            historico.dequeue()

        if tipo == 1 and escolha == cor_sorteada:
            multiplicador = 14 if escolha == "verde" else 2
            ganho = aposta * multiplicador
            saldo += ganho - aposta
            print(f"\n\n{c_verde}Você ganhou R$ {ganho:.2f}!{c_fim}")
        elif tipo == 2 and escolha == sorteado:
            ganho = aposta * 36
            saldo += ganho - aposta
            print(f"\n\n{c_verde}Acertou em cheio! Você ganhou R$ {ganho:.2f}!{c_fim}")
        else:
            saldo -= aposta
            print(f"\n\n{c_verm}Você perdeu R$ {aposta:.2f}.{c_fim}")

    print(f"\nJogo encerrado. Saldo final: {c_amarelo}R$ {saldo:.2f}{c_fim}")


if __name__ == "__main__":
    jogar_roleta()

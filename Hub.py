import subprocess
import sys

while True:
    print('=' * 40)
    print('SEJA BEM VINDO AO CASSINO DGRV'.center(40))
    print('=' * 40)
    print('Escolha seu jogo e se divirta!!\n')
    print("1 - 21")
    print("0 - Sair")

    escolha = input("\nNúmero do jogo: ")

    if escolha == "1":
        subprocess.run([sys.executable, "main.py"], cwd="Grazi")
    elif escolha == "0":
        print("Obrigado pela presença!"+'\n'+"Volte novamente!")
        break
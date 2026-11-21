import subprocess
import sys
from logos import logo_hub

logo_hub()

while True:
    print('=' * 40)
    print('SEJA BEM VINDO AO CASSINO DGRV'.center(40))
    print('=' * 40)
    print('\n\nEscolha seu jogo e se divirta!!')
    print("1 - 21")
    print("2 - Roleta")
    print("0 - Sair")

    escolha = input("Número do jogo: ")

    if escolha == "1":
        subprocess.run([sys.executable, "main.py"], cwd="Grazi")
    elif escolha == "2":
        subprocess.run([sys.executable, "main.py"], cwd="Ricardo")
    elif escolha == "0":
        print("Obrigado pela presença!"+'\n'+"Volte novamente!")
        # break  ("exit()" encerra o programa como um todo Vini ;D)
        exit()
import subprocess
import sys
import os
from logos import logo_hub

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear') # limpa o terminal a cada interação, evitando acumular um monte de telas

while True:
    limpaTela()
    logo_hub()
    
    print('=' * 40)
    print('SEJA BEM VINDO AO CASSINO DGRV'.center(40))
    print('=' * 40)
    print('\n\nEscolha seu jogo e se divirta!!')
    print("1 - 21")
    print("2 - Roleta")
    print("3 - Bac bo")
    print("4 - Vini 1")
    print("0 - Sair")

    escolha = input("Número do jogo: ")

    if escolha == "1":
        limpaTela()
        subprocess.run([sys.executable, "main.py"], cwd="Grazi")
        input("\nAperte Enter para voltar ao menu...")
    elif escolha == "2":
        limpaTela()
        subprocess.run([sys.executable, "main.py"], cwd="Ricardo")
        input("\nAperte Enter para voltar ao menu...")
    elif escolha == "3":
        limpaTela()
        subprocess.run([sys.executable, "bac_bo.py"], cwd="Davi")
        input("\nAperte Enter para voltar ao menu...")
    elif escolha == "4":
        limpaTela()
        subprocess.run([sys.executable, "Vini_1.py"], cwd="Vini")
        input("\nAperte Enter para voltar ao menu...")
    elif escolha == "0":
        print("Obrigado pela presença!"+'\n'+"Volte novamente!")
        # break  ("exit()" encerra o programa como um todo Vini ;D)
        exit()
    else:
        print('Opção inválida! Digite 1, 2, 3, 4 ou 0')
        input('\nAperte Enter para voltar ao menu...')
import random
import os
import sys

while True:
    print("\nJOGO DE ADIVINHAÇÃO DE NÚMEROS\n\n")
    
    x = "0"
    
    while x == "0":
        print("1. Iniciar Jogo\n")
        print("2. Sair\n")
        x = input("Opção: ")
    
        os.system('clear')
    
        if x == "2":
            os.system('clear')
            print("\nJogo Finalizado!")
            break
            sys.exit()
        elif x == "1":
            print("\nDigite um Intervalo de Valores\n")
            l1 = int(input("- Digite o Limite Inferior: "))
            l2 = int(input("- Digite o Limite Superior: "))
            num_ale = random.randint(l1, l2)
    
            num_ale = int(num_ale)
            
            print(num_ale)
    
        os.system('clear')
    
        num_usu = "0"
        num_usu = int(num_usu)
        while num_usu != num_ale:
            print(f'\nEscolha um Numero Inteiro que esteja entre {l1} e {l2}\n')
            num_usu = input("Seleção: ")
            
            try:
                num_usu = int(num_usu)
    
                print(num_ale)
                if num_usu < l1 or num_usu > l2:
                    print("\nTente novamente! Chutou fora do Intervalo!\n")
                elif num_usu < num_ale:
                    print("\nTente novamente! Chutou muito Baixo!\n")
                elif num_usu > num_ale:
                    print("\nTente novamente! Chutou muito Alto!\n")
                elif num_ale == num_usu:
                    print("\nParabéns! Você Acertou!\n")
                    break
            except ValueError:
                print("\nPor favor, insira um número inteiro válido!\n")
    
    
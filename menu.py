from alunos import cadastrar_aluno
from submenu import submenu


def menu():
    print("\n ---- Controle Esportes ----")
    print(" 1. Cadastrar aluno")
    print(" 2. Relatórios")
    print(" 3. Sair")

    opcao = int(input("\n Digite uma opção: "))

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        submenu()
    elif opcao == 3:
        print(" Programa finalizado")
        exit()
    else:
        print(" Opção inválida")

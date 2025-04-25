import alunos
import relatorios


def submenu():
    print("\n --- Relatórios ---")
    print(" 1. Alunos")
    print(" 2. Modalidades")
    print(" 3. Idades")
    print(" 4. Sair")
    opcao = int(input(" Digite a opção desejada: "))

    if opcao == 1:
        alunos.listar_alunos()
    elif opcao == 2:
        relatorios.buscar_modalidade()
    elif opcao == 3:
        relatorios.buscar_idade()
    elif opcao == 4:
        exit

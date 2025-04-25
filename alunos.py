def cadastrar_aluno():
    nome = input(" Digite o nome do aluno: ")
    idade = int(input(" Digite a idade: "))
    modalidade = str(input(" Digite a modalidade do aluno:"))

    with open("inscricoes_aluno.txt", "a") as arquivo:
        linha = f"{nome},{idade},{modalidade}\n"
        arquivo.write(linha)
    print(" Inscrição cadastrada com sucesso!")


def listar_alunos():
    with open("inscricoes_aluno.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            print(
                f" Aluno: {dados[0].capitalize()} | Idade: {dados[1]} | Modalidade: {dados[2].capitalize()}"
            )

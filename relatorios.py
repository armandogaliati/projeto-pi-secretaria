def buscar_modalidade():
    buscar_m = input(" Digite o que voce quer buscar: ")

    with open("inscricoes_aluno.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            if dados[2] == buscar_m:
                print(f"\n {dados[0]} está cadastrado em {dados[2]} ")


def buscar_idade():
    idade = 0
    contador = 0
    with open("inscricoes_aluno.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            idade_temp = int(dados[1])
            idade = idade + idade_temp
            contador += 1
        media = idade / contador
        print(f"\n A média de idade entre os alunos é de {media:.2f} anos!")

print("Corretor de Gabarito\n")
print("Cadastro da Prova")

total_questoes = int(input("Quantas questões tem a prova? "))
nota_maxima = float(input("Quanto vale a prova? "))

print("\n Digite a reposta correta para cada questão (A, B, C, D, E):")

# essa é a primeira funcao recursiva pra recber o gabarito
gabarito = [] #aqui vai receber o gabarito e deixar imutavel
def inserir_gabarito(questao, total_questoes, gabarito):
    if questao > total_questoes:
        return
    resposta = input(f"Questão {questao}: ")
    #vou usar strip para tirar espaco e upper pra deixar maiusculo logo, assim fica mais facil comparar
    gabarito.append(resposta.strip().upper())
    inserir_gabarito(questao + 1, total_questoes, gabarito)

inserir_gabarito(1, total_questoes, gabarito)




print("\nCadastro dos Alunos e Respostas")



lista_alunos_respostas = [] #aqui vai receber os alunos e respostas e deixar imutavel

#agora que ja pegamos o gabarito da prova vamos pegar os alunos e respostas
def inserir_alunos_respostas(lista_alunos_respostas, total_questoes):
    nome = input("Digite o nome do aluno ou 'parar' para terminar:")

    #remove logo os espcos e deixa minusculo
    if nome.strip().lower() == 'parar':
        return

    print(f"Respostas do aluno {nome}:")
    
    respostas = []

    print("\n Digite a reposta do aluno para cada questão (A, B, C, D, E):")
    #vai precisar fazer uma funcao interna recursiva para pegar as respostas segue a mesma ideia do ggabarito
    def inserir_respostas(questao_atual, total_questoes, respostas):
        if questao_atual > total_questoes:
            return
        reposta_aluno = input(f"Questão {questao_atual}: ")
        respostas.append(reposta_aluno.strip().upper())
        inserir_respostas(questao_atual + 1, total_questoes, respostas)

    inserir_respostas(1, total_questoes, respostas)

    #agora so cria uma lista geral com os nomes e respostas
    lista_alunos_respostas.append({
        'nome': nome,
        'respostas': respostas
    })

    return inserir_alunos_respostas(lista_alunos_respostas, total_questoes)

inserir_alunos_respostas(lista_alunos_respostas, total_questoes)

print("\nGabarito e Respostas dos Alunos:")
print(f"Gabarito: {gabarito}")
for aluno in lista_alunos_respostas:
    print(f"Aluno: {aluno['nome']}\nRespostas: {aluno['respostas']}")


    



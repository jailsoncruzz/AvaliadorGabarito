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
#primeira funcao com closure
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


valor_questao = lambda nota_maxima, total_questoes: nota_maxima / total_questoes

#definir logo uma funcao pra calcular a nota pq vou passar ela na hora de avaliar
def calcular_nota(valor_questao, acertos):
    return valor_questao * acertos

#funcao de compar respota
def avaliar(lista_alunos_respostas, gabarito):

    def avaliar_aluno(aluno):
         #pra ficar mais claro eu vou usar um list comprehension mas como isso cria uma nova lista com acertos e uso o len() para mostrar o tamnho que é a mesma coisa que contar os acertos
        acertos = len([i for i in range(len(gabarito)) if aluno['respostas'][i] == gabarito[i]])
        #e aqui é a mesma coisa
        erros = len([i for i in range(len(gabarito)) if aluno['respostas'][i] != gabarito[i]])
        return {
            'nome': aluno['nome'],
            'acertos': acertos,
            'erros': erros
        }
    
    #ai quando chega aqui a gente usa um list() pra criar uma lista e o usa o map pra fazer com que a funcao avaliar_aluno rode cada interacao de lista_alunos_respostas
    #e aqui tbm a gente ja usa alta ordem pq passa avaliar_aluno para map
    return list(map(avaliar_aluno, lista_alunos_respostas))


avaliacoes = avaliar(lista_alunos_respostas, gabarito)



#aqui é o final já uma funcao geral pra mostrar os resultados
def resultado_final():
    #usando a funcao lmbda
    valor_q = valor_questao(nota_maxima, total_questoes)


    #aqui uma recursao para mostrar cada aluno sem usar loop
    def mostrar_resultado(i=0):
        if i >= len(avaliacoes):
            return
        
        aluno_avaliado = avaliacoes[i]
        aluno_respostas = lista_alunos_respostas[i]['respostas']
        
        #chama o calculo da nota
        nota_aluno = calcular_nota(valor_q, aluno_avaliado['acertos'])

        print("_________________")
        print(f"\nNome do Aluno: {aluno_avaliado['nome']}")

        #agora aqui já é outra recursao mas pra mostrar a respostas do aluno atual
        def mostrar_respostas(j=0):
            if j >= total_questoes:
                return
            
            
            print(f"\nQuestão {j+1}:")
            print(f"Resposta do aluno: {aluno_respostas[j]}")
            print(f"Resposta correta: {gabarito[j]}")

    
            mostrar_respostas(j + 1)
            
        #aqui comeca mostrar as respostas
        mostrar_respostas()
        
        print(f"\nAcertos: {aluno_avaliado['acertos']}")
        print(f"Erros: {aluno_avaliado['erros']}")
        print(f"Nota final: {nota_aluno}")

        mostrar_resultado(i + 1)

    #aqui comeca a funcao de mostrar o resultado
    mostrar_resultado()

resultado_final()

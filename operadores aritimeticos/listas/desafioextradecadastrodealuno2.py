alunos = {}

opcao = -1

while (opcao != 0):

    opcao = int(input("o que desejafazer?\n" 
                    "opção 1: cadastrar aluno \n"
                    "opção 2: exibir media \n"
                    "opção 3: exibir aluno com maior nota \n"
                    "opção 0: sair \n\n"
                    "opção -> "))
    
    if opcao == 1:

        key_aluno = len(alunos) + 1

        values_alunos = {}

        nome_aluno = input("informe o nome do aluno -> ")

        idade_aluno = int(input("informe a idade do aluno -> "))

        nota_aluno = float(input( "informe a nota do aluno -> "))
                                 
        values_alunos.update({"nome": nome_aluno,
                              "idade": idade_aluno,
                              "nota": nota_aluno})

        alunos.update({key_aluno: values_alunos})

        print()

    elif opcao == 2:

        soma_notas = 0

        for aluno in alunos.values():

            soma_notas += aluno0["nota"]

        print(f"a media das notas é {soma_notas / len(alunos)} \n")

    elif opcao == 3:

        maior = 0

        id = 0

        for id, aluno in alunos.items():

            if aluno["nota"] > maior:
               
               maior = aluno["nota"]
               
               id_aluno = id

        print(f"o aluno com a maior nota é {alunos[id_aluno] ["nome"]} | nota {maior}")

    else:

        print("\n opcao invalida \n")
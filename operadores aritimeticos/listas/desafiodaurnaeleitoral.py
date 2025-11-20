candidatos = {}

opcao = -1

while (opcao != 0):

    opcao = int(input("o que desejafazer?\n" 
                    "opção 1: cadastrar candidato \n"
                    "opção 2: exibir numero \n"
                    "opção 3: exibir votos validos \n"
                    "opcao 4: exibir votos nulos \n"
                    "opcão 5: tratar de forma amigavel, sem encerrar \n"
                    "opcão 6: exibir colocação \n"
                    "opção 0: sair \n\n"
                    "opção -> "))
    
    if opcao == 1:

        Carlos_candidato = len(candidatos) + 1

        values_candidatos = {}

        nome_candidatos = input("informe o nome do candidato -> ")

        Numero_candidato = int(input("informe o numero do candidato -> "))

                                 
        values_candidatos.update({"nome": nome_candidatos,
                              "numero": Numero_candidato })
        
        candidatos.update({Carlos_candidato: values_candidatos})

        minha_lista = ["carlos", "vera", "marcos" "beti", "didi"]

        minha_tupla = tuple(minha_lista)

        print(f"Lista original: {minha_lista}")

        print()

    elif opcao == 2:

        soma_votos = 0

        for candidatos in candidatos.values():

            soma_votos += candidato["voto"]
        print(f"a media dos votos é {soma_voto / len(candidatos)} \n")

    elif opcao == 3:

        maior = 0

        id = 0

        for id, candidato in candidatos.items():

            if candidato["voto"] > maior: 
               
               maior = candidato["voto"]
               
               id_candidato = id

               colocacão_candidato = float(input( "informe a colocacão -> "))

        print(f"o candidato com o maior voto é {candidatos ["id_candidato"] ["nome"]} | voto {maior}")

    else:

        print("\n opcao invalida \n")

    
from sistema import Sistema

def main():
    sistema  =  receber_dados()

    sistema.printar_dados()

    seguro,programa = sistema.alocar_recurso()

    while(seguro):
        sistema.printar_dados()
        print("programa " + str(programa + 1) + " executou")
        input("aperte enter pra continuar")
        
        seguro,programa = sistema.alocar_recurso()

    if sistema.algoritmo_terminou():
        print("progamas em estado seguro")
    else :
        print("programas em estado inseguro")

def receber_dados():
    quantidade_programas = int(input("qual a quantidade de programas?"))
    quantidade_tipo_recursos = int(input("qual a quantidade de tipos recursos?"))

    flag = True

    while flag:
        recursos_totais_str = input("digite a matriz de recursos totais(Ex: 1,2,3,4): ").split(",")
        if len(recursos_totais_str) == quantidade_tipo_recursos:
            flag = False
        else:
            print("digite separado por virgulas e/ou com {} recursos".format(quantidade_tipo_recursos))
    recursos_totais = [int(i) for i in recursos_totais_str]

    flag = True

    while flag:
        recursos_disponiveis_str = input("digite a matriz de recursos disponiveis(Ex: 1,2,3,4): ").split(",")
        if len(recursos_disponiveis_str) == quantidade_tipo_recursos:
            flag = False
        else:
            print("digite separado por virgulas e/ou com {} recursos".format(quantidade_tipo_recursos))

    recursos_disponiveis = [int(i) for i in recursos_disponiveis_str]

    matriz_alocados = []
    matriz_requisitos = []
    for i in range(quantidade_programas):
        flag = True

        while flag:
            recursos_alocados_programa = input("digite os recursos alocados do programa  {} (Ex: 1,2,3,4): ".format(i+1)).split(",")
            if len(recursos_alocados_programa) == quantidade_tipo_recursos:
                flag = False
            else:
                print("digite separado por virgulas e/ou com {} recursos".format(quantidade_tipo_recursos))
        matriz_alocados.append([int(i) for i in recursos_alocados_programa])

        flag = True

        while flag:
            recursos_requisitados_programa = input("digite os recursos requisitados do programa  {} (Ex: 1,2,3,4): ".format(i+1)).split(",")
            if len(recursos_requisitados_programa) == quantidade_tipo_recursos:
                flag = False
            else:
                print("digite separado por virgulas e/ou com {} recursos".format(quantidade_tipo_recursos))
        matriz_requisitos.append([int(i) for i in recursos_requisitados_programa])
        print(matriz_alocados)
        print(matriz_requisitos)
        print(recursos_totais)
        print(recursos_disponiveis)

    return Sistema(recursos_totais,recursos_disponiveis,matriz_alocados,matriz_requisitos)

        
    
if __name__ == "__main__":
    main()
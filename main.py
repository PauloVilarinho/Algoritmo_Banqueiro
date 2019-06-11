from sistema import Sistema

def main():
    sistema = Sistema([6,4,7,6],
                    [3,0,1,2],
                    [[1,2,2,1],[1,1,3,3],[1,1,1,0]],
                    [[2,1,0,1],[0,1,0,1],[0,0,4,0]])

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

if __name__ == "__main__":
    main()
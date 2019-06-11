from utils import *

class Sistema:

    def __init__(self,recursos_totais,recursos_disponiveis,matriz_alocados,matriz_requisicao):
        self.recursos_totais = recursos_totais
        self.recursos_disponiveis = recursos_disponiveis
        self.matriz_alocados = matriz_alocados
        self.matriz_requisicao = matriz_requisicao
        self.quantidade_recursos = len(recursos_disponiveis)

    def printar_dados(self):
        print("recursos totais:")
        print(self.recursos_totais)
        print("recursos disponiveis:")
        print(self.recursos_disponiveis)
        print("matriz de recursos alocados:")
        print(printar_matriz(self.matriz_alocados))
        print("matriz de recursos requisitados:")
        print(printar_matriz(self.matriz_requisicao))

    def alocar_recurso(self):
        vetor_comparativo = [0]*self.quantidade_recursos

        for programa in range(len(self.matriz_requisicao)):
            for recurso in range(self.quantidade_recursos):
                if self.matriz_requisicao[programa][recurso] > self.recursos_disponiveis[recurso]:
                    break
                elif recurso == self.quantidade_recursos -1 and self.matriz_requisicao[programa] != vetor_comparativo :
                    self.realocar_recursos(programa)
                    return True,programa
        return False,programa

    
    def realocar_recursos(self,programa):
        for recurso in range(self.quantidade_recursos):
            self.recursos_disponiveis[recurso] += self.matriz_alocados[programa][recurso] 
            self.matriz_alocados[programa][recurso] = 0
            self.matriz_requisicao[programa][recurso] = 0

    def algoritmo_terminou(self):
        for programa in range(len(self.matriz_requisicao)):
            for recurso in range(self.quantidade_recursos):
                if self.matriz_requisicao[programa][recurso] != 0 :
                    return False
        return True

    

class Estado():

    def __init__(self, missionarios_esq, missionarios_dir, canibais_esq, canibais_dir, lado_rio):
 
        self.missionarios_esq = missionarios_esq
        self.missionarios_dir = missionarios_dir
        self.canibais_esq = canibais_esq
        self.canibais_dir = canibais_dir
        self.lado_rio = lado_rio
        self.pai = None
        self.filhos = []


    def __str__(self):
        return "Missionários - ESQUERDA: {} | Canibais - ESQUERDA: {} <-----RIO------> Missionários - DIREITA: {} | Canibais - DIREITA: {}".format(self.missionarios_esq, self.canibais_esq, self.canibais_dir,self.missionarios_dir)

    def estado_valido(self):


        if ((self.missionarios_esq < 0) or (self.missionarios_dir < 0)
            or (self.canibais_esq < 0) or (self.canibais_dir < 0)):
            return False

        return ((self.missionarios_esq == 0 or self.missionarios_esq >= self.canibais_esq) and
                (self.missionarios_dir == 0 or self.missionarios_dir >= self.canibais_dir))


    def estado_final(self):

        resultado_esq = self.missionarios_esq == self.canibais_esq == 0
        resultado_dir = self.missionarios_dir == self.canibais_dir == 3
        return resultado_esq and resultado_dir

    def gerar_filhos(self):


        novo_lado_rio = 'dir' if self.lado_rio == 'esq' else 'esq'
        movimentos = [
            {'missionarios': 2, 'canibais': 0},
            {'missionarios': 1, 'canibais': 0},
            {'missionarios': 1, 'canibais': 1},
            {'missionarios': 0, 'canibais': 1},
            {'missionarios': 0, 'canibais': 2},
        ]

        for movimento in movimentos:
            if self.lado_rio == 'esq':

                missionarios_esq = self.missionarios_esq - movimento['missionarios']
                missionarios_dir = self.missionarios_dir + movimento['missionarios']
                canibais_esq = self.canibais_esq - movimento['canibais']
                canibais_dir = self.canibais_dir + movimento['canibais']
            else:

                missionarios_dir = self.missionarios_dir - movimento['missionarios']
                missionarios_esq = self.missionarios_esq + movimento['missionarios']
                canibais_dir = self.canibais_dir - movimento['canibais']
                canibais_esq = self.canibais_esq + movimento['canibais']

            filho = Estado(missionarios_esq, missionarios_dir, canibais_esq,
                           canibais_dir, novo_lado_rio)
            filho.pai = self
            if filho.estado_valido():
                self.filhos.append(filho)


class Missionarios_Canibais():

    def __init__(self):

        self.fila_execucao = [Estado(3, 0, 3, 0, 'esq')]
        self.solucao = None

    def gerar_solucao(self):

        for elemento in self.fila_execucao:
            if elemento.estado_final():

                self.solucao = [elemento]
                while elemento.pai:
                    self.solucao.insert(0, elemento.pai)
                    elemento = elemento.pai
                break;
            elemento.gerar_filhos()
            self.fila_execucao.extend(elemento.filhos)


def main():
    problema = Missionarios_Canibais()
    problema.gerar_solucao()
    for estado in problema.solucao:
        print estado

if __name__ == '__main__':
    main()
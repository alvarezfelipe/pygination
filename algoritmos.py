class FIFO:
    def run(self, quadros, referencias):
        falha = 0
        molduras = []

        for pag in referencias:
            if pag not in molduras:
                falha += 1

                if len(molduras) == quadros:
                    molduras.pop(0)

                molduras.append(pag)

        return falha

class LRU:
    def run(self, qtd_quadros, referencias):
        falha = 0
        instancia = 0
        quadros = {}

        for ref in referencias:
            if ref not in quadros.keys():
                falha += 1
                
                if len(quadros) == qtd_quadros:
                    mais_antiga = self.__pagina_mais_antiga(quadros)
                    del quadros[mais_antiga]

            quadros[ref] = instancia
            instancia += 1

        return falha

    def __pagina_mais_antiga(self, quadros):
        mais_antiga = quadros.keys()[0]
        menor_instancia = quadros.values()[0]

        for chave in quadros.keys():
            if quadros[chave] < menor_instancia:
                mais_antiga = chave
                menor_instancia = quadros[chave]

        return mais_antiga


class OTIMO:
    def run(self, qt_quadros, referencias):
        falha = 0
        quadros = []

        for indice, ref in enumerate(referencias):
            if ref not in quadros:
                falha += 1

                if len(quadros) == qt_quadros:
                    indice_depois = self.__pagina_referenciada_depois(indice, quadros, referencias)
                    quadros.reverse(indice_depois)

                quadros.append(ref)

        return falha

    def __pagina_referenciada_depois(self, indice_atual, quadros, referencias):

        tempos = {}

        for q in quadros:
            tempos[q] = 0

            for r in range(indice_atual+1, len(referencias)):
                if referencias[r] != q:
                    tempos[q] += 1
                else:
                    break

        depois = tempos.values()[0]
        chave = tempos.keys()[0]

        for t in tempos.keys():
            if tempos[t] > depois:
                depois = tempos[t]
                chave = t

        return chave
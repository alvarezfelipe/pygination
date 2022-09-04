def FIFO(lista, quadros):
    memoria = []
    faltas = 0
    index = 0

    for x in range(len(lista)):
        if lista[x] not in memoria and len(memoria) < quadros:
            memoria.insert(x, lista[x])
            faltas += 1
        elif lista[x] not in memoria and len(memoria) >= quadros:
            memoria[index] = lista[x]
            faltas += 1
            index += 1
        if index == quadros:
            index = 0
    return faltas

def OTIMO(lista, quadros):
    memoria = []
    existe = [0] * quadros
    faltas = 0

    for x in range(len(lista)):
        if lista[x] not in memoria and len(memoria) < quadros:
            memoria.insert(x, lista[x])
            faltas += 1
        elif lista[x] not in memoria and len(memoria) >= quadros:
            for y in range (x, len(lista)):
                if lista[y] in memoria and sum(existe) < quadros:
                    existe[memoria.index(lista[y])] = 1

                if sum(existe) == quadros:
                    memoria[memoria.index(lista[y])] = lista[x]
                    faltas += 1
                    existe = [0] * quadros
                    break
                elif sum(existe) < quadros and y == len(lista)-1:
                    for z in range(0, quadros):
                        if existe[z] != 1:
                            memoria[z] = lista[x]
                            faltas += 1
                            existe = [0] * quadros
                            break
    return faltas

def LRU(lista, quadros):
    memoria = []
    lista_auxiliar = []
    existe = [0] * quadros
    faltas = 0

    for x in range(len(lista)):
        if lista[x] not in memoria and len(memoria) < quadros:
            memoria.insert(x,lista[x])
            faltas += 1
        elif lista[x] not in memoria and len(memoria) >= quadros:
            lista_auxiliar = lista.copy()
            lista_auxiliar.reverse()

            for y in range(len(lista_auxiliar) - x, len(lista_auxiliar)):
                if lista_auxiliar[y] in memoria and sum(existe) < quadros:
                    existe[memoria.index(lista_auxiliar[y])] = 1
                if sum(existe) == quadros:
                    memoria[memoria.index(lista_auxiliar[y])] = lista[x]
                    faltas += 1
                    existe = [0] * quadros
                    break
                elif sum(existe) < quadros and y == len(lista)-1:
                    for z in range (0,quadros):
                        if existe[z] != 1:
                            memoria[z] = lista[x]
                            faltas += 1
                            existe = [0] * quadros
                            break
    return faltas
def dijkstra(grafo, a, z):
    
    #Determina cual es el camino mas cortoentre 'a' y 'z' los cuales a,z son llamados nodos,
    # Grafo = quien contiene por asi decir los caminos.
    
    inf = 0#Infinito
    for letra in grafo:
        for v,w in grafo[letra]:
            inf += w
            
    # Inicializacion de estructuras auxiliares:
    #  L: diccionario vertice -> etiqueta
    #  S: conjunto de vertices con etiquetas temporales
    #  A: vertice -> vertice previo (en camino longitud minima)
    
    L = dict([(letra, inf) for letra in grafo]) #crear un grafo {}
    L[a] = 0
    S = set([letra for letra in grafo]) #crear un grafo {}
    A = {}
    
    # Funcion auxiliar, dado un vertice retorna su etiqueta
    # se utiliza para encontrar el vertice the etiqueta minima
    
    def regresar_minimo(v):
        
        return L[v]
    
    # Iteracion principal del algoritmo de Dijkstra
    while z in S:
        letra = min(S, key=regresar_minimo)#min es el minimo
        S.discard(letra)
        for v, w in grafo[letra]:
            if v in S:
                if L[letra] + w < L[v]:
                    L[v] = L[letra] + w
                    A[v] = letra
                    
    # Reconstruccion del camino de longitud minima
    P = []
    u = z
    while letra != a:
        P.append(letra)
        #print(P)
        letra = A[letra]
        #print(letra)
    P.append('a')
    P.reverse()

    return P
                    

grafo = {'a' : [('e',14),('c',9),('b',7)],
         'b':[('c',10),('d',15)],
         'c':[('e',2),('d',11)],
         'd':[('f',6)],
         'e':[('f',9)],}


def main():
    
    p =  dijkstra(grafo, 'a', 'd')
    print (' nodos con distancia mas corta hasta dicho punto: ', p)
    
if __name__ == '__main__':
    main()

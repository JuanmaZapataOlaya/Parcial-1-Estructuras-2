import networkx as graf
import random

Col = graf.Graph()

nodos = ["antioquia", "cordoba", "choco", "caldas", "santander"]
Col.add_nodes_from(nodos)

valoresRandom = [random.randint(1, 10) for _ in range(8)]

aristas = [("antioquia", "santander", {"valor": valoresRandom[0]}),
           ("antioquia", "caldas", {"valor": valoresRandom[1]}),
           ("antioquia", "choco", {"valor": valoresRandom[2]}),
           ("antioquia", "cordoba", {"valor": valoresRandom[3]}),
           ("choco", "caldas", {"valor": valoresRandom[4]}),
           ("cordoba", "choco", {"valor": valoresRandom[5]}),
           ("santander", "cordoba", {"valor": valoresRandom[6]}),
           ("santander", "caldas", {"valor": valoresRandom[7]})]
Col.add_edges_from(aristas)

#En visual no funciona pero en jupiter si
graf.draw(Col, with_labels=True)

def valor_de_conexion(grafo, nodo1, nodo2):
    if grafo.has_edge(nodo1, nodo2):
        return grafo[nodo1][nodo2]["valor"]
    else:
        return None

def conquistar(grafo, territorio_actual, recursos_disponibles, memo, camino_actual):
    if (territorio_actual, recursos_disponibles) in memo:
        return memo[(territorio_actual, recursos_disponibles)]
    
    if recursos_disponibles == 0:
        return camino_actual

    caminos_posibles = []
    
    for territorio_siguiente in grafo.neighbors(territorio_actual):
        valor_conexion_territorio = valor_de_conexion(grafo, territorio_actual, territorio_siguiente)
        
        if valor_conexion_territorio is not None and recursos_disponibles >= valor_conexion_territorio:
            recursos_restantes = recursos_disponibles - valor_conexion_territorio
            nuevo_camino = camino_actual + [territorio_siguiente]
            caminos_posibles.append(conquistar(grafo, territorio_siguiente, recursos_restantes, memo, nuevo_camino))
    
    if caminos_posibles:
        mejor_camino = max(caminos_posibles, key=len)
    else:
        mejor_camino = camino_actual
        
    memo[(territorio_actual, recursos_disponibles)] = mejor_camino
    
    return mejor_camino

def juego_estrategia_conquista(grafo, presupuesto_inicial):
    memo = {}
    camino_optimo = conquistar(grafo, "antioquia", presupuesto_inicial, memo, ["antioquia"])
    return camino_optimo

presupuesto_inicial = 10
camino_optimo = juego_estrategia_conquista(Col, presupuesto_inicial)
print("")
print("Resultados Conquista")
print("Camino óptimo:", camino_optimo)
print("")

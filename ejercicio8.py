import heapq

# Crear un diccionario para almacenar los planetas y sus conexiones
graph = {
    "Tierra": {"Knowhere": 20, "Zen-Whoberi": 10, "Vomir": 30},
    "Knowhere": {"Tierra": 20, "Zen-Whoberi": 15, "Titán": 25},
    "Zen-Whoberi": {"Tierra": 10, "Knowhere": 15, "Nidavellir": 5},
    "Vomir": {"Tierra": 30, "Titán": 35, "Nidavellir": 20},
    "Titán": {"Knowhere": 25, "Vomir": 35, "Nidavellir": 40},
    "Nidavellir": {"Zen-Whoberi": 5, "Vomir": 20, "Titán": 40},
    "Nameplanet1": {"Nameplanet2":value, "Nameplanet3":value},
    "Nameplanet2": {"Nameplanet3":value, "Nameplanet4":value},
    "Nameplanet3": {"Nameplanet5":value, "Nameplanet6":value},
    "Nameplanet4": {"Nameplanet7":value, "Nameplanet8":value},
    "Nameplanet5": {"Nameplanet9":value, "Nameplanet10":value},
    "Nameplanet6": {"Nameplanet11":value, "Nameplanet12":value},
    "Nameplanet7": {"Nameplanet13":value, "Nameplanet14":value},
}

# Función para encontrar el árbol de expansión mínima
def prim(graph):
    mst = {}
    visited = set()
    heap = []
    start = list(graph.keys())[0]
    visited.add(start)
    for neighbour, cost in graph[start].items():
        heap.append((cost, start, neighbour))
    heapq.heapify(heap)

    while heap:
        cost, frm, to = heapq.heappop(heap)
        if to not in visited:
            visited.add(to)
            mst[frm] = (to, cost)
            for neighbour, cost in graph[to].items():
                if neighbour not in visited:
                    heap.append((cost, to, neighbour))
                    heapq.heapify(heap)
    return mst

print("Árbol de expansión mínima:", prim(graph))
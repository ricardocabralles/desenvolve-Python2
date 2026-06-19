"""Módulo de controle do jogador e lógica de movimentação."""
import sys
sys.setrecursionlimit(5000) # Permite que a IA resolva labirintos grandes e complexos
def iniciar_jogador():
    """Define posição inicial e pontuação."""
    return {"pos": [1, 1], "pontos": 0}

def resolver_recursivo(mapa, x, y, visitados=None):
    """Função recursiva para encontrar a saída (Backtracking)."""
    if visitados is None:
        visitados = set()

    if mapa[x][y] == 2: # Caso Base: Saída encontrada
        return [[x, y]]

    visitados.add((x, y))
    direcoes = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for nx, ny in direcoes:
        # Verifica limites do mapa e se não é parede ou já visitado
        if 0 <= nx < len(mapa) and 0 <= ny < len(mapa[0]):
            if mapa[nx][ny] != 1 and (nx, ny) not in visitados:
                caminho = resolver_recursivo(mapa, nx, ny, visitados)
                if caminho:
                    return [[x, y]] + caminho
    return None
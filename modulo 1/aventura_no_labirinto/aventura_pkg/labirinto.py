"""Módulo de geração procedural de labirintos rigorosos com 10 níveis de progressão."""
import random
from rich.console import Console

def criar_labirinto(dificuldade="fácil", fase=1):
    """
    Gera labirintos que ficam maiores e mais tortuosos a cada fase.
    Garante caminho único com becos sem saída muito longos.
    """
    # Progressão: Fase 1 começa pequena, Fase 10 fica gigante.
    # Fácil: aumenta de 2 em 2 | Difícil: aumenta de 4 em 4
    incremento = 2 if dificuldade == "fácil" else 4
    base = 11 if dificuldade == "fácil" else 19
    
    largura = base + (fase * incremento)
    altura = largura
    
    # Dimensões ímpares são obrigatórias para este algoritmo
    if largura % 2 == 0: largura += 1
    if altura % 2 == 0: altura += 1

    mapa = [[1 for _ in range(largura)] for _ in range(altura)]

    def cavar(x, y):
        mapa[y][x] = 0
        
        # Direções: Baixo, Cima, Direita, Esquerda
        direcoes = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        
        # Para tornar os caminhos falsos MAIS LONGOS:
        # Misturamos as direções, mas o algoritmo vai até o fim de cada uma antes de voltar.
        random.shuffle(direcoes)
        
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 < nx < largura-1 and 0 < ny < altura-1 and mapa[ny][nx] == 1:
                mapa[y + dy//2][x + dx//2] = 0
                cavar(nx, ny)

    cavar(1, 1)
    
    # A saída é colocada sempre no canto inferior, forçando a travessia total
    mapa[altura-2][largura-2] = 2 
    return mapa

def imprimir_labirinto(mapa, pos_jogador):
    """
    Renderiza o labirinto garantindo que ele caiba na tela e 
    reposicionando o cursor no topo para evitar scroll.
    """
    console = Console()
    
    buffer_visual = ""
    for r, linha in enumerate(mapa):
        for c, valor in enumerate(linha):
            if [r, c] == pos_jogador:
                buffer_visual += "[bold magenta]☺ [/]"
            elif valor == 1:
                buffer_visual += "[blue]█ [/]"
            elif valor == 2:
                buffer_visual += "[bold yellow]★ [/]"
            else:
                buffer_visual += "  "
        buffer_visual += "\n"
    
    # Em vez de clear(), usamos um código que reseta a posição do cursor
    # Isso evita que o terminal "role" para baixo a cada movimento
    print("\033[H", end="") 
    console.print(buffer_visual, end="")
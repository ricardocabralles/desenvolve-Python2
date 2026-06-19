"""Módulo de som estável usando Pygame e Streaming via RAM."""
import pygame
import urllib.request
import io

# Inicializa o mixer de áudio
pygame.mixer.init()

def iniciar_musica(fase):
    """Lê o MP3 da internet e toca sem salvar no disco."""
    # Links diretos e estáveis do Archive.org e KHInsider
    links = {
        1: "https://archive.org/download/dragon-ball-z-p8rylb/DJ%20Skulldiner%20-%20Dragon%20Ball%20Z%20-%2002%20Cha%20La%20Head%20Cha%20La.mp3",
        2: "https://archive.org/download/super-mario-bros-the-great-mission-to-rescue-princess-peach-original-soudtrack/5%20The%20Kames%20Scheme.mp3",
        3: "https://archive.org/download/DBGTOST/01PrologueSubtitle.mp3",
        4: "https://archive.org/download/yugiohforbiddenmemoriessoundtrack/01%20Main%20Menu.mp3",
        5: "https://archive.org/download/trilha-sonora-de-hercules-1997/14%20A%20profecia.mp3",
        6: "https://archive.org/download/yugiohforbiddenmemoriessoundtrack/06%203D%20Duel%20%28Egypt%29.mp3",
        7: "https://archive.org/download/yugiohforbiddenmemoriessoundtrack/10%20Heishin%27s%20Invasion.mp3",
        8: "https://archive.org/download/yugiohforbiddenmemoriessoundtrack/11%20Heishin%20Millennium%20Puzzle%20Confrontation.mp3",
        9: "https://archive.org/download/yugiohforbiddenmemoriessoundtrack/12%20Tournament%20Announcement.mp3",
        10: "https://archive.org/download/yugiohforbiddenmemoriessoundtrack/43%203D%20Duel%20%28Final%20Duel%29.mp3"
    }
    
    url = links.get(fase)
    if url:
        try:
            # Para a música anterior antes de carregar a nova
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

            # Faz o download temporário para a memória RAM
            with urllib.request.urlopen(url) as response:
                musica_data = io.BytesIO(response.read())
                pygame.mixer.music.load(musica_data)
                pygame.mixer.music.play(-1) # -1 toca em loop infinito
        except Exception as e:
            print(f"\n[Aviso] Não foi possível carregar o áudio da fase {fase}: {e}")

def parar_musica():
    """Para o áudio imediatamente."""
    pygame.mixer.music.stop()
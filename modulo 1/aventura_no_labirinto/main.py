from aventura_pkg import som
import argparse
import time
from pynput import keyboard
from aventura_pkg import labirinto, jogador, utils

def iniciar_fase(nome, dificuldade, modo_ia, fase_numero):
    # Limpa tudo antes de gerar a nova fase
    from rich.console import Console
    Console().clear() 
    # CHAMA A MÚSICA DA FASE AQUI
    som.iniciar_musica(fase_numero) 
    
    mapa = labirinto.criar_labirinto(dificuldade, fase_numero)
    dados = jogador.iniciar_jogador()
    mapa = labirinto.criar_labirinto(dificuldade, fase_numero)
    dados = jogador.iniciar_jogador()
    pos = dados["pos"]
    
    if modo_ia:
        print(f"\n--- FASE {fase_numero}: IA RESOLVENDO ---")
        caminho = jogador.resolver_recursivo(mapa, pos[0], pos[1])
        if caminho:
            for passo in caminho:
                labirinto.imprimir_labirinto(mapa, passo)
                time.sleep(0.2)
            return True
        return False
    else:
        print(f"\n--- FASE {fase_numero}: SUA VEZ, {nome}! ---")
        venceu = [False] # Usamos lista para alterar dentro do escopo do pynput

        def ao_pressionar(tecla):
            nova_pos = list(pos)
            try:
                if tecla == keyboard.Key.up: nova_pos[0] -= 1
                elif tecla == keyboard.Key.down: nova_pos[0] += 1
                elif tecla == keyboard.Key.left: nova_pos[1] -= 1
                elif tecla == keyboard.Key.right: nova_pos[1] += 1
                elif tecla == keyboard.Key.esc: return False
                
                if 0 <= nova_pos[0] < len(mapa) and 0 <= nova_pos[1] < len(mapa[0]):
                    if mapa[nova_pos[0]][nova_pos[1]] != 1:
                        pos[:] = nova_pos
                
                labirinto.imprimir_labirinto(mapa, pos)
                if mapa[pos[0]][pos[1]] == 2:
                    venceu[0] = True
                    return False
            except: pass

        with keyboard.Listener(on_press=ao_pressionar) as listener:
            labirinto.imprimir_labirinto(mapa, pos)
            listener.join()
        return venceu[0]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, required=True)
    # Outros argumentos CLI mantidos para cumprir o requisito do professor
    parser.add_argument("--difficulty", default="fácil")
    parser.add_argument("--color", default="cyan")
    parser.add_argument("--disable-sound", action="store_true")
    parser.add_argument("--auto-solve", action="store_true")
    args = parser.parse_args()

    while True:
        print(f"\nOlá {args.name}! O que deseja fazer?")
        print("1. Iniciar Jogo (Manual)")
        print("2. Modo Assistido (IA resolvendo)")
        print("3. Instruções")
        print("4. Sair")
        
        escolha = input("Escolha: ")
        
        match escolha:
            case "1" | "2":
                modo_ia = (escolha == "2")
                dif = input("Escolha a dificuldade (1. Fácil / 2. Difícil): ")
                dificuldade = "difícil" if dif == "2" else "fácil"
                
                fase = 1
                fase = 1
                while fase <= 10: # Agora o jogo tem 10 níveis!
                    sucesso = iniciar_fase(args.name, dificuldade, modo_ia, fase)
                    if sucesso:
                        print(f"\n🔥 EXCELENTE! Fase {fase} concluída!")
                        fase += 1
                        time.sleep(1)
                    else:
                        print("\nFim de jogo ou desistência.")
                        break
                
                if fase > 10: 
                    print("\n[bold gold1]🏆 INCRÍVEL! VOCÊ É O MESTRE SUPREMO DOS LABIRINTOS! 🏆[/]")
                    sucesso = iniciar_fase(args.name, dificuldade, modo_ia, fase)
                  
            case "3":
                utils.imprime_instrucoes()
            case "4":
                som.parar_musica() # Para o som antes de fechar
                break
            case _:
                print("Opção inválida.")

if __name__ == "__main__":
    main()
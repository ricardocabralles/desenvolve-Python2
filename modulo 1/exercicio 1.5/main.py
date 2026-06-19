import argparse
from personalizador import layout, painel, progresso, estilo

# Dicionário para mapear as opções da CLI para as funções
MAPA = {
    "layout": {"1": layout.layout_simples, "2": layout.layout_duplo},
    "painel": {"1": painel.painel_borda, "2": painel.painel_colorido},
    "progresso": {"1": progresso.progresso_carregamento, "2": progresso.progresso_spinner},
    "estilo": {"1": estilo.estilo_negrito_azul, "2": estilo.estilo_alerta}
}

def main():
    parser = argparse.ArgumentParser(description="Formatador de texto usando Rich.")
    
    parser.add_argument("texto", help="Texto ou caminho do arquivo para imprimir.")
    
    parser.add_argument("-a", "--arquivo", action="store_true", 
                        help="Ative se o argumento 'texto' for um caminho de arquivo.")
    
    parser.add_argument("-m", "--modulo", choices=MAPA.keys(), default="painel",
                        help="Escolha o módulo: layout, painel, progresso, estilo.")
    
    parser.add_argument("-f", "--funcao", choices=["1", "2"], default="1",
                        help="Escolha a função (ID): 1 ou 2.")

    args = parser.parse_args()

    # Executa a função escolhida
    funcao_escolhida = MAPA[args.modulo][args.funcao]
    funcao_escolhida(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
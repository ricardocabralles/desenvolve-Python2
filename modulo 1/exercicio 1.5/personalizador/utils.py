"""
Utilitários compartilhados para o pacote personalizador.
"""
def obter_texto(entrada, is_arquivo):
    """
    Trata a entrada de dados, lendo arquivos se necessário.
    
    Returns:
        str: O conteúdo final pronto para ser exibido.
    """
    if is_arquivo:
        try:
            with open(entrada, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return f"[bold red]Erro:[/] Arquivo '{entrada}' não encontrado."
    return entrada
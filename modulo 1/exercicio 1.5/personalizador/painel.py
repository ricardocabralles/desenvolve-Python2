"""
Módulo para exibição de conteúdos dentro de painéis (caixas) estilizados.
"""
from rich.console import Console
from rich.panel import Panel
from .utils import obter_texto

console = Console()

def painel_borda(texto, isArquivo=False):
    """Exibe o texto dentro de um painel com borda simples."""
    conteudo = obter_texto(texto, isArquivo)
    console.print(Panel(conteudo, title="Painel Informação"))

def painel_colorido(texto, isArquivo=False):
    """Exibe o texto em um painel com bordas vermelhas e sombra."""
    conteudo = obter_texto(texto, isArquivo)
    console.print(Panel(conteudo, border_style="bright_red", subtitle="Fim do conteúdo"))
"""
Módulo para aplicação de estilos de cores e formatações básicas de texto.
"""
from rich.console import Console
from .utils import obter_texto

console = Console()

def estilo_negrito_azul(texto, isArquivo=False):
    """Imprime o texto em azul e negrito."""
    conteudo = obter_texto(texto, isArquivo)
    console.print(f"[bold blue]{conteudo}[/]")

def estilo_alerta(texto, isArquivo=False):
    """Imprime o texto com estilo de erro/alerta."""
    conteudo = obter_texto(texto, isArquivo)
    console.print(f"[white on red] ALERTA: {conteudo} [/]")
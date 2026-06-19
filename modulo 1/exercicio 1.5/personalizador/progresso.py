"""
Módulo para visualização de indicadores de progresso e carregamento.
"""
from rich.console import Console
from rich.progress import track
from time import sleep
from .utils import obter_texto

console = Console()

def progresso_carregamento(texto, isArquivo=False):
    """Simula o processamento do texto com uma barra de progresso."""
    conteudo = obter_texto(texto, isArquivo)
    for _ in track(range(5), description="Processando..."):
        sleep(0.2)
    console.print(f"[bold green]Concluído:[/] {conteudo}")

def progresso_spinner(texto, isArquivo=False):
    """Usa um spinner enquanto exibe o conteúdo."""
    conteudo = obter_texto(texto, isArquivo)
    with console.status("[bold blue]Lendo dados...") as status:
        sleep(1)
        console.print(conteudo)
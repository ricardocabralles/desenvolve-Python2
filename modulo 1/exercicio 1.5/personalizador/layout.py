"""
Módulo para gerenciamento de layouts de terminal usando a biblioteca Rich.
Permite dividir a tela em diferentes regiões para exibição de conteúdo.
"""
from rich.console import Console
from rich.layout import Layout
from .utils import obter_texto

console = Console()

def layout_simples(texto, isArquivo=False):
    """Cria um layout dividido com o texto no topo."""
    conteudo = obter_texto(texto, isArquivo)
    layout = Layout()
    layout.split_column(
        Layout(name="topo"),
        Layout(name="base")
    )
    layout["topo"].update(conteudo)
    layout["base"].update("Rodapé de Layout")
    console.print(layout)

def layout_duplo(texto, isArquivo=False):
    """Divide a tela horizontalmente e repete o texto."""
    conteudo = obter_texto(texto, isArquivo)
    layout = Layout()
    layout.split_row(Layout(conteudo), Layout(conteudo))
    console.print(layout)
from rich import inspect
from rich.color import Color

inspect(inspect)           # Exibe as informações principais da função inspect

color = Color.parse('red')
inspect(color, methods=True)        # Gera um relatorio sobre um objeto python

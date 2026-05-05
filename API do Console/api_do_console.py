from rich.console import Console
from rich import inspect
from rich import print

console = Console()                  # permite extrair o maximo visual do rich

if __name__ == '__main__':
    inspect(console)
    print(
        console.size,
        '\nconsole.encoding', console.encoding,
        '\nconsole.is_terminal', console.is_terminal,
        '\nconsole.color', console.color_system
    )

    '''
    Você pode definir color_systemum dos seguintes valores:

    None        - Desativa completamente a cor.
    "auto"      - Detectará automaticamente o sistema de cores.
    "standard"  - Pode exibir 8 cores, com variações normais e 
                brilhantes, totalizando 16 cores.
    "256"       - Pode exibir as 16 cores do padrão, além de uma paleta
                fixa de 240 cores.
    "truecolor" - Pode exibir 16,7 milhões de cores, o que 
                provavelmente corresponde a todas as cores que seu 
                monitor consegue exibir.
    "windows"   - É possível exibir 8 cores no terminal Windows antigo.
                O novo terminal Windows pode exibir "truecolor".
    '''
    
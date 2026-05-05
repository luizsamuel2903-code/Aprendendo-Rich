# python -m rich, isso mostrara uma "pequena" paleta sobre a bibliteca

from rich  import print                    # Sobrescreve a funçao print nativa

print(
    '[italic red]Hellow[/italic red]',            # Exibe um texto enriquecido
    locals()                      # Retorna um dicionario que sera enriquecido
)

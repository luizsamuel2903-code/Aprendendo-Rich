# python -m rich.status, exibe uma pequena barra de espera
# python -m rich.spinner, exibe as possiveis animaçoes
 
from api_do_console import console
from time import sleep

with console.status('Working...'):
    sleep(2)

# Com o parametro spinner e possivel mudar a animação 
with console.status('Monkeying around...', spinner='monkey'):
    sleep(2)


with console.status('Aguarde...', spinner='aesthetic'):
    sleep(2)
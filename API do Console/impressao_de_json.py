from api_do_console import console
from rich.json import JSON

console.print_json('[false, true, null, "foo"]')  # Imprime o Json enriquecido

# Imprime o momento de execução e logo após o Json enriquecido
console.log(JSON('["foo", "bar", false, true, null]'))
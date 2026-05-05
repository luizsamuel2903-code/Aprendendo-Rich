from rich.console import Console

console = Console(width=20)

# Tanto o print quanto o log suportam o parametro justify
style = 'bold white on blue'

console.rule('[red bold]Justify no print[/red bold]' )

console.print('Rich', style=style)
console.print('Rich', style=style, justify='left')
console.print('Rich', style=style, justify='center')
console.print('Rich', style=style, justify='right')

# Redefinindo a largura do console
console.rule('[red bold]Justiy no log[/red bold]')
console.width = 50

console.log('Rich', style=style, justify='left')
console.log('Rich', style=style, justify='center')
console.log('Rich', style=style, justify='right')
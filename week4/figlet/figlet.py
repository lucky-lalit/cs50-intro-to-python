from pyfiglet import Figlet
from sys import argv
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()


if len(argv) == 1:
    figlet.setFont(font = choice(fonts))
    print('output: '+ '\n' +figlet.renderText(input("Input: ")))
    exit()

elif len(argv) == 3:
    if argv[1] != '-f' and argv[1] != '--font':
        exit('Invalid usage')
    elif argv[2] not in fonts:
        exit('Invalid usage')
    figlet.setFont(font = argv[2])
    print('ouput :' + '\n' + figlet.renderText(input("Input: ")))
else:
    exit('Invalid usage')

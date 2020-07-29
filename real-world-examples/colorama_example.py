#!/usr/bin/python

from colorama import init, Fore, Back, Style
init(autoreset=True)


print(Fore.RED + 'some red text')
print(Fore.GREEN + 'some green text')
print(Fore.BLUE + 'some blue text')
print(Fore.CYAN + 'some cyan text')
print(Fore.MAGENTA + 'some magenta text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.BRIGHT + Fore.GREEN + 'and green color in bright text')
print('automatically back to default color again')



# These are available color
"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""

from colors import colors as c
from os import system
from sys import exit


try:
    system('cd hakrawler; apt-get install docker.io -y; docker build -t hakluke/hakrawler .; clear')
    API_KEY = input(
        c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.MAGANTA + c.ANIMATION +
        ' ==> ' + c.RESET + c.YELLOW + 'https://account.shodan.io/' + c.MAGANTA
        + c.ANIMATION + ' <==\n' + c.RESET + c.CYAN +
        "    Enter Your Shodan Account API-KEY or If You Don't Have One,\n"
        "    Visit This Link To Register And Get The Key: " + c.RESET)

    system(f'shodan init {API_KEY}')
except Exception as Err_api:
    exit(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + f' {Err_api}.')
except KeyboardInterrupt:
    exit(c.YELLOW + '\nbye'.title())

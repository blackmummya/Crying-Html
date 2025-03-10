from colors import colors as c
from pyfiglet import figlet_format


def banner():
    # First line of banner (no backslashes here)
    print(f'   {c.ANIMATION + c.GREEN}({c.RESET}          '
          f'{c.ANIMATION + c.GREEN}({c.RESET}          (  '
          f'       ({c.ANIMATION + c.GREEN}({c.RESET})'
          f'{c.ANIMATION + c.GREEN}({c.RESET}       (     '
          f'              ')
    # Second line: double each backslash
    print(f'  ){c.ANIMATION + c.GREEN}\\){c.RESET})       '
          f'){c.ANIMATION + c.GREEN}){c.RESET}\\       )\\'
          f' ( {c.ANIMATION + c.GREEN}({c.RESET}   /)     '
          f' ){c.ANIMATION + c.GREEN}){c.RESET} ')
    # Third line
    print(f' ({c.ANIMATION + c.GREEN}()/{c.RESET}(     '
          f'( {c.ANIMATION + c.GREEN}/{c.RESET}({c.ANIMATION + c.GREEN}'
          f'({c.RESET}(       ( {c.ANIMATION + c.GREEN}('
          f'{c.RESET})      /{c.ANIMATION + c.GREEN}({c.RESET} '
          f'({c.ANIMATION + c.GREEN}({c.RESET}      '
          f'(/{c.ANIMATION + c.GREEN}({c.RESET}( ')
    # Fourth line: update all occurrences of \ to \\ where necessary
    print(f' (_{c.ANIMATION + c.GREEN}){c.RESET}){c.ANIMATION + c.GREEN}'
          f'({c.RESET}    )\\({c.ANIMATION + c.GREEN}){c.RESET}) '
          f'){c.ANIMATION + c.GREEN}){c.RESET}\\    ) {c.ANIMATION + c.GREEN}'
          f'({c.RESET} /(    ){c.ANIMATION + c.GREEN}){c.RESET}'
          f')\\ {c.ANIMATION + c.GREEN}){c.RESET}(    \\(_{c.ANIMATION + c.GREEN}){c.RESET}(    ')
    # Fifth line: double backslashes in the parts with literal backslashes
    print(f'{c.ANIMATION + c.GREEN}({c.RESET}_){c.ANIMATION + c.GREEN}'
          f'){c.RESET}_){c.ANIMATION + c.GREEN}){c.RESET}  ({c.ANIMATION + c.GREEN}'
          f'({c.RESET}_){c.ANIMATION + c.GREEN}){c.RESET}/ /({c.ANIMATION + c.GREEN}'
          f'({c.RESET}_)  (({c.ANIMATION + c.GREEN}){c.RESET} \\(  ){c.ANIMATION + c.GREEN}'
          f'){c.RESET}_|({c.ANIMATION + c.GREEN}({c.RESET}_)({c.ANIMATION + c.GREEN}'
          f'({c.RESET}    )\\){c.ANIMATION + c.GREEN}){c.RESET}_   ')
    # Sixth line (ASCII art with no problematic backslashes)
    print(f'╭━━╮╭╮{c.ANIMATION + c.RED}╱╱{c.RESET}╭━━━┳━━━┳╮╭━╮ ╭━╮╭━┳╮{c.ANIMATION + c.RED}'
          f'╱{c.RESET}╭┳━╮╭━┳━╮╭━┳╮{c.ANIMATION + c.RED}╱╱{c.RESET}╭┳━━━╮')
    # Seventh line
    print(f'┃╭╮┃┃┃{c.ANIMATION + c.RED}╱╱{c.RESET}┃╭━╮┃╭━╮┃┃┃╭╯ ┃┃╰╯┃┃┃{c.ANIMATION + c.RED}╱'
          f'{c.RESET}┃┃┃╰╯┃┃┃╰╯┃┃╰╮╭╯┃╭━╮┃')
    # Eighth line
    print(f'┃╰╯╰┫┃{c.ANIMATION + c.RED}╱╱{c.RESET}┃┃{c.ANIMATION + c.RED}╱{c.RESET}┃┃┃{c.ANIMATION + c.RED}'
          f'╱{c.RESET}╰┫╰╯╯{c.ANIMATION + c.RED}╱{c.RESET} ┃╭╮╭╮┃┃{c.ANIMATION + c.RED}╱{c.RESET}'
          f'┃┃╭╮╭╮┃╭╮╭╮┣╮╰╯╭┫┃{c.ANIMATION + c.RED}╱{c.RESET}┃┃')
    # Ninth line
    print(f'┃╭━╮┃┃{c.ANIMATION + c.RED}╱{c.RESET}╭┫╰━╯┃┃{c.ANIMATION + c.RED}╱{c.RESET}╭┫╭╮┃{c.ANIMATION + c.RED}'
          f'╱{c.RESET} ┃┃┃┃┃┃┃{c.ANIMATION + c.RED}╱{c.RESET}┃┃┃┃┃┃┃┃┃┃┃┃╰╮╭╯┃╰━╯┃')
    # Tenth line
    print(f'┃╰━╯┃╰━╯┃╭━╮┃╰━╯┃┃┃╰╮ ┃┃┃┃┃┃╰━╯┃┃┃┃┃┃┃┃┃┃┃{c.ANIMATION + c.RED}╱{c.RESET}┃┃{c.ANIMATION + c.RED}'
          f'╱{c.RESET}┃╭━╮┃')
    # Eleventh line
    print(f'╰━━━┻━━━┻╯{c.ANIMATION + c.RED}╱{c.RESET}╰┻━━━┻╯╰━╯ ╰╯╰╯╰┻━━━┻╯╰╯╰┻╯╰╯╰╯{c.ANIMATION + c.RED}'
          f'╱{c.RESET}╰╯{c.ANIMATION + c.RED}╱{c.RESET}╰╯{c.ANIMATION + c.RED}╱{c.RESET}╰╯')


def version():
    __author__ = 'Black_Mummya'
    __version__ = '0.4v'
    __email__ = 'blackmummya@gmail.com'
    __status__ = 'Development'
    __codename__ = 'Html_Crying'
    __source__ = 'https://github.com/blackmummya'
    __info__ = 'use for field bug bounty and penetration testing'.title()

    print(c.CYAN + f'Name: {__codename__}\n'
                   f'Use: {__info__}\n'
                   f'Author: {__author__}\n'
                   f'Source: {__source__}\n')


def gi():
    logo_gi = """
    
░██████╗░░█████╗░████████╗██╗░░██╗███████╗██████╗░  ██╗███╗░░██╗███████╗░█████╗░
██╔════╝░██╔══██╗╚══██╔══╝██║░░██║██╔════╝██╔══██╗  ██║████╗░██║██╔════╝██╔══██╗
██║░░██╗░███████║░░░██║░░░███████║█████╗░░██████╔╝  ██║██╔██╗██║█████╗░░██║░░██║
██║░░╚██╗██╔══██║░░░██║░░░██╔══██║██╔══╝░░██╔══██╗  ██║██║╚████║██╔══╝░░██║░░██║
╚██████╔╝██║░░██║░░░██║░░░██║░░██║███████╗██║░░██║  ██║██║░╚███║██║░░░░░╚█████╔╝
░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░
    """
    print(logo_gi)

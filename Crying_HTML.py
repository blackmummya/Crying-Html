#!/usr/bin/env python3
dont_write_bytecode = True
try:
    from colors import colors as c
    from sys import exit
    from subprocess import check_output
    from bs4 import BeautifulSoup
    from os import getgid, system
    from colorama import Fore
    from banner import banner
    from requests import get
    import re
except Exception as Err:
    exit(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + f' {Err}.' + c.RESET)


# TODO: If the user is not in the root DIRECTORY, the script will stop working !
if getgid() == 0:
    # TODO: display banner.
    banner()
    try:
        client_url = input(c.CYAN + '[*] enter target url: '.title() + c.RESET)
        FLAG = get(client_url)
        if FLAG.status_code == 200:
            pass
    except Exception as Err:
        print(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + f' {Err}')
    except KeyboardInterrupt:
        exit(c.YELLOW + '\nbye.'.title())
else:
    print(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + ' Run it as root!'.title())


def html_parser():
    try:
        while True:
            system('clear')
            banner()
            user_requests = input(c.RED + '[1]' + c.YELLOW + ' display source code.'.title() +
                                  c.RED + '\n[2]' + c.YELLOW + ' save source code.'.title() +
                                  c.RED + '\n[3]' + c.YELLOW + ' get all links.'.title() +
                                  c.RED + '\n[4]' + c.YELLOW + ' get all subdomains.'.title() +
                                  c.RED + '\n[5]' + c.YELLOW + ' ip discover.\n\n'.title() +
                                  c.RED + '[*]' + c.YELLOW + ' choose: '.title())
            system('clear')

            if user_requests == '1':
                get_response = get(client_url)
                print(c.RESET + f'\n{get_response.text}')
            elif user_requests == '2':
                get_response = get(client_url)
                content = get_response.text
                with open('index.txt', 'w') as f:
                    f.write(content)
                    print(c.YELLOW + '\ndone'.title())
            elif user_requests == '3':
                get_response = get(client_url)
                soup = BeautifulSoup(get_response.content, 'lxml')
                for index, link in enumerate(soup.find_all('a'), start=1):
                    print(Fore.YELLOW + f'{index}: ' + c.GREEN + f'{link.get("href")}' + c.WHITE + ' ==> ' + c.CYAN + f'{link.text}')
            elif user_requests == '4':
                system(c.RESET + 'cd hakrawler; apt-get install docker.io -y; docker build -t hakluke/hakrawler .')
                system('clear')
                banner()
                system(f'echo {client_url} | docker run --rm -i hakluke/hakrawler -subs')
            elif user_requests == '5':
                regular_curl = re.findall(r'(?:https://)(.*)', client_url)[0]
                get_ip = check_output([f'nslookup {regular_curl.strip("/")}'], shell=True)
                regex = re.findall(r'(?:Address:)(.*)', get_ip.decode())
                system('clear')
                banner()
                print(c.CYAN + 'IP:' + c.YELLOW + f'{regex[1]}')

            elif user_requests == 'exit':
                exit(c.YELLOW + '\nbye.'.title())

            else:
                print(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + ' Your choice as your existence is wrong !'.title())
            break

    except KeyboardInterrupt:
        exit(c.YELLOW + '\nbye.'.title())


if __name__ == '__main__':
    html_parser()

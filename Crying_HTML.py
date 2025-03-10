try:
    from subprocess import check_output
    from colors import colors as c
    from colorama import Fore
    from banner import banner
    from time import sleep
    from os import system
    from sys import exit
    from json import dump, load
    import re
except Exception as Err:
    exit(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + f' {Err}.' + c.RESET)


def nmap(url):
    system('clear')
    banner = """

███╗░░██╗███╗░░░███╗░█████╗░██████╗░
████╗░██║████╗░████║██╔══██╗██╔══██╗
██╔██╗██║██╔████╔██║███████║██████╔╝
██║╚████║██║╚██╔╝██║██╔══██║██╔═══╝░
██║░╚███║██║░╚═╝░██║██║░░██║██║░░░░░
╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░
"""
    print(banner)
    try:
        set_timing = int(input(c.YELLOW + c.ANIMATION + '\n[+]' + c.RESET + c.CYAN +
                               ' Set timing template between 0-5 (higher is faster): '.title()))
        if 5 < set_timing < 0:
            system('clear')
            exit(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + 'invalid time'.title())
        regular_curl = re.findall(r'(?:https://)(.*)', url)[0]
        get_ip = check_output([f'nslookup {regular_curl.strip("/")}'], shell=True)
        regex = re.findall(r'(?:Address:)(.*)', get_ip.decode())
        system('clear')
        print(banner)
        print(
            c.GREEN + '\n[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'vulnerability scanner for this ip' + c.YELLOW + f'{regex[1]}' + c.GREEN + ' default choose:\n\n'.title() +
            c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Enable OS detection, version detection, script scanning, and traceroute.\n'.title() +
            c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Fast mode - Scan fewer ports than the default scan.\n'.title() +
            c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + f'Set timing template {set_timing}.\n'.title() +
            c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Increase verbosity level.\n\n\n' + Fore.RESET.title() + c.RESET)
        system(f'nmap -A -F -T{set_timing} {regex[1]} -v')

    except KeyboardInterrupt:
        exit(c.YELLOW + '\nBye')
    except ValueError:
        exit(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + 'invalid input'.title())


def shodan(cl):
    system('clear')
    banner = """
░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░███╗░░██╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗████╗░██║
╚█████╗░███████║██║░░██║██║░░██║███████║██╔██╗██║
░╚═══██╗██╔══██║██║░░██║██║░░██║██╔══██║██║╚████║
██████╔╝██║░░██║╚█████╔╝██████╔╝██║░░██║██║░╚███║
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝
"""
    print(banner)
    regular_curl = re.findall(r'(?:https://)(.*)', cl)[0]
    get_ip = check_output([f'nslookup {regular_curl.strip("/")}'], shell=True)
    pythex = re.findall(r'(?:Address:)(.*)', get_ip.decode())
    res = check_output(f'shodan host {pythex[1]}', shell=True).decode()
    _host_name_ = re.findall(r'(?:Hostnames:)(.*)', res)[0]
    _n_ports_ = re.findall(r'(?:Number of open ports:)(.*)', res)[0]
    _o_ports_ = re.findall(r'(?:Ports:)(\s.*\s.*\s.*\s.*\s.*\s.*\s.*\s.*\s.*\s.*\s.*\s.*\s.*)', res)[0]
    print(
        c.GREEN + '\n[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'HostName:' + c.YELLOW + f" {_host_name_.lstrip()}\n" +
        c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Number of open ports:' + c.YELLOW + f" {_n_ports_.lstrip()}\n" +
        c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Ports:' + c.YELLOW + f"{_o_ports_.lstrip()}")
    try:
        _vul_ = re.findall(r'(?:Vulnerabilities: )(.*\s.*)', res)[0]
        print(c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Vulnerability:' + c.RED + f"\n{_vul_.lstrip()}")
    except IndexError:
        pass

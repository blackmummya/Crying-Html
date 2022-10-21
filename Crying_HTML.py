try:
    from banner import banner, gi, version
    from vulnerability import nmap, shodan
    from subprocess import check_output
    from colors import colors as c
    from bs4 import BeautifulSoup
    from os import getgid, system
    from colorama import Fore
    from requests import get
    from json import loads
    from sys import exit
    import re
except Exception as Err:
    exit(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + f' {Err}.')


# TODO: If the user is not in the root DIRECTORY, the script will stop working !
if getgid() == 0:
    # TODO: display banner.
    system('clear')
    banner()
    version()
    try:
        client_url = input(c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'enter target url: '.title())
        FLAG = get(client_url)
        if FLAG.status_code == 200:
            pass
    except Exception as Err:
        exit(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + f' {Err}')
    except KeyboardInterrupt:
        exit(c.YELLOW + '\nbye.'.title())
else:
    print(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + ' Run it as root!'.title())


def vulnerability_scanner(url):
    try:
        set_timing = int(input(c.YELLOW + c.ANIMATION + '[+]' + c.RESET + c.CYAN +
                               ' Set timing template between 0-5 (higher is faster): '.title()))
        if 5 < set_timing < 0:
            system('clear')
            exit(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + 'invalid time'.title())
        regular_curl = re.findall(r'(?:https://)(.*)', url)[0]
        get_ip = check_output([f'nslookup {regular_curl.strip("/")}'], shell=True)
        regex = re.findall(r'(?:Address:)(.*)', get_ip.decode())
        system('clear')
        banner()
        print(
            c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'vulnerability scanner for this ip' + c.YELLOW + f'{regex[1]}' + c.GREEN + ' default choose:\n\n'.title() +
            c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Enable OS detection, version detection, script scanning, and traceroute.\n'.title() +
            c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Fast mode - Scan fewer ports than the default scan.\n'.title() +
            c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + f'Set timing template {set_timing}.\n'.title() +
            c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Increase verbosity level.\n\n\n' + Fore.RESET.title() + c.RESET)
        system(f'nmap -A -F -T{set_timing} {regex[1]} -v')

    except KeyboardInterrupt:
        exit(c.YELLOW + '\nBye')
    except ValueError:
        exit(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + 'invalid input'.title())


def gather_info(url, _url_):
    system('clear')
    gi()
    _ip_ = loads(get(url).text)['ip']
    _type_ = loads(get(url).text)['type']
    _city_ = loads(get(url).text)['city']
    _flag_ = loads(get(url).text)['flag']
    _id_ = loads(get(url).text)['timezone']
    _utc_ = loads(get(url).text)['timezone']
    _state_ = loads(get(_url_).text)['state']
    _abbr_ = loads(get(url).text)['timezone']
    _org_ = loads(get(url).text)['connection']
    _isp_ = loads(get(url).text)['connection']
    _success_ = loads(get(url).text)['success']
    _latitude_ = loads(get(url).text)['latitude']
    _domain_ = loads(get(url).text)['connection']
    _continent_ = loads(get(url).text)['continent']
    _longitude_ = loads(get(url).text)['longitude']
    _current_time_ = loads(get(url).text)['timezone']
    _country_code_ = loads(get(url).text)['country_code']
    _country_name_ = loads(get(_url_).text)['country_name']
    _continent_code_ = loads(get(url).text)['continent_code']

    print(c.GREEN + '[' + c.WHITE + '*' + c.GREEN + ']' + c.CYAN + 'info\n'.title() +
          c.WHITE + '=======\n' +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'IP:' + c.YELLOW + f' {_ip_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Type:' + c.YELLOW + f' {_type_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Success:' + c.YELLOW + f' {_success_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Continent:' + c.YELLOW + f' {_continent_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'continent_code:' + c.YELLOW + f' {_continent_code_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'country_name:' + c.YELLOW + f' {_country_name_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'country_code:' + c.YELLOW + f' {_country_code_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'City:' + c.YELLOW + f' {_city_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Latitude:' + c.YELLOW + f' {_latitude_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Longitude:' + c.YELLOW + f' {_longitude_}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Flag:' + c.YELLOW + f' {_flag_["img"]}\n' +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'State:' + c.YELLOW + f' {_state_}\n\n'.title() +
          c.GREEN + '[' + c.WHITE + '*' + c.GREEN + ']' + c.CYAN + 'Connection\n'.title() +
          c.WHITE + '=============\n' +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Org:' + c.YELLOW + f' {_org_["org"]}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Isp:' + c.YELLOW + f' {_isp_["isp"]}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Domain:' + c.YELLOW + f' {_domain_["domain"]}\n\n'.title() +
          c.GREEN + '[' + c.WHITE + '*' + c.GREEN + ']' + c.CYAN + 'time-zone\n'.title() +
          c.WHITE + '============\n' +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Id:' + c.YELLOW + f' {_id_["id"]}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Abbr:' + c.YELLOW + f' {_abbr_["abbr"]}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Utc:' + c.YELLOW + f' {_utc_["utc"]}\n'.title() +
          c.GREEN + '[' + c.WHITE + '+' + c.GREEN + ']' + c.CYAN + 'Current Time:' + c.YELLOW + f' {_current_time_["current_time"]}\n'.title())


def html_parser():
    system('clear')
    banner()
    user_requests = input(c.RED + '[1]' + c.CYAN + ' display source code.'.title() +
                          c.RED + '\n[2]' + c.CYAN + ' save source code.'.title() +
                          c.RED + '\n[3]' + c.CYAN + ' get all links.'.title() +
                          c.RED + '\n[4]' + c.CYAN + ' get all subdomains.'.title() +
                          c.RED + '\n[5]' + c.CYAN + ' ip discover.'.title() +
                          c.RED + '\n[6]' + c.CYAN + ' scan vulnerability.'.title() +
                          c.RED + '\n[7]' + c.CYAN + ' information gathering.\n\n'.title() +
                          c.RED + '[*]' + c.CYAN + ' choose: '.title())
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
            print(
                Fore.YELLOW + f'{index}: ' + c.GREEN + f'{link.get("href")}' + c.WHITE + ' ==> ' + c.CYAN + f'{link.text}')
    elif user_requests == '4':
        system('clear')
        banner()
        system(f'echo {client_url} | docker run --rm -i hakluke/hakrawler -subs')
    elif user_requests == '5':
        regular_curl = re.findall(r'(?:https://)(.*)', client_url)[0]
        get_ip = check_output([f'nslookup {regular_curl.strip("/")}'], shell=True)
        pythex = re.findall(r'(?:Address:)(.*)', get_ip.decode())
        system('clear')
        banner()
        print(c.CYAN + 'IP:' + c.YELLOW + f'{pythex[1]}')
    elif user_requests == '6':
        system('clear')
        banner()
        opt_vul = input(c.RED + '\n[1]' + c.CYAN + ' using nmap to scan vulnerability.\n'.title() +
                        c.RED + '[2]' + c.CYAN + ' using shodan to scan vulnerability.\n\n'.title() +
                        c.RED + '[*]' + c.CYAN + ' choose: '.title())
        if opt_vul == '1':
            nmap(client_url)
        elif opt_vul == '2':
            shodan(client_url)
    elif user_requests == '7':
        regular_curl = re.findall(r'(?:https://)(.*)', client_url)[0]
        get_ip = check_output([f'nslookup {regular_curl.strip("/")}'], shell=True)
        pythex = re.findall(r'(?:Address:)(.*)', get_ip.decode())
        system('clear')
        gi()
        gather_info(f'http://ipwho.is/{pythex[1].lstrip()}',
                    f'https://geolocation-db.com/json/{pythex[1].lstrip()}&position=true')
    elif user_requests == 'exit':
        exit(c.YELLOW + '\nbye.'.title())

    else:
        print(
            c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + ' Your choice as your existence is wrong !'.title())
    exit()


if __name__ == '__main__':
    try:
        html_parser()
    except Exception as Err:
        print(c.RED + '[' + c.YELLOW + c.ANIMATION + '!' + c.RESET + c.RED + ']' + f' {Err}.')
    except KeyboardInterrupt:
        exit(c.YELLOW + '\nbye.'.title())

import re
import sys
import json
import socket
from subprocess import check_output, CalledProcessError
from os import getgid, system
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

# Custom modules
from banner import banner, gi, version
from vulnerability import nmap, shodan
from colors import colors as c


init(autoreset=True)


def clear_screen():
    system('clear')


def print_error(msg):
    print(c.RED + f'[{c.YELLOW}{c.ANIMATION}!{c.RESET}{c.RED}] {msg}')


def get_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print_error(f"Error fetching JSON from {url}: {e}")
        return {}


def ensure_root():
    if getgid() != 0:
        print(c.RED + f"[{c.YELLOW}{c.ANIMATION}{c.RESET}{c.RED}] Run it as root!".title())
        sys.exit(1)


def prompt_target_url():
    target = input(c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + 'Enter target URL: '.title())
    try:
        resp = requests.get(target)
        if resp.status_code == 200:
            return target
        else:
            print_error(f"Received status code {resp.status_code} for {target}")
            sys.exit(1)
    except Exception as e:
        print_error(e)
        sys.exit(1)


def vulnerability_scanner(url):
    try:
        set_timing = int(input(c.YELLOW + c.ANIMATION + '[+]' + c.RESET + c.CYAN +
                                 ' Set timing template between 0-5 (higher is faster): '.title()))
        if set_timing < 0 or set_timing > 5:
            clear_screen()
            sys.exit(c.RED + f'[{c.YELLOW}{c.ANIMATION}{c.RESET}{c.RED}] Invalid timing value.'.title())

        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path
        try:
            ns_output = check_output(['nslookup', domain]).decode()
            ip_matches = re.findall(r'Address:\s*(.*)', ns_output)
            if len(ip_matches) < 2:
                print_error("IP address not found using nslookup.")
                return
            target_ip = ip_matches[1].strip()
        except CalledProcessError as e:
            print_error(f"nslookup failed: {e}")
            return

        clear_screen()
        banner()
        print(
            c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Vulnerability scanner for IP: {target_ip}\n' +
            c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + 'Enable OS detection, version detection, script scanning, and traceroute.\n' +
            c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + 'Fast mode - Scan fewer ports than the default scan.\n' +
            c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Set timing template {set_timing}.\n' +
            c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + 'Increase verbosity level.\n\n'
        )
        system(f'nmap -A -F -T{set_timing} {target_ip} -v')
    except KeyboardInterrupt:
        sys.exit(c.YELLOW + '\nBye')
    except ValueError:
        sys.exit(c.RED + f'[{c.YELLOW}{c.ANIMATION}{c.RESET}{c.RED}] Invalid input.'.title())


def gather_info(ipwho_url, geo_url):
    clear_screen()
    gi()
    ip_data = get_json(ipwho_url)
    geo_data = get_json(geo_url)

    _ip_ = ip_data.get('ip', 'N/A')
    _type_ = ip_data.get('type', 'N/A')
    _city_ = ip_data.get('city', 'N/A')
    _flag_ = ip_data.get('flag', {}).get('img', 'N/A')
    _continent_ = ip_data.get('continent', 'N/A')
    _continent_code_ = ip_data.get('continent_code', 'N/A')
    _country_code_ = ip_data.get('country_code', 'N/A')
    _country_name_ = geo_data.get('country_name', 'N/A')
    _latitude_ = ip_data.get('latitude', 'N/A')
    _longitude_ = ip_data.get('longitude', 'N/A')
    _state_ = geo_data.get('state', 'N/A')
    _org_ = ip_data.get('connection', {}).get('org', 'N/A')
    _isp_ = ip_data.get('connection', {}).get('isp', 'N/A')
    _success_ = ip_data.get('success', 'N/A')
    _timezone_ = ip_data.get('timezone', {})
    _id_ = _timezone_.get('id', 'N/A')
    _abbr_ = _timezone_.get('abbr', 'N/A')
    _utc_ = _timezone_.get('utc', 'N/A')
    _current_time_ = _timezone_.get('current_time', 'N/A')

    print(
        c.GREEN + f'[{c.WHITE}*{c.GREEN}] ' + c.CYAN + 'Info\n' +
        c.WHITE + '=======\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'IP: {c.YELLOW}{_ip_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Type: {c.YELLOW}{_type_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Success: {c.YELLOW}{_success_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Continent: {c.YELLOW}{_continent_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Continent Code: {c.YELLOW}{_continent_code_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Country Name: {c.YELLOW}{_country_name_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Country Code: {c.YELLOW}{_country_code_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'City: {c.YELLOW}{_city_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Latitude: {c.YELLOW}{_latitude_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Longitude: {c.YELLOW}{_longitude_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Flag: {c.YELLOW}{_flag_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'State: {c.YELLOW}{_state_}\n\n' +
        c.GREEN + f'[{c.WHITE}*{c.GREEN}] ' + c.CYAN + 'Connection\n' +
        c.WHITE + '=============\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Org: {c.YELLOW}{_org_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Isp: {c.YELLOW}{_isp_}\n\n' +
        c.GREEN + f'[{c.WHITE}*{c.GREEN}] ' + c.CYAN + 'Time-Zone\n' +
        c.WHITE + '============\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'ID: {c.YELLOW}{_id_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Abbr: {c.YELLOW}{_abbr_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'UTC: {c.YELLOW}{_utc_}\n' +
        c.GREEN + f'[{c.WHITE}+{c.GREEN}] ' + c.CYAN + f'Current Time: {c.YELLOW}{_current_time_}\n'
    )


def html_parser(client_url):
    clear_screen()
    banner()
    user_requests = input(
        c.RED + '[1]' + c.CYAN + ' Display source code.\n' +
        c.RED + '[2]' + c.CYAN + ' Save source code.\n' +
        c.RED + '[3]' + c.CYAN + ' Get all links.\n' +
        c.RED + '[4]' + c.CYAN + ' Get all subdomains.\n' +
        c.RED + '[5]' + c.CYAN + ' IP discover.\n' +
        c.RED + '[6]' + c.CYAN + ' Scan vulnerability.\n' +
        c.RED + '[7]' + c.CYAN + ' Information gathering.\n\n' +
        c.RED + '[*]' + c.CYAN + ' Choose: '
    ).strip()

    clear_screen()

    if user_requests == '1':
        response = requests.get(client_url)
        print(c.RESET + '\n' + response.text)
    elif user_requests == '2':
        response = requests.get(client_url)
        with open('index.txt', 'w') as f:
            f.write(response.text)
        print(c.YELLOW + '\nDone'.title())
    elif user_requests == '3':
        response = requests.get(client_url)
        soup = BeautifulSoup(response.content, 'lxml')
        for index, link in enumerate(soup.find_all('a'), start=1):
            href = link.get("href")
            text = link.get_text(strip=True)
            print(Fore.YELLOW + f'{index}: ' + c.GREEN + f'{href}' + c.WHITE + ' ==> ' + c.CYAN + f'{text}')
    elif user_requests == '4':
        clear_screen()
        banner()
        system(f'echo {client_url} | docker run --rm -i hakluke/hakrawler -subs')
    elif user_requests == '5':
        parsed = urlparse(client_url)
        domain = parsed.netloc or parsed.path
        try:
            ns_output = check_output(['nslookup', domain]).decode()
            ip_matches = re.findall(r'Address:\s*(.*)', ns_output)
            if len(ip_matches) < 2:
                print_error("IP address not found.")
                return
            target_ip = ip_matches[1].strip()
            clear_screen()
            banner()
            print(c.CYAN + 'IP: ' + c.YELLOW + f'{target_ip}')
        except Exception as e:
            print_error(e)
    elif user_requests == '6':
        clear_screen()
        banner()
        opt_vul = input(
            c.RED + '\n[1]' + c.CYAN + ' Using nmap to scan vulnerability.\n' +
            c.RED + '[2]' + c.CYAN + ' Using shodan to scan vulnerability.\n\n' +
            c.RED + '[*]' + c.CYAN + ' Choose: '
        ).strip()
        if opt_vul == '1':
            nmap(client_url)
        elif opt_vul == '2':
            shodan(client_url)
    elif user_requests == '7':
        parsed = urlparse(client_url)
        domain = parsed.netloc or parsed.path
        try:
            ns_output = check_output(['nslookup', domain]).decode()
            ip_matches = re.findall(r'Address:\s*(.*)', ns_output)
            if len(ip_matches) < 2:
                print_error("IP address not found.")
                return
            target_ip = ip_matches[1].strip()
            clear_screen()
            gi()
            gather_info(f'http://ipwho.is/{target_ip}', f'https://geolocation-db.com/json/{target_ip}&position=true')
        except Exception as e:
            print_error(e)
    elif user_requests.lower() == 'exit':
        sys.exit(c.YELLOW + '\nBye'.title())
    else:
        print(c.RED + f'[{c.YELLOW}{c.ANIMATION}{c.RESET}{c.RED}] Your choice is invalid!'.title())
    sys.exit()


def main():
    try:
        ensure_root()
        clear_screen()
        banner()
        version()
        client_url = prompt_target_url()
        html_parser(client_url)
    except Exception as e:
        print_error(e)
    except KeyboardInterrupt:
        sys.exit(c.YELLOW + '\nBye'.title())


if __name__ == '__main__':
    main()

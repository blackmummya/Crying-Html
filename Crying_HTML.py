#!/usr/bin/env python3
import re
import sys
import subprocess
from os import system
from colors import colors as c
from colorama import Fore
from banner import banner
from time import sleep

def clear_screen() -> None:
    """Clears the terminal screen."""
    system('clear')

def get_domain(url: str) -> str:
    """
    Extracts the domain from a URL.
    
    Returns the domain part after 'https://' or 'http://'.
    """
    match = re.search(r'https?://([^/]+)', url)
    if match:
        return match.group(1).strip()
    else:
        # Fallback: if the URL doesn't start with a scheme, assume the full string is the domain.
        return url.strip()

def lookup_ip(domain: str) -> str:
    """
    Uses nslookup to find the IP address of a given domain.
    
    Returns the second IP found (if available), or the first one.
    Exits if no valid IP is found.
    """
    try:
        # Run nslookup command without shell=True for safety.
        output = subprocess.check_output(['nslookup', domain]).decode()
        # Find all IP addresses in the output.
        matches = re.findall(r'Address:\s*([\d.]+)', output)
        if not matches:
            raise ValueError("No IP address found for domain: " + domain)
        # Use the second IP if available; otherwise, use the first.
        return matches[1].strip() if len(matches) > 1 else matches[0].strip()
    except Exception as e:
        print(c.RED + f"Error during nslookup for '{domain}': {e}" + c.RESET)
        sys.exit(1)

def prompt_timing() -> int:
    """
    Prompts the user to enter a timing template between 0 and 5.
    
    Exits if input is invalid.
    """
    try:
        timing = int(input(c.YELLOW + c.ANIMATION + '\n[+]' + c.RESET + c.CYAN +
                             ' Set timing template between 0-5 (higher is faster): '.title()))
        if timing < 0 or timing > 5:
            raise ValueError("Timing value must be between 0 and 5")
        return timing
    except ValueError as ve:
        print(c.RED + f"[{c.YELLOW}{c.ANIMATION}{c.RESET}{c.RED}] Invalid input: {ve}" + c.RESET)
        sys.exit(1)

def run_nmap_scan(url: str) -> None:
    """
    Clears the screen, displays a banner, prompts for timing,
    extracts the IP address via nslookup, and runs an nmap scan.
    """
    clear_screen()
    ascii_banner = """
███╗░░██╗███╗░░░███╗░█████╗░██████╗░
████╗░██║████╗░████║██╔══██╗██╔══██╗
██╔██╗██║██╔████╔██║███████║██████╔╝
██║╚████║██║╚██╔╝██║██╔══██║██╔═══╝░
██║░╚███║██║░╚═╝░██║██║░░██║██║░░░░░
╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░
"""
    print(ascii_banner)
    timing = prompt_timing()
    
    domain = get_domain(url)
    ip_address = lookup_ip(domain)
    
    clear_screen()
    print(ascii_banner)
    info = (
        f"\n[{c.WHITE}+{c.GREEN}] {c.CYAN}Vulnerability scanner for this IP: {c.YELLOW}{ip_address}{c.GREEN} default choose:\n\n"
        f"[{c.WHITE}+{c.GREEN}] {c.CYAN}Enable OS detection, version detection, script scanning, and traceroute.\n"
        f"[{c.WHITE}+{c.GREEN}] {c.CYAN}Fast mode - Scan fewer ports than the default scan.\n"
        f"[{c.WHITE}+{c.GREEN}] {c.CYAN}Set timing template {timing}.\n"
        f"[{c.WHITE}+{c.GREEN}] {c.CYAN}Increase verbosity level.\n\n\n{Fore.RESET}{c.RESET}"
    )
    print(info)
    
    # Run the nmap command with provided timing and target IP.
    system(f"nmap -A -F -T{timing} {ip_address} -v")

def run_shodan_scan(url: str) -> None:
    """
    Clears the screen, displays a banner, extracts the IP via nslookup,
    runs a Shodan scan, and prints key output such as hostnames, open ports, and vulnerabilities.
    """
    clear_screen()
    ascii_banner = """
░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░███╗░░██╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗████╗░██║
╚█████╗░███████║██║░░██║██║░░██║███████║██╔██╗██║
░╚═══██╗██╔══██║██║░░██║██║░░██║██╔══██║██║╚████║
██████╔╝██║░░██║╚█████╔╝██████╔╝██║░░██║██║░╚███║
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝
"""
    print(ascii_banner)
    domain = get_domain(url)
    ip_address = lookup_ip(domain)
    
    try:
        # Run shodan command.
        res = subprocess.check_output(f"shodan host {ip_address}", shell=True).decode()
    except Exception as e:
        print(c.RED + f"Error running Shodan command: {e}" + c.RESET)
        sys.exit(1)
    
    # Extract fields using regular expressions.
    host_name = re.search(r'Hostnames:\s*(.*)', res)
    n_ports = re.search(r'Number of open ports:\s*(.*)', res)
    ports = re.search(r'Ports:\s*(.*)', res)
    
    host_name_str = host_name.group(1).strip() if host_name else "N/A"
    n_ports_str = n_ports.group(1).strip() if n_ports else "N/A"
    ports_str = ports.group(1).strip() if ports else "N/A"
    
    print(
        f"\n[{c.WHITE}+{c.GREEN}] {c.CYAN}HostName: {c.YELLOW}{host_name_str}\n"
        f"[{c.WHITE}+{c.GREEN}] {c.CYAN}Number of open ports: {c.YELLOW}{n_ports_str}\n"
        f"[{c.WHITE}+{c.GREEN}] {c.CYAN}Ports: {c.YELLOW}{ports_str}"
    )
    
    # Optionally print vulnerabilities if available.
    vul_match = re.search(r'Vulnerabilities:\s*(.*)', res)
    if vul_match:
        print(f"\n[{c.WHITE}+{c.GREEN}] {c.CYAN}Vulnerability: {c.RED}{vul_match.group(1).strip()}")

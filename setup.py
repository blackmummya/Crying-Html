import subprocess
import sys
from os import chdir, system, path
from colors import colors as c

def run_command(command, description=""):
    if description:
        print(c.GREEN + f"[+] {description}" + c.RESET)
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        sys.exit(c.RED + f"Error executing command: {command}" + c.RESET)
    return result

def setup_docker_image():
    if not path.isdir("hakrawler"):
        sys.exit(c.RED + "The 'hakrawler' directory does not exist." + c.RESET)

    chdir("hakrawler")
    
    run_command("apt-get install docker.io -y", "Installing docker.io")
    run_command("docker build -t hakluke/hakrawler .", "Building Docker image for hakluke/hakrawler")
    
    system('clear')

def init_shodan():
    prompt = (
        c.GREEN + "[" + c.WHITE + "+" + c.GREEN + "]" + c.MAGANTA + c.ANIMATION +
        " ==> " + c.RESET + c.YELLOW + "https://account.shodan.io/" + c.MAGANTA + c.ANIMATION +
        " <==\n" + c.RESET + c.CYAN +
        "    Enter Your Shodan Account API-KEY or if you don't have one,\n"
        "    visit the above link to register and get your key: " + c.RESET
    )
    api_key = input(prompt).strip()
    if not api_key:
        sys.exit(c.RED + "No API key provided." + c.RESET)
    
    run_command(f"shodan init {api_key}", "Initializing Shodan API key")

if __name__ == '__main__':
    try:
        setup_docker_image()
        init_shodan()
    except KeyboardInterrupt:
        sys.exit(c.YELLOW + "\nBye" + c.RESET)
    except Exception as err_api:
        sys.exit(c.RED + f"[{c.YELLOW}{c.ANIMATION}!{c.RESET}{c.RED}] {err_api}." + c.RESET)

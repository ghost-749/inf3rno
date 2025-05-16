import os
import platform
import time
import random
from modules import ip_info, port_scanner, whois_lookup, hash_cracker, passgen
from modules import subdomain_finder, dns_lookup, reverse_ip, url_scan, admin_finder
from modules import header_analyzer, mac_lookup
from modules import directory_bruteforcer, sql_injection_scanner, wifi_password

# ANSI color codes for hacker aesthetic
NEON_GREEN = "\033[1;32m"
NEON_MAGENTA = "\033[1;35m"
NEON_CYAN = "\033[1;36m"
NEON_RED = "\033[1;31m"
DIM_WHITE = "\033[2;37m"
RESET = "\033[0m"

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def banner():
    print(f"""{NEON_MAGENTA}
8888888888b    8888888888888.d8888b. 8888888b. 888b    888 .d88888b.  
  888  8888b   888888      d88P  Y88b888   Y88b8888b   888d88P" "Y88b 
  888  88888b  888888           .d88P888    88888888b  888888     888 
  888  888Y88b 8888888888      8888" 888   d88P888Y88b 888888     888 
  888  888 Y88b888888           "Y8b.8888888P" 888 Y88b888888     888 
  888  888  Y88888888      888    888888 T88b  888  Y888888     888 
  888  888   Y8888888      Y88b  d88P888  T88b 888   Y8888Y88b. .d88P 
8888888888    Y888888       "Y8888P" 888   T88b888    Y888 "Y88888P"  
{NEON_GREEN}                     INF3RNO | ELITE CYBER OPS TOOLKIT{RESET}
{NEON_RED}                     >> INITIATING MODULES... <<{RESET}
{NEON_CYAN}                       :: GH0ST_749 v1.0 ::{RESET}
""")


def loading_animation():
    """Display a fast scanning animation."""
    print(f"{NEON_CYAN}[!] SCANNING TARGET...{RESET}", end='', flush=True)
    for _ in range(5):
        print(f"{NEON_GREEN}/////{RESET}", end='', flush=True)
        time.sleep(0.05)  # Fast animation
    print()

def pause():
    input(f"{NEON_MAGENTA}[>] PRESS ENTER TO RETURN TO MATRIX...{RESET}")

def validate_url(url):
    """Basic URL validation."""
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url.strip()

def validate_file(path):
    """Check if file exists."""
    return os.path.isfile(path)

def main():
    clear()
    banner()  # Display banner once at startup
    print(f"{NEON_GREEN}|==> SELECT ATTACK VECTOR:{RESET}")
    print(f"{NEON_CYAN}  [01] INFILTRATE IP")
    print(f"  [02] SCAN PORTS")
    print(f"  [03] WHOIS RECON")
    print(f"  [04] CRACK HASH")
    print(f"  [05] FORGE PASSWORD")
    print(f"  [06] ENUMERATE SUBDOMAINS")
    print(f"  [07] DNS RECON")
    print(f"  [08] REVERSE IP")
    print(f"  [09] SCAN URL")
    print(f"  [10] HUNT ADMIN PANEL")
    print(f"  [11] ANALYZE HEADERS")
    print(f"  [12] MAC VENDOR LOOKUP")
    print(f"  [13] BRUTEFORCE DIRECTORIES")
    print(f"  [14] SQL INJECTION PROBE")
    print(f"  [15] EXTRACT WIFI KEYS")
    print(f"  [00] TERMINATE SESSION{RESET}")

    while True:
        choice = input(f"{NEON_GREEN}[>] VECTOR: {RESET}").strip()
        print(f"{NEON_CYAN}[DEBUG] Selected choice: '{choice}'{RESET}")  # Debug print

        try:
            if choice == "1":
                ip = input(f"{NEON_GREEN}[>] TARGET IP [INFILTRATE]: {RESET}").strip()
                if ip:
                    loading_animation()
                    print(ip_info.lookup(ip))
                else:
                    print(f"{NEON_RED}[!] TARGET IP REQUIRED!{RESET}")

            elif choice == "2":
                ip = input(f"{NEON_GREEN}[>] TARGET IP [SCAN]: {RESET}").strip()
                if ip:
                    loading_animation()
                    ports = port_scanner.scan(ip)
                    print(f"{NEON_CYAN}OPEN PORTS:{RESET}", ports)
                else:
                    print(f"{NEON_RED}[!] TARGET IP REQUIRED!{RESET}")

            elif choice == "3":
                domain = input(f"{NEON_GREEN}[>] TARGET DOMAIN [RECON]: {RESET}").strip()
                if domain:
                    loading_animation()
                    print(whois_lookup.lookup(domain))
                else:
                    print(f"{NEON_RED}[!] DOMAIN REQUIRED!{RESET}")

            elif choice == "4":
                h = input(f"{NEON_GREEN}[>] HASH [DECRYPT]: {RESET}").strip()
                wordlist = input(f"{NEON_GREEN}[>] WORDLIST PATH: {RESET}").strip()
                if h and validate_file(wordlist):
                    loading_animation()
                    print(f"{NEON_CYAN}RESULT:{RESET}", hash_cracker.crack(h, wordlist))
                else:
                    print(f"{NEON_RED}[!] INVALID HASH OR WORDLIST PATH!{RESET}")

            elif choice == "5":
                try:
                    length = int(input(f"{NEON_GREEN}[>] PASSWORD LENGTH: {RESET}").strip())
                    if length > 0:
                        loading_animation()
                        print(f"{NEON_CYAN}FORGED PASSWORD:{RESET}", passgen.generate(length))
                    else:
                        print(f"{NEON_RED}[!] LENGTH MUST BE POSITIVE!{RESET}")
                except ValueError:
                    print(f"{NEON_RED}[!] NUMERIC INPUT REQUIRED!{RESET}")

            elif choice == "6":
                domain = input(f"{NEON_GREEN}[>] TARGET DOMAIN [ENUMERATE]: {RESET}").strip()
                if domain:
                    loading_animation()
                    print(f"{NEON_CYAN}SUBDOMAINS:{RESET}", subdomain_finder.find(domain))
                else:
                    print(f"{NEON_RED}[!] DOMAIN REQUIRED!{RESET}")

            elif choice == "7":
                domain = input(f"{NEON_GREEN}[>] TARGET DOMAIN [DNS]: {RESET}").strip()
                if domain:
                    loading_animation()
                    print(f"{NEON_CYAN}DNS DATA:{RESET}", dns_lookup.lookup(domain))
                else:
                    print(f"{NEON_RED}[!] DOMAIN REQUIRED!{RESET}")

            elif choice == "8":
                ip = input(f"{NEON_GREEN}[>] TARGET IP [REVERSE]: {RESET}").strip()
                if ip:
                    loading_animation()
                    print(f"{NEON_CYAN}REVERSE IP DATA:{RESET}", reverse_ip.lookup(ip))
                else:
                    print(f"{NEON_RED}[!] TARGET IP REQUIRED!{RESET}")

            elif choice == "9":
                url = input(f"{NEON_GREEN}[>] TARGET URL [SCAN]: {RESET}").strip()
                if url:
                    url = validate_url(url)
                    loading_animation()
                    print(f"{NEON_CYAN}SCAN RESULT:{RESET}", url_scan.scan(url))
                else:
                    print(f"{NEON_RED}[!] URL REQUIRED!{RESET}")

            elif choice == "10":
                domain = input(f"{NEON_GREEN}[>] TARGET DOMAIN [HUNT]: {RESET}").strip()
                if domain:
                    loading_animation()
                    print(f"{NEON_CYAN}ADMIN PANELS:{RESET}", admin_finder.find(domain))
                else:
                    print(f"{NEON_RED}[!] DOMAIN REQUIRED!{RESET}")

            elif choice == "11":
                url = input(f"{NEON_GREEN}[>] TARGET URL [ANALYZE]: {RESET}").strip()
                if url:
                    url = validate_url(url)
                    loading_animation()
                    print(f"{NEON_CYAN}HEADERS:{RESET}", header_analyzer.analyze(url))
                else:
                    print(f"{NEON_RED}[!] URL REQUIRED!{RESET}")

            elif choice == "12":
                mac = input(f"{NEON_GREEN}[>] MAC ADDRESS [LOOKUP]: {RESET}").strip()
                if mac:
                    loading_animation()
                    print(f"{NEON_CYAN}VENDOR:{RESET}", mac_lookup.lookup(mac))
                else:
                    print(f"{NEON_RED}[!] MAC ADDRESS REQUIRED!{RESET}")

            elif choice == "13":
                url = input(f"{NEON_GREEN}[>] TARGET URL [BRUTEFORCE]: {RESET}").strip()
                wordlist = input(f"{NEON_GREEN}[>] WORDLIST PATH: {RESET}").strip()
                if url and validate_file(wordlist):
                    url = validate_url(url)
                    loading_animation()
                    print(f"{NEON_CYAN}DIRECTORIES:{RESET}", directory_bruteforcer.bruteforce(url, wordlist))
                else:
                    print(f"{NEON_RED}[!] INVALID URL OR WORDLIST PATH!{RESET}")

            elif choice == "14":
                url = input(f"{NEON_GREEN}[>] TARGET URL [SQL PROBE]: {RESET}").strip()
                if url:
                    url = validate_url(url)
                    loading_animation()
                    print(f"{NEON_CYAN}SQL INJECTION DATA:{RESET}", sql_injection_scanner.scan(url))
                else:
                    print(f"{NEON_RED}[!] URL REQUIRED!{RESET}")

            elif choice == "15":
                loading_animation()
                print(f"{NEON_CYAN}WIFI KEYS:{RESET}", wifi_password.extract())

            elif choice == "0":
                print(f"{NEON_RED}[!] TERMINATING SESSION...{RESET}")
                time.sleep(1)
                break

            else:
                print(f"{NEON_RED}[!] INVALID VECTOR! RESELECT.{RESET}")

        except Exception as e:
            print(f"{NEON_RED}[!] SYSTEM BREACH DETECTED: {str(e)}{RESET}")

        pause()

if __name__ == "__main__":
    main()
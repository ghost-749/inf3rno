import requests
from urllib.parse import urljoin

def bruteforce(url, wordlist_path):
    """
    Brute-force directories on a web server using a wordlist.
    Args:
        url (str): Base URL of the target (e.g., http://example.com)
        wordlist_path (str): Path to the wordlist file
    Returns:
        list: List of discovered directories
    """
    found_directories = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    try:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            directories = [line.strip() for line in file if line.strip()]

        for directory in directories:
            target_url = urljoin(url, directory)
            try:
                response = requests.get(target_url, headers=headers, timeout=5)
                if response.status_code == 200:
                    found_directories.append(target_url)
                    print(f"[+] Found: {target_url}")
                elif response.status_code == 403:
                    print(f"[!] Forbidden: {target_url}")
            except requests.RequestException as e:
                print(f"[-] Error accessing {target_url}: {e}")
                continue

    except FileNotFoundError:
        return f"Error: Wordlist file '{wordlist_path}' not found."
    except Exception as e:
        return f"Error: {str(e)}"

    return found_directories if found_directories else "No directories found."
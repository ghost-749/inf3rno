import requests

def find(domain):
    subdomains = ["www", "mail", "ftp", "test", "dev", "admin"]
    found = []
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=2)
            if r.status_code < 400:
                found.append(url)
        except:
            continue
    return found if found else "No subdomains found."

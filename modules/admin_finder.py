import requests

def find(domain):
    paths = ["admin", "admin/login", "admin.php", "admin.html", "login", "wp-admin"]
    found = []
    for path in paths:
        url = f"http://{domain}/{path}"
        try:
            r = requests.get(url, timeout=2)
            if r.status_code == 200:
                found.append(url)
        except:
            continue
    return found if found else "No admin panels found."

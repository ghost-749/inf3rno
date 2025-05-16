import subprocess

def lookup(domain):
    try:
        result = subprocess.run(["whois", domain], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

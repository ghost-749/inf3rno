import requests

def analyze(url):
    try:
        r = requests.get(url)
        return r.headers
    except Exception as e:
        return {"error": str(e)}

import socket

def lookup(domain):
    try:
        return socket.gethostbyname_ex(domain)
    except Exception as e:
        return f"Error: {e}"

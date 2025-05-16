import socket

def lookup(ip):
    try:
        return socket.gethostbyaddr(ip)
    except Exception as e:
        return f"Error: {e}"

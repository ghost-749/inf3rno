import socket

def scan(host):
    open_ports = []
    for port in range(1, 1025):
        try:
            with socket.create_connection((host, port), timeout=0.5):
                open_ports.append(port)
        except:
            continue
    return open_ports

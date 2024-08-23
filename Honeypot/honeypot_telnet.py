import socket, logging

# Configurer les logs
logging.basicConfig(filename='honeypot.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def start_telnet_honeypot(host='0.0.0.0', port=23):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Honeypot Telnet démarré sur {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        logging.info(f"Nouvelle connexion Telnet de {client_address}")
        client_socket.send(b"Bienvenue sur Telnet honeypot!\n")
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break
                logging.info(f"Commande Telnet reçue de {client_address}: {data.decode().strip()}")
                client_socket.send(b"Commande non reconnue.\n")
            except ConnectionResetError:
                break
        client_socket.close()

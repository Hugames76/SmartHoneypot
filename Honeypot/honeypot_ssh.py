import socket ,logging, signal, sys

# Configurer les logs pour capturer les tentatives d'intrusion
logging.basicConfig(filename='honeypot.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')


def start_honeypot(host='0.0.0.0', port=2222):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Le serveur écoute jusqu'à 5 connexions simultanées
    print(f"Honeypot démarré sur {host}:{port}")

    def signal_handler(sig, frame):
        print('Arrêt du honeypot...')
        server_socket.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            logging.info(f"Nouvelle connexion de {client_address}")

            # Simuler un faux prompt SSH
            client_socket.send(b"Bienvenue sur SSH honeypot!\n")
            while True:
                try:
                    data = client_socket.recv(1024)  # Recevoir des données de l'attaquant
                    if not data:
                        break
                    logging.info(f"Commande reçue de {client_address}: {data.decode().strip()}")
                    client_socket.send(b"Commande non reconnue.\n")  # Répondre avec un message par défaut
                except ConnectionResetError:
                    break

            client_socket.close()
        except OSError:
            break
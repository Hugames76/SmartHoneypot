import socket
import logging

# Configurer les logs
logging.basicConfig(filename='..\\DATA\\honeypot.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def start_honeypot(host='0.0.0.0', port=2222):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Écoute des connexions simultanées
    print(f"Honeypot SSH démarré sur {host}:{port}")

    fake_files = ['file1.txt', 'file2.log', 'report.pdf']
    current_dir = '/home/user/'

    while True:
        client_socket, client_address = server_socket.accept()
        logging.info(f"Nouvelle connexion SSH de {client_address}")
        client_socket.send(b"Bienvenue sur SSH honeypot!\n")
        client_socket.send(f"{current_dir}$ ".encode())

        while True:
            try:
                data = client_socket.recv(1024).decode().strip()
                if not data:
                    break

                logging.info(f"Commande reçue SSH de {client_address}: {data}")

                # Simulation des commandes shell
                if data == 'ls':
                    response = '\n'.join(fake_files) + '\n'
                elif data == 'pwd':
                    response = current_dir + '\n'
                elif data.startswith('cd '):
                    new_dir = data.split(' ')[1]
                    current_dir += new_dir + '/'
                    response = ''
                elif data.startswith('exit'):
                    break
                else:
                    response = f"Commande '{data}' non reconnue.\n"

                client_socket.send(response.encode())
                client_socket.send(f"{current_dir}$ ".encode())
            except ConnectionResetError:
                break

        client_socket.close()

import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

logging.basicConfig(filename='honeypot.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')


class HoneypotHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"Requête GET reçue de {self.client_address}: {self.path}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bienvenue sur le serveur HTTP Honeypot!")

def start_http_honeypot():
    http_server = HTTPServer(('0.0.0.0', 8080), HoneypotHTTP)
    print("Honeypot HTTP démarré sur le port 8080")
    http_server.serve_forever()

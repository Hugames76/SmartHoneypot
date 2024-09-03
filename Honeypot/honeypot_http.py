import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

logging.basicConfig(filename='..\\DATA\\honeypot.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Pages fictives vulnérables
login_page = """
<html>
<body>
    <h1>Login</h1>
    <form method="POST" action="/login">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

# Simuler une injection SQL
def simulate_sql_injection(username):
    if "'" in username:
        return "Erreur SQL: tentative d'injection détectée!"
    return "Connexion réussie"

class HoneypotHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/login":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(login_page.encode())
        elif self.path == "/vulnerable":
            # Page vulnérable à XSS
            params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            user_input = params.get("input", [""])[0]
            response = f"<h1>Input reçu: {user_input}</h1>"
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/login":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()
            post_params = urllib.parse.parse_qs(post_data)
            username = post_params.get('username', [''])[0]
            password = post_params.get('password', [''])[0]

            # Capturer la tentative de connexion
            logging.info(f"Login tentatif avec username: {username} et password: {password}")

            response = simulate_sql_injection(username)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.encode())

def start_http_honeypot():
    http_server = HTTPServer(('0.0.0.0', 8080), HoneypotHTTP)
    print("Honeypot HTTP démarré sur le port 8080")
    http_server.serve_forever()

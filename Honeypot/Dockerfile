# Utiliser une image de base Python légère
FROM python:3.9-slim

# Installer les dépendances pour SMB (Impacket) et RDP (RDPY)
RUN pip install --upgrade pip
RUN pip install impacket

# Copier les scripts Python dans le conteneur
COPY honeypot.py /app/honeypot.py
COPY honeypot_http.py /app/honeypot_http.py
COPY honeypot_ssh.py /app/honeypot_ssh.py
COPY honeypot_telnet.py /app/honeypot_telnet.py
COPY honeypot_smb.py /app/honeypot_smb.py
COPY honeypot_rdp.py /app/honeypot_rdp.py

# Définir le répertoire de travail
WORKDIR /app

# Exposer les ports nécessaires pour les services
EXPOSE 2222
EXPOSE 8080
EXPOSE 23
EXPOSE 445
EXPOSE 3389

# Lancer le script principal
CMD ["python", "honeypot.py"]

from impacket import smbserver
import logging

# Configurer les logs
logging.basicConfig(filename='honeypot.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def start_smb_honeypot():
    logging.info("Démarrage du honeypot SMB")
    server = smbserver.SimpleSMBServer(listenAddress='0.0.0.0', listenPort=445)
    server.setSMB2Support(True)
    server.addShare("SHARE", "/tmp")
    logging.info("Honeypot SMB démarré sur 0.0.0.0:445")
    server.start()

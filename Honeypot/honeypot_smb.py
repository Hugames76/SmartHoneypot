from impacket import smbserver
import logging

# Configurer les logs
logging.basicConfig(filename='..\\DATA\\honeypot.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def start_smb_honeypot():
    logging.info("Démarrage du honeypot SMB")
    
    # Créer un faux serveur SMB avec accès invité activé
    server = smbserver.SimpleSMBServer(listenAddress='0.0.0.0', listenPort=445)
    server.setSMB2Support(True)
    server.addShare("Public", "/tmp", 'Faux partage public avec accès invité')
    logging.info("Honeypot SMB démarré sur 0.0.0.0:445 avec accès invité")
    server.start()

# import logging
# from pyrdp import RDPPyServer

# Configurer les logs
# logging.basicConfig(filename='honeypot.log', level=logging.INFO, 
#                     format='%(asctime)s - %(message)s')

# def start_rdp_honeypot():
#     logging.info("Démarrage du honeypot RDP")
#     server = RDPPyServer(("0.0.0.0", 3389))
#     logging.info("Honeypot RDP démarré sur 0.0.0.0:3389")
#     server.start()
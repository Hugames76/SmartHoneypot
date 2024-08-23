import threading, logging
import honeypot_http
import honeypot_ssh
import honeypot_telnet
import honeypot_smb
# import honeypot_rdp

def start_honeypots():
    # Démarrer les honeypots dans des threads séparés
    try :
        ssh_thread = threading.Thread(target=honeypot_ssh.start_honeypot)
        http_thread = threading.Thread(target=honeypot_http.start_http_honeypot)
        telnet_thread = threading.Thread(target=honeypot_telnet.start_telnet_honeypot)
        smb_thread = threading.Thread(target=honeypot_smb.start_smb_honeypot)
        #rdp_thread = threading.Thread(target=honeypot_rdp.start_rdp_honeypot)

        # Lancer les threads
        ssh_thread.start()
        http_thread.start()
        telnet_thread.start()
        smb_thread.start()
        #rdp_thread.start()

        # Garder le programme en cours d'exécution
        ssh_thread.join()
        http_thread.join()
        telnet_thread.join()
        smb_thread.join()
        #rdp_thread.join()
        
    except logging.error as e:
        print(e)
        pass

if __name__ == "__main__":
    start_honeypots()

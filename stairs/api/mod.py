import socket


def send_data(mess, ip, port) -> bool:
    '''
    Send message to microcontroler on port and ip  and waiting for response
    '''
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(mess, (ip, port))
        sock.settimeout(0.5)
        sock.recvfrom(128)
        sock.close()
        return True
    except:
        sock.close()
        return False
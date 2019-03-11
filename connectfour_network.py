'''POORVA NENE 38426682'''
import socket
import collections
'''module that implements the I32CFSP and all socket handling'''

def connect(host: str, port: int) -> 'connection':
    ''' Makes a new connection with in and out pseudo-files.'''
    the_socket = socket.socket()

    the_socket.connect((host,port))

    the_socket_in = the_socket.makefile('r')
    the_socket_out = the_socket.makefile('w')

    return the_socket, the_socket_in, the_socket_out



def gethost() -> str:
    while True:
        host = input('HOST: ').strip()
        if host == '':
            print('Please specify a host (IP address or hostname)')
        else:
            return host



def getport() -> int:
    while True:
        try:
            port = int(input('PORT: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port

        except ValueError:
            print('Ports must be an integer between 0 and 65535')
            
def read_message(connection: 'connection') -> str:
    the_socket, the_socket_in, the_socket_out = connection
    return the_socket_in.readline()[:-1]           

def send_message(connection: 'connection', message: str) -> None:
    the_socket, the_socket_in, the_socket_out = connection
    the_socket_out.write(message + '\r\n')
    the_socket_out.flush()



def close(connection: 'connection') -> None:
    the_socket, the_socket_in, the_socket_out = connection
    the_socket_in.close()
    the_socket_out.close()
    the_socket.close()
    

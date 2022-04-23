import socket
import sys

MAX_LEN = 1024
HOST_IP = "192.168.1.207"
PORT = 12345

CLIENT_MESSAGE = "202481600170791"

def main():
    # Declare variable to hold the socket
    sock = None

    # Create the socket
    try:
        sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        print( "Client: Socket successfully created" )
    except socket.error as err:
        print( "Client: Socket creation failed with error %s" %(err) )
 
    # connecting to the server
    sock.connect( (HOST_IP, PORT) )
    print ( "Client: The socket has successfully connected to localhost" )

    # Send a message back to the server
    sock.send( CLIENT_MESSAGE.encode() )

    # Receive up to MAX_LEN bytes (chars) from the server & output
    msg = sock.recv( MAX_LEN )
    print( "Client: Recieved message from server - %s" %msg.decode( "utf-8" ) )

    return int(msg)



if __name__ == "__main__":
    main()

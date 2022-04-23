import socket			

MAX_LEN = 1024
SERVER_MESSAGE = "Thank you for connecting :)"

def main():

    # Create a socket object
    s = socket.socket()		
    print( "Server: Socket successfully created" )

    # Reserve a port on computer
    port = 12345			

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))		
    print ("Server: Socket binded to %s" %(port))

    # put the socket into listening mode
    s.listen(5)	
    print ("Server: Socket is listening")		

    # a forever loop until we interrupt it or
    # an error occurs
    while True:

        # Establish connection with client.
        c, addr = s.accept()	
        print( 'Server: Got connection from', addr )

        # send a thank you message to the client. encoding to send byte type.
        c.send( SERVER_MESSAGE.encode() )

        # Recieve the reply from the client
        msg = c.recv( MAX_LEN )
        print( "Server: Recieved message from client - %s" %msg.decode( "utf-8" ) )

        # Close the connection with the client
        c.close()


if __name__ == "__main__":
    main()
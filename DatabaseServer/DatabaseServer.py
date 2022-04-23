######################################################################
## IMPORTS
######################################################################

import paho.mqtt.client as paho
import json
import uuid
import socket
import time

import sys
sys.path.insert( 1, "../Database" )
import database as Database

######################################################################
## CLASSES
######################################################################

class DatabaseServer:
    ######################################################################
    ## CONSTANTS
    ######################################################################

    PORT = 12345
    MAX_LEN = 256

    ######################################################################
    ## CLASS VARIABLES
    ######################################################################

    SOCKET = None
    DATABASE = None

    ######################################################################
    ## MEMBER VARIABLES
    ######################################################################


    ######################################################################
    ## CONSTRUCTORS
    ######################################################################

    def initialize( ):

        # Initialize the static database
        DatabaseServer.DATABASE = Database.Database( "database.ini" )

        # Initialize the socket
        DatabaseServer.SOCKET = socket.socket()
        DatabaseServer.SOCKET.bind( ('', DatabaseServer.PORT ) )

        # put the socket into listening mode
        DatabaseServer.SOCKET.listen(5)	




    ######################################################################
    ## PRIVATE CALLBACKS
    ######################################################################

    ######################################################################
    ## PRIVATE METHODS
    ######################################################################

    def __handle_connection( conn ):

        # Recieve the reply from the client
        msg = conn.recv( DatabaseServer.MAX_LEN )
        print( "DatabaseServer: Recieved request from client for room  %s" %msg.decode( "utf-8" ) )

        room_num = int( msg )
        last_occupied = DatabaseServer.DATABASE.last_occupied( room_num )
        print( "Room ", room_num, " was last occupied at time ", last_occupied )

        # Figure out if the room was occupied in the last 5 seconds
        outgoing_msg = None
        if( time.time() - last_occupied <= 5 ):
            outgoing_msg = "1"
        else:
            outgoing_msg = "0"

        # send a thank you message to the client. encoding to send byte type.
        conn.send( outgoing_msg.encode() )

        # Close the connection with the client
        conn.close()

    ######################################################################
    ## PUBLIC METHODS
    ######################################################################
       

    '''
    Runs the client loop. This must be called after the connect method
     has been called.
    '''
    def run(  ):
        print( "B" )

        # Inititialze the class
        if DatabaseServer.SOCKET is None:
            DatabaseServer.initialize()

        print( "A" )

        # a forever loop until we interrupt it or
        # an error occurs
        while True:

            # Establish connection with client.
            c, addr = DatabaseServer.SOCKET.accept()
            DatabaseServer.__handle_connection( c )


try:
    DatabaseServer.run()
except Exception as e:
    print( e )
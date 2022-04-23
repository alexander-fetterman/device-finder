######################################################################
## IMPORTS
######################################################################

import paho.mqtt.client as paho
import json
import uuid

import sys
sys.path.insert( 1, "../Database" )
import database as Database

######################################################################
## CLASSES
######################################################################

class MqttDriver:
    ######################################################################
    ## CONSTANTS
    ######################################################################

    BROKER_URI = "127.0.0.1"
    CLIENT_NAME = "DemoClient"
    TOPIC = "/Demo"

    DEVICE_ID = "devID"
    TIMESTAMP = "ts"

    ######################################################################
    ## CLASS VARIABLES
    ######################################################################

    CLIENT = None
    DATABASE = None

    ######################################################################
    ## MEMBER VARIABLES
    ######################################################################


    ######################################################################
    ## CONSTRUCTORS
    ######################################################################

    '''
    Creates the member client. THIS METHOD DOES NOT DO ANY CONNECTING
     OR SUBSCRIBING!
    @param clientName --- The (unique) client name to be assigned to the
     member client.
    @param database --- A (user defined) database object, supplied externally
    '''
    def initialize( ): #database ):
        # Create a static MQTT client
        MqttDriver.CLIENT_NAME = str( uuid.getnode() )
        MqttDriver.CLIENT = paho.Client( MqttDriver.CLIENT_NAME )

        # Set the callback method for message received
        MqttDriver.CLIENT.on_message = MqttDriver.__message_received

        

        # Use the argument database as the member database
        MqttDriver.DATABASE = Database.Database( "database.ini" )


    ######################################################################
    ## PRIVATE CALLBACKS
    ######################################################################

    '''
    Acts as a driver for all logic following a message being received.
    '''
    def __message_received( client, userdata, message ):
        print( "Message received: ", str( message.payload.decode("utf-8") ) )
        
        # Parse the message into a dictionary
        try:
            msg_values = json.loads( str( message.payload.decode("utf-8") ) )

            #print( msg_values )
            print( "Device detected in room %d at time %d" % ( msg_values[ MqttDriver.DEVICE_ID ], msg_values[ MqttDriver.TIMESTAMP ] ) )
            MqttDriver.DATABASE.insert_values( msg_values[ MqttDriver.DEVICE_ID ], msg_values[ MqttDriver.TIMESTAMP ] )
        except Exception as e:
            print( "*****MESSAGE RECEIVE FAILED*****\n", e )

        # Insert the tuple into the database
        # print( 'Inserting tuple...' )
        # self.database.insert_values( msg_values[ 'ts' ], msg_values[ 'ms' ] )


    ######################################################################
    ## PRIVATE METHODS
    ######################################################################


    ######################################################################
    ## PUBLIC METHODS
    ######################################################################
    
    '''
    Connects the member Mqtt Client to the remote broker
    @param brokerURI --- The URI (universal resource identifier) of the broker
     to connect to. This should be in the form specified by the paho library.
    '''
    def connect(  ):
        # Connect the member client to the broker at the parameter
        #  specified URI
        MqttDriver.CLIENT.connect( MqttDriver.BROKER_URI )
    
    '''
    Subscribes the member Mqtt Client to a given topic
    @param topic --- The topic to subscribe to
    '''
    def subscribe(  ):
        # Subcribe to the input topic
        MqttDriver.CLIENT.subscribe( MqttDriver.TOPIC )

    '''
    Runs the client loop. This must be called after the connect method
     has been called.
    '''
    def run(  ):
        print( "B" )

        # Inititialze the class
        if MqttDriver.CLIENT is None:
            MqttDriver.initialize()
            MqttDriver.connect()
            MqttDriver.subscribe()

        print( "A" )

        # Start the client loop - use loop forever because we do not
        #  want to return.
        MqttDriver.CLIENT.loop_forever()


MqttDriver.run()
######################################################################
## IMPORTS
######################################################################

from re import M
import paho.mqtt.client as paho
import json
import uuid
import time

######################################################################
## CLASSES
######################################################################

class MqttClient():
    ######################################################################
    ## CONSTANTS
    ######################################################################

    BROKER_URI = "127.0.0.1"
    CLIENT_NAME = "DemoClient"
    TOPIC = "/Demo"

    ######################################################################
    ## CLASS VARIABLES
    ######################################################################

    CLIENT = None
    MAC = None

    ######################################################################
    ## MEMBER VARIABLES
    ######################################################################


    ######################################################################
    ## CONSTRUCTORS
    ######################################################################

    '''
    Creates the member client & connects it to the broker
    '''
    def initialize( ):
        # Create a static MQTT client
        MqttClient.CLIENT = paho.Client( MqttClient.CLIENT_NAME )

        # Connect the client to the broker
        MqttClient.CLIENT.connect( MqttClient.BROKER_URI )

        # Store the MAC address statically
        MqttClient.MAC = str( uuid.getnode() )

        # Use the argument database as the member database
        # self.database = database    

    ######################################################################
    ## PRIVATE HELPER FUNCTIONS
    ######################################################################    

    def generate_message(  ):
        # Create a new dictionary to create the message in
        msg_dict = dict()

        # Add the device ID
        msg_dict[ 'devID' ] = MqttClient.MAC

        # Add the current timestamp
        msg_dict[ 'ts' ] = int( time.time() )

        # Return the JSON string representation of the dictionary
        return json.dumps( msg_dict )
        


    ######################################################################
    ## PUBLIC APPLICATION LOGIC
    ######################################################################    
    
    def send_message(  ):

        # Initialize the static client if it hasn't been already
        if MqttClient.CLIENT is None:
            MqttClient.initialize()

        MqttClient.CLIENT.publish( MqttClient.TOPIC, MqttClient.generate_message() )
import RPi.GPIO as GPIO
import time
import datetime

class GPIO_Reader():
    
    ##################################################
    ## CONSTANTS
    ##################################################

    PIN = 5
    DETECTED = 1

    SLEEP_DETECTED = 1
    SLEEP_UNDETECTED = 1

    ##################################################
    ## PRIVATE STATIC METHODS
    ##################################################

    def __initialize(  ):
        # Initialize GPIO
        GPIO.setwarnings( True )
        GPIO.setmode( GPIO.BCM )

        # Set designated pin as an input
        GPIO.setup( GPIO_Reader.PIN, GPIO.IN )

    
    def device_found(  ):
        pass

    ##################################################
    ## PUBLIC STATIC METHODS
    ##################################################

    def run(  ):
        # Initialization code
        GPIO_Reader.__initialize()

        # Loop forever
        while( True ):
            # Check the pin
            pin_level = GPIO.input( GPIO_Reader.PIN )

            if( pin_level == GPIO_Reader.DETECTED ):
                print( "\n***** DEVICE DETECTED! *****\n" )
                time.sleep( GPIO_Reader.SLEEP_DETECTED )
            else:
                print( "NO DEVICE FOUND..." )
                time.sleep( GPIO_Reader.SLEEP_UNDETECTED )
                


GPIO_Reader.run()

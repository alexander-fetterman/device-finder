import RPi.GPIO as GPIO
import time
import datetime

class GPIO_Reader():
    
    ##################################################
    ## CONSTANTS
    ##################################################

    ##################################################
    ## PRIVATE STATIC METHODS
    ##################################################

    def __initialize(  ):
        # Initialize GPIO
        GPIO.setwarnings( True )
        GPIO.setmode( GPIO.BCM )

    ##################################################
    ## PUBLIC STATIC METHODS
    ##################################################

    def run(  ):
        # Initialization code
        GPIO_Reader.__initialize()

        # Loop forever
        while( True ):


# GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=18)

try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        print("Last valid input: " + str(datetime.datetime.now()))

	        print("Temperature: %-3.1f C" % result.temperature)
	        print("Humidity: %-3.1f %%" % result.humidity)

	    #time.sleep(0)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

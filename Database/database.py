######################################################################
## IMPORTS
######################################################################
from configparser import ConfigParser
import psycopg2 as psql

######################################################################
## CLASSES
######################################################################

class Database:
    ######################################################################
    ## CONSTANTS
    ######################################################################
    
    DATABASE_TYPE = 'postgresql'
    TABLE_NAME = 'devices'
    DB_INI = "database.ini"#""~/Documents/IoT/device-finder/Database/database.ini"#"/home/alexander/IoT/device-finder/Database/database.ini"

    ######################################################################
    ## MEMBER VARIABLES
    ######################################################################
    

    ######################################################################
    ## CONSTRUCTORS
    ######################################################################
    
    '''
    Creates a Database object. Does not connect to any database. Defines
     all member variables. Set the connection member variable to null.
    @param filename --- The initialization filename which will be used for connection
    '''
    def __init__( self, filename ):
        self.FILENAME = Database.DB_INI
        self.db_connect()

    ######################################################################
    ## PRIVATE METHODS
    ######################################################################

    '''
    Parses the internally stored config file, and returns the parameters
      necessary to connect to a database.
    '''
    def __parse_config( self ):
        # create a parser
        parser = ConfigParser()
        
        # read config file
        parser.read( Database.DB_INI )

        # get section, default to postgresql
        db = {}
        if parser.has_section( self.DATABASE_TYPE ):
            params = parser.items( self.DATABASE_TYPE )
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format( self.DATABASE_TYPE, self.FILENAME ))

        return db
    
    '''
    Builds the string representation of the query to insert 
    '''
    def build_insert_query():
        raise Exception( 'Method not yet implemented' )

    ######################################################################
    ## PUBLIC METHODS
    ######################################################################


    '''
    Connects to a database and stores the connection within this 
     object. This is required before calling any DB operations.
    '''
    def db_connect( self ):
        # Connect to the database using the config file
        self.connection = psql.connect( **self.__parse_config() )

        # Open a cursor to the database
        self.cursor = self.connection.cursor()

    '''
    Inserts a tuple into the database
    '''
    def insert_values( self, timestamp, moisture_level ):
        # Perform the insert operation
        self.cursor.execute( "INSERT INTO {table} VALUES( {ts}, {ms} )".format( table = self.TABLE_NAME, ts = timestamp, ms = moisture_level ) )
        
        # Commit the insert operation
        self.connection.commit()

    def last_occupied( self, room_number ):
        self.cursor.execute( "SELECT max( ts ) as last_occupied FROM devices WHERE mac = {rn};".format( rn=room_number ) )
        return self.cursor.fetchone()[0]


    '''
    Get the most recent tuples from the database.
    @param limit --- The maximum number of tuples to return.
    '''
    def get_values( self, limit ):
        # Execute a query - this does not return any data yet
        self.cursor.execute( "SELECT * FROM sensordata order by ts desc LIMIT {lm};".format( table = self.TABLE_NAME, lm=limit ) )

        # Fetch all of the data requested. This may be a time intensive 
        #  operation over external network.
        tuples = self.cursor.fetchall()
        return tuples

db = Database( "database.ini" )
db.db_connect()
db.insert_values( 2, 5 )
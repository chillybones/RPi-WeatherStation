import Adafruit_DHT
from time import sleep

class DHT_Read():

    def __init__(self, RPiPin):
        # Define the sensor type and GPIO pin
        self.sensor = Adafruit_DHT.DHT11
        self.pin = RPiPin

    def GetReading(self):
        # Get a reading out of the DHT
        self.humid, self.temp = Adafruit_DHT.read_retry(self.sensor, self.pin)

        # Print to the console so we know there is a good reading
        print('temp={0:0.1f}*C  humidity={1:0.1f}%'.format(self.temp, self.humid))

        # Return dictionary of values
        return {"IndoorTemp": self.temp, "IndoorHumidity": self.humid}


    def WriteToDateBase(self, ReadingDict):
        # Eventually this will write to a database for historical tracking
        return 0
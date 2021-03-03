#!/home/pi/virtual_envs/controller_venv/bin/python3

"""
'temp_humidity.py'
==================================
Example of sending analog sensor
values to an Adafruit IO feed.

Author(s): Brent Rubell

Tutorial Link: Tutorial Link: https://learn.adafruit.com/adafruit-io-basics-temperature-and-humidity

Dependencies:
    - Adafruit IO Python Client
        (https://github.com/adafruit/io-client-python)
    - Adafruit_Python_DHT
        (https://github.com/adafruit/Adafruit_Python_DHT)
"""

# import standard python modules.
import time

import board
import adafruit_dht

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# Delay in-between sensor readings, in seconds.
DHT_READ_TIMEOUT = 10

# Pin connected to DHT22 data pin
DHT_DATA_PIN = 27

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_cLGV14ODaefrNxlGGbVmwOSjCzXR'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username).
ADAFRUIT_IO_USERNAME = 'tushargarud'

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D27)

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Set up Adafruit IO Feeds.
temperature_c_feed = aio.feeds('temperature-c')
temperature_f_feed = aio.feeds('temperature-f')
humidity_feed = aio.feeds('humidity')
    
while True:
    try:
        # Print the values to the serial port
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
            # Send humidity and temperature feeds to Adafruit IO
            temperature_c = '%.2f'%(temperature)
            temperature_f = '%.2f'%(temperature * (9 / 5) + 32)
            humidity = '%.2f'%(humidity)
            aio.send(temperature_c_feed.key, str(temperature_c))
            aio.send(temperature_f_feed.key, str(temperature_f))
            aio.send(humidity_feed.key, str(humidity))            
        else:
            print('Failed to get DHT22 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print('RuntimeError while getting DHT22 Reading, trying again in ', DHT_READ_TIMEOUT, 'seconds')
        time.sleep(DHT_READ_TIMEOUT)
        continue
    except Exception as error:
        print('Exception while getting DHT22 Reading. Exiting')
        dhtDevice.exit()
        raise error

    time.sleep(DHT_READ_TIMEOUT)

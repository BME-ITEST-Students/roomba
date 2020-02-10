from PD2030.roomba import Client
from PD2030.roomba import Misc
import time

c = Client.Client(False)
c.start_remote_server()
c.toggle_logging(False)

while True:
    text = c.formatted_sensor_data()
    Misc.clear_console()
    print(text)
    time.sleep(1)
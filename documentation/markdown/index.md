<!-- PD2030 documentation master file, created by
sphinx-quickstart on Sat Jan 11 15:45:57 2020.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Roomba client documentation


### class PD2030.roomba.Client.Client(ip=False, do_upload=True)
This class is used to communicate with the robot.

For student use: Yes


* **Parameters**

    
    * **ip** – The IP address of the raspberry pi controlling the roomba robot.


    * **do_upload** – Boolean, indicating whether code should be uploaded to the raspberry pi.



#### delete_remote_folder(folder)
Function to delete a remote folder.

For student use: No


* **Parameters**

    **folder** – Folder to be deleted.



* **Returns**

    None



#### formatted_sensor_data()
Reads out all roomba sensors and formats the results into a text that can be printed to the console.

For student use: Yes


* **Returns**

    Formatted text containing all sensor values.



#### get_adc()
Get all the analog values from the seeed ADC shield, as percentages in the range 0-100

For student use: Yes


* **Returns**

    A list of values.



#### get_bumper_data(binary=False)
Gets the roomba bumper data.

For student use: Yes


* **Parameters**

    **binary** – Boolean, specifies whether the raw or the binary values should be returned.



* **Returns**

    A list of values.



#### get_external_sensor(sensor)
Generic function to get sensor readings from sensors that are not attached to the Seeed shield and are not roomba sensors.

For student use: No


* **Parameters**

    **sensor** – A string specifying which sensor to read.



* **Returns**

    Sensor data



#### get_roomba_sensors()
Gets the values of all roomba sensors.

For student use: Yes


* **Returns**

    A dictionary of sensors values



#### get_thermal_image(plot=False)
Gets the image from the thermal camera.

For student use: Yes


* **Parameters**

    **plot** – boolean, should be the image be plotted?



* **Returns**

    A numpy array of temperature values (pixels).



#### move(distance)
Moves the robot foward by a given distance.

For student use: Yes


* **Parameters**

    **distance** – distance in mm



* **Returns**

    A return message from the robot.



#### print_log(text, level='i')
Function that handles writing text to the log.

For student use: No


* **Parameters**

    
    * **text** – Log message as string.


    * **level** – The level of importance of the message: (i)nfo, (w), or (c)ricical



#### remote_folder_exists(folder)
Function testing whether a folder exists on the raspberry.

For student use: No


* **Parameters**

    **folder** – The folder to be tested.



* **Returns**

    Boolean



#### remote_server_process()
A function implementing the process of reading the output generated by the server and printing it to the local console.

For student use: No


* **Returns**

    None.



#### send_command(command, port, answer=True)
Low level function sending a string command to the remote server.

For student use: No


* **Parameters**

    
    * **command** – Command as a string.


    * **port** – Port to use


    * **answer** – Boolean specifying whether an answer should be read out.



* **Returns**

    The returned data, if any.



#### send_raw_command(command)
Sends a raw string to the server. The server will process this string as a command for the robot.

For student use: No


* **Parameters**

    **command** – A string



* **Returns**

    None



#### set_display(text)
Sets the display screen of the root to a specified text value.

For student use: Yes


* **Parameters**

    **text** – The message to be shown. Only the first 4 characters can be displayed.



* **Returns**

    A return message from the robot.



#### set_motors(left, right)
A low level function to set the speed of the motors of the roomba.

For student use: Yes


* **Parameters**

    
    * **left** – Left speed as an integer in the range -500,500 mm/s


    * **right** – Right speed as an integer in the range -500,500 mm/s



* **Returns**

    A return message from the robot.



#### set_velocity(linear, angular)
Sets the linear and angular velocity of the roomba.

For student use: Yes


* **Parameters**

    
    * **linear** – Linear speed in mm/s


    * **angular** – Angular speed in degrees/s



* **Returns**

    None



#### start_remote_server()
Starts the remote server as a Python thread.

For student use: No


* **Returns**

    None



#### stop_remote_python()
Stops all Python processes on the remote raspberry pi.

For student use: No


* **Returns**

    The return value as generated by the raspberry pi.



#### stop_remote_server()
Sends a command stopping the remote server on port 12345

For student use: No


* **Returns**

    None



#### test_communication(message=[])
Function to test the communication between the host computer and the raspberry. Sends a test string to the raspberry and prints a returned message.

For student use: No


* **Parameters**

    **message** – A list of message parts to be sent.



* **Returns**

    None, the function prints output to the console.



#### toggle_logging(state=True)
This functions can be used to toggle whether logging messages are generated and written to the console.

For student use: No


* **Parameters**

    **state** – Boolean



* **Returns**

    None



#### turn(degrees)
Turns the robot a number of degrees.

For student use: Yes


* **Parameters**

    **degrees** – turn angle in degrees.



* **Returns**

    A return message from the robot.



#### upload_files(verbose=False)
This function uploads all the files specified in filelist.txt to the raspberry pi.

For student use: No


* **Parameters**

    **verbose** – Boolean



* **Returns**

    None



### PD2030.roomba.Client.get_bumper_data(sensor_data, binary=False)
Helper function to extract the bumper data. Should not be called directly.

For student use: No


* **Parameters**

    
    * **sensor_data** – raw sensor data


    * **binary** – boolean



* **Returns**

    list of bumpter values


# Maestro board documentation


### class PD2030.maestro.Board.Board(ser_port=None, verbose=True)
This class is used to communicate with the maestro-based board

For student use: Yes


* **Parameters**

    
    * **ser_port** – The port used for serial communication. If omitted, the code will try to find the port.


    * **verbose** – Boolean.



#### calibrate_photo()
Function to calibrate the photocell. A number of measurements will be taken. The recorded minimum and 
maximum values are used to normalize subsequent measurements.


* **Returns**

    Minimum and maximum value.



#### calibrate_pot()
Function to calibrate the potentiometer. A number of measurements will be taken. The recorded minimum and 
maximum values are used to normalize subsequent measurements.


* **Returns**

    Minimum and maximum value.



#### get_dial()
Get the normalized level of the potentiometer.


* **Returns**

    float
    Level of the potentiometer in the range [0, 1].



#### get_photo()
Gets the normalized level of the photocell.


* **Returns**

    float
    Level of the photocell in the range [0, 1].



#### set_led1(value)
Set state of LED 1.


* **Parameters**

    **value** (*Bool*) – State of LED 1.



* **Returns**

    None



#### set_led2(value)
Set state of LED 2.


#### set_leds(l1, l2)
Shortcut to set both LEDs at the same time.


* **Parameters**

    
    * **l1** (*Bool*) – State of LED 1


    * **l2** (*Bool*) – State of LED 2



* **Returns**

    None



#### set_servo1(position, raw=False)
Set the position of servo 1.


* **Parameters**

    
    * **position** (*Float*) – Normalized target position [0, 1] for the servo.


    * **raw** (*Bool*) – If true, position is given in steps.



* **Returns**

    None



#### set_servo2(target, raw=False)
Set the position of servo 2.


#### stop_all()
Set all motors to a neutral position and switch of both LEDs.


* **Returns**

    None

 
Arduino DHT11 Temperature and Humidity Web Monitor
==================================================

Project Overview
----------------

This project uses an Arduino with a DHT11 sensor to measure temperature and humidity, and displays the data on a web page using a Flask web application. The Arduino reads data from the DHT11 sensor and sends it to a Flask server through the serial port. The Flask app continuously updates and displays this data in real-time on a simple webpage.

Technologies Used
-----------------

*   **Arduino** with DHT11 sensor
*   **Flask** - a Python web framework
*   **Serial Communication** between Arduino and Flask
*   **HTML** for creating the web interface

Libraries Used
--------------

*   **DHT sensor library** for Arduino (used to read data from the DHT11 sensor)
*   **Flask** for creating the web server in Python
*   **PySerial** for serial communication between Arduino and Flask

Installation Instructions
-------------------------

### 1\. Arduino Setup

*   Connect the **DHT11 sensor** to your Arduino as follows:
    *   **VCC** to **5V**
    *   **GND** to **GND**
    *   **Data Pin** to **A0** (or any other available pin on your Arduino)
*   Install the **DHT sensor library** in Arduino IDE:
    *   Go to **Sketch** > **Include Library** > **Manage Libraries**
    *   Search for **DHT sensor library** and install it
*   Upload the provided Arduino code to your Arduino board.

### 2\. Flask Web Server Setup

*   Install the required Python libraries:
    
    pip install flask pyserial
    
*   Create a Python file for the Flask app or clone this repository, and add the Flask code provided.
*   Make sure to replace the serial port with the correct one for your system (e.g., \`COM5\` for Windows or \`/dev/ttyUSB0\` for Linux).
*   Run the Flask app using:
    
    python app.py
    

### 3\. Accessing the Web Application

*   Open your web browser and visit **http://:5001/** to view the temperature and humidity.
*   The webpage will automatically update with the latest data from the Arduino every minute.

Additional Notes
----------------

*   If you're using Windows, make sure the Arduino is connected to the correct COM port, and Flask can access it.
*   The Flask app will display the temperature and humidity in real-time and update every minute as the Arduino sends new data.

from flask import Flask, render_template_string
import serial
import time


app = Flask(__name__)


ser = serial.Serial('COM5', 9600, timeout=1) # port  depends on which usb port is used by the arduino, You can check on Windows computer management -> device manager


temperature = None
humidity = None


@app.route('/')
def index():
    global temperature, humidity

   
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        if "Temperature:" in data and "Humidity:" in data:
            parts = data.split(", ")
            temperature = parts[0].split(":")[1].strip()  
            humidity = parts[1].split(":")[1].strip()     

    
    return render_template_string("""
            <!DOCTYPE html>
            <html lang="hu">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Temperature and Humidity</title>
                <style>
                    body {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        background-color: #f4f4f4;
                        font-family: Arial, sans-serif;
                        margin: 0;
                    }
                    .container {
                        background: white;
                        padding: 20px 40px;
                        border-radius: 15px;
                        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                        text-align: center;
                    }
                    h1, h2 {
                        margin: 10px 0;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>Temp: {{ temperature }} </h2>
                    <h2>Humidity: {{ humidity }} </h2>
                </div>
            </body>
            </html>
        """, temperature=temperature, humidity=humidity)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8080, debug=False) #you can change the ip and port if neccessary

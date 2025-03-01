#include <DHT.h>

#define DHTPIN A0  // DHT11 pin
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  
 
Serial.print("Temperature: ");
Serial.print(t, 1);  
Serial.print(" C, Humidity: ");
Serial.print(h, 1); 
Serial.println(" %");

  
  delay(60000);  //  1 min updates
}

 // DHT library need to install

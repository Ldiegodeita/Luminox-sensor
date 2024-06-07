#include <SoftwareSerial.h>
//Diego Rojas de Ita 2024
//Code you can use in arduino UNO for sending commands directly to Luminox sensor
// Sensor will retrieve a 3 component line corresponding to oxygen partial pressure, %concentration, Temperature, and atmospheric pressure.
// Define the pins for RX and TX
const int rxPin = 8;  // Pin 10 connected to TX of LuminOx (Pin 3)
const int txPin = 9;  // Pin 11 connected to RX of LuminOx (Pin 4)

// Create a software serial port
SoftwareSerial mySerial(rxPin, txPin);

void setup() {
  // Start the hardware serial port for debugging
  Serial.begin(9600);
  
  // Start the software serial port for LuminOx communication
  mySerial.begin(9600);
  
  // Ensure power is applied to the sensor before communication
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);

  // Allow some time for the sensor to initialize
  // delay(1000);
  
  //Serial.println("LuminOx Sensor listo");
}

void loop() {
  // Check if data is available from the monitor serial
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    sendCommand(command);
  }

  // Check if data is available from the sensor
  if (mySerial.available() > 0) {
    String sensorData = mySerial.readStringUntil('\n');
    //Serial.println("ARD_sensor: " + sensorData);
    Serial.println(sensorData);
  }
}

void sendCommand(String command) {
  // Append the terminator to the command
  command += "\r\n";
  
  // Send the command to the sensor
  mySerial.print(command);

  // Print the command sent for debugging
  // Serial.print("ARD_ComSENT: ");
  // for (int i = 0; i < command.length(); i++) {
  //   Serial.print(command[i], HEX);
  //   Serial.print(" ");
  // }
  // Serial.println();
  
  // Wait a bit for the sensor to process the command
  //delay(100);  // 100ms delay
}

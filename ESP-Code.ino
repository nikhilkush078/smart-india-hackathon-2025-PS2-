#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "RESISTOR_Game_AP";
const char* password = "password123";

ESP8266WebServer server(80);

// Pin connected to the MOSFET Gate
const int mosfetPin = D1; 
const int frequency = 50; // 50Hz for the transformer
const int dutyCycle = 128; // 50% duty cycle (0-255)

void triggerHapticFeedback() {
  Serial.println("Shock Triggered: 50Hz Switching Active");
  
  // Start 50Hz PWM signal
  analogWriteFreq(frequency);
  analogWrite(mosfetPin, dutyCycle);
  
  delay(200); // Duration of the physical feedback [cite: 773, 811]
  
  // Stop switching
  analogWrite(mosfetPin, 0);
  server.send(200, "text/plain", "Feedback Executed");
}

void setup() {
  Serial.begin(115200);
  pinMode(mosfetPin, OUTPUT);
  digitalWrite(mosfetPin, LOW);

  // Setup ESP8266 as Access Point [cite: 736, 790]
  WiFi.softAP(ssid, password);
  Serial.print("AP IP Address: ");
  Serial.println(WiFi.softAPIP());

  server.on("/shock", triggerHapticFeedback);
  server.begin();
}

void loop() {
  server.handleClient();
}

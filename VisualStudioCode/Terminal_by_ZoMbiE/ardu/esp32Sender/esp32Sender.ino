#include "softTimer.h"

bool fEOL = true;

void send() {
  if (fEOL)
    Serial.println(String(millis()) + " n");
  else
    Serial.print(String(millis()) + " non");
}

SoftTimer timer(1000, send, false);

String inputString = "";     
bool stringComplete = false;  

void setup() {
  Serial.begin(115200);
  inputString.reserve(200);
  timer.start();
}

void loop() {
  if (stringComplete) {
    int num = inputString.toInt();
    if (num > 0) {
      timer.setInterval(num);
    }
    if (inputString == "n\n")
      fEOL = true;
    if (inputString == "non\n")      
      fEOL = false;
    //Serial.print(inputString);
    inputString = "";
    stringComplete = false;
  }
  timer.update();
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

#include "softTimer.h"

void send() {
  Serial.println(millis());
}

SoftTimer timer(1000, send, false);

String inputString = "";      // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(9600);
  inputString.reserve(200);
  timer.start();
}

void loop() {
  if (stringComplete) {
    Serial.println(inputString);
    int num = inputString.toInt();
    if (num >= 10) {
      Serial.println("ok");
      timer.setInterval(num);
      // timer.stop();
      // timer.restart(num, send, true);
    }
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

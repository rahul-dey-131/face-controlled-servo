#include <Servo.h>

int servoPin = 6;
Servo eye;

int angle = 90;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  eye.attach(servoPin);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    angle = (Serial.readStringUntil('\r')).toInt();
    eye.write(angle);
  }
}

const int FingerSensorPin = 2;

void setup() {
  Serial.begin(115200);
  pinMode(FingerSensorPin, INPUT);
}

void loop() {
  Serial.println(!digitalRead(FingerSensorPin));
  delay(100);
}

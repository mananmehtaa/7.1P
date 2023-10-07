const int photodiodePin = A0; // Analog pin for photodiode
const int relayPin = 2;       // Digital pin to control relay

int lightThreshold = 500; // Adjust this value based on ambient light conditions
int detectionRange = 200; // Define the range within which a person is detected

void setup()
{
  pinMode(photodiodePin, INPUT);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW); // Initially, turn off the relay
}

void loop()
{
  int lightIntensity = analogRead(photodiodePin);

  if (lightIntensity < lightThreshold)
  {
    // Person detected within the range, turn on the light
    digitalWrite(relayPin, HIGH);
    delay(1000); // Wait for a second to stabilize the detection
  }
  else
  {
    // No person detected, turn off the light
    digitalWrite(relayPin, LOW);
  }
}

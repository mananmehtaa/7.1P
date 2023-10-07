#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C address 0x27, 16 column and 2 rows

void setup()
{
    lcd.begin(16, 2);   // Initialize LCD
    Serial.begin(9600); // Start serial communication
}

void loop()
{
    if (Serial.available() > 0)
    {
        String message = Serial.readStringUntil('\n');
        lcd.clear();        // Clear the LCD
        lcd.print(message); // Print the received message
    }
    delay(500); // Delay for readability
}

# Import necessary libraries
import serial
import time

# Establish serial connections to Arduino Nano boards
arduino1 = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  
arduino2 = serial.Serial('/dev/ttyACM1', 9600, timeout=1)  

# Function to send message to Arduino Nano boards
def send_to_arduino(arduino, message):
    arduino.write(message.encode('utf-8'))
    arduino.flush()

# Main program
counter = 4  # Initial counter value
try:
    while True:
        # Display counter on LED display
        display_message = f"Counter: {str(counter).zfill(2)}"
        send_to_arduino(arduino1, display_message)  # Sending message to the first Arduino Nano
        send_to_arduino(arduino2, display_message)  # Sending message to the second Arduino Nano
        
        # Simulating motion sensor detection
        motion_detected = True  # Replace this with actual motion sensor input
        if motion_detected:
            print("Motion detected! LED bulb is ON.")
            # Code to control LED bulb ON
        else:
            print("No motion detected. LED bulb is OFF.")
            # Code to control LED bulb OFF

        counter += 1  # Increment the counter for the next iteration
        time.sleep(1)  # Wait for 1 second before the next iteration

except KeyboardInterrupt:
    print("Program terminated.")
    arduino1.close()  # Close the serial connection to the first Arduino Nano
    arduino2.close()  # Close the serial connection to the second Arduino Nano

import serial
import time

# Attempt to create a serial connection
try:
    ser = serial.Serial('/dev/pts/2', 9600, timeout=1)  # Adjust as needed
    print(f"Connected to {ser.portstr}")  # Confirm connection
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    try:
        # Ensure command is sent as a single byte
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")  # Show command in hex for clarity
    except Exception as e:
        print(f"Failed to send command: {e}")

# Move motor forward
print("Rover moving forward...")
send_command(64 + 43)  # Move motor 1 forward at medium speed
send_command(192 + 43)  # Move motor 2 forward at medium speed
time.sleep(2)  # Simulate running for 2 seconds

# Stop motors
print("Rover stopping...")
send_command(64)  # Stop motor 1
send_command(192)  # Stop motor 2
time.sleep(1)  # Simulate pause for a second

# Move motor backward
print("Rover moving backward...")
send_command(64 - 43)  # Move motor 1 backward at medium speed
send_command(192 - 43)  # Move motor 2 backward at medium speed
time.sleep(2)  # Simulate running for 2 seconds

# Stop motors
print("Rover stopping...")
send_command(64)  # Stop motor 1
send_command(192)  # Stop motor 2

# Close the serial connection
ser.close()
print("Serial connection closed.")


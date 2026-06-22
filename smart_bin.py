import time

print ("This is gonna be a pretty cool bin, I hope it works!")

#I am working on a smart bin that can detect when it is full and send a notification to the user's phone. 

while True:
    try:
        bin_level = int(input("Enter the current level(%) of the bin (0-100): "))
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def check_bin_level(bin_level):
    while bin_level < 0 or bin_level > 100:
        print("Invalid bin level! Please enter a value between 0 and 100.")
        try:
            bin_level = int(input("Enter the current level(%) of the bin (0-100): "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    if bin_level == 100:
            print("The bin is full! Sending notification to the user's phone...")
    elif bin_level >= 80:
        print("The bin is almost full! Sending notification to the user's phone...")
    elif bin_level >= 50:
        print("Past half!! Sending notification to the user's phone...")
    else:
        print("The bin is not full yet. No notification sent.")

def detect_motion():
    # Simulating motion detection (in a real scenario, this would be replaced with actual sensor data)
    motion_detected = False  # Change this to True to simulate motion detection
    if motion_detected:
        print("Opening the bin lid...")
    else:
        print("No motion detected, keeping the bin lid closed.")


while True:  
    check_bin_level(bin_level)
    detect_motion()
    time.sleep(15)  # Simulating a delay between checks (e.g., every 15 seconds)

    try:
        bin_level = int(input("Enter the current level(%) of the bin (0-100): "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

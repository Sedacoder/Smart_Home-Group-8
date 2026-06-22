print ("This is gonna be a pretty cool bin, I hope it works!")

#I am working on a smart bin that can detect when it is full and send a notification to the user's phone. 

bin_level = int(input("Enter the current level(%) of the bin (0-100): "))
def check_bin_level(bin_level):
    if bin_level < 0 or bin_level > 100:
        print("Invalid bin level! Please enter a value between 0 and 100.")
        return False
    return True

check_bin_level(bin_level)

if check_bin_level(bin_level):
        if bin_level == 100:
            print("The bin is almost full! Sending notification to the user's phone...")
        if bin_level >= 80:
            print("The bin is almost full! Sending notification to the user's phone...")
        else:
            print("The bin is not full yet. No notification sent.")





 
motion_detected = True

if motion_detected:
    print("Opening the bin lid...")
else:
    print("No motion detected, keeping the bin lid closed.")


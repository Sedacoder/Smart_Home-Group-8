print ("This is gonna be a pretty cool bin, I hope it works!")

#I am working on a smart bin that can detect when it is full and send a notification to the user's phone. 

bin_level = int(input("Enter the current level of the bin (0-100): "))

if bin_level == 100:
    print("Empty Bin now!")
elif bin_level > 80:
    print("Bin is almost full, please empty it soon!")
elif bin_level > 50:
    print("Bin is getting full, please keep an eye on it!")
else:
    print("Bin is not full yet, stay clean")
 
motion_detected = True

if motion_detected:
    print("Opening the bin lid...")
else:
    print("No motion detected, keeping the bin lid closed.")
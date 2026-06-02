import time
import random

# Setup our safety limit
SAFETY_LIMIT = 50.0  # If water goes above 50 cm, sound the alarm
water_level = 10.0   # Starting water level in cm

print(" Flood Sensor Active. Monitoring water levels...\n")

# Run the sensor loop
while True:
    # Simulate the water level rising by a random amount between 5 and 15 cm
    water_level += random.uniform(5.0, 15.0)

    print(f"Current Water Level: {water_level:.1f} cm")

    # Check if a flood is about to happen
    if water_level >= SAFETY_LIMIT:
        print("\n ALARM ")
        print("WARNING: Water level has exceeded the safety limit!")
        print(" FLOOD IMMINENT - PLEASE EVACUATE THE AREA!")
        break  # Stops the program after the alarm triggers

    time.sleep(1)  # Wait 1 second before checking again

# Additional checks after evacuation
print("\nEvacuate immediately!")

water_level = 47.3
water_level = 40.5

if not isinstance(water_level, int):
    print(True)
else:
    print(False)
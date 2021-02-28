# 1 rod = 5.0292 meters
ROD = 5.0292

# 1 furlong = 40 rods
FURLONG = 40

# 1 mile = 1609.34 meters
MILE = 1609.34

# 1 foot = 0.3048 meters
FOOT = 0.3048

# average walking speed is 3.1 miles per hour
WALKING_SPEED = 3.1 / 60

rods = input("Input rods:")

rods = float(rods)
meters = rods * ROD
feet = rods * ROD / FOOT
miles = rods * ROD / MILE
furlongs = rods / FURLONG
minutes = miles / WALKING_SPEED


print("Your input:", rods, "rods.", "\n\n")
print("Conversions")
print("Meters:", meters)
print("Feet:", feet)
print("Miles:", miles)
print("Furlongs:", furlongs)
print("Minutes to walk", rods, "rods:", minutes)
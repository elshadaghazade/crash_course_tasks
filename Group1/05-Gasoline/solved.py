# You can find these measures on the web (try wikipedia), but just in case:
# • 1 gallon is equivalent to 3.7854 liters
# • 1 barrel of oil produces 19.5 gallons of gas (approximately, can vary depending on the oil
# source. This number will work for us). FYI, a barrel is 42 gallons.
# • 1 gallon of gas produces approximately 20 pounds of CO2. Again, good enough
# • 1 gallon of gas produces 115,000 BTU (British Thermal Units). 1 gallon of ethanol
# produces 75,700 BTU.
# • God knows what the cost should be, but let’s peg it at $4.00/gallon


gallons = input("Please enter the number of gallons of gasoline: ")
gallons = float(gallons)
liters = gallons * 3.7854
barrels = gallons / 19.5
co2 = gallons / 20
ethanol = gallons * 115000 / 75700
price = gallons * 4


print(gallons, "gallons is the equivalent of", liters, "liters")
print(gallons, "gallons of gasoline requires", barrels, "of oil")
print(gallons, "gallons of gasoline produces", co2, "pounds of CO2")
print(gallons, "gallons of gasoline is energy equivalent to", ethanol, "gallons of ethanol")
print(gallons, "gallons of gasoline requires", price, "US dollars")
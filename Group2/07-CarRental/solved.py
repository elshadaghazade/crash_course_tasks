while True:
    category = input("Type your category: ").strip().lower()
    
    if not category in "bdwq":
        print("You've entered wrong category. Try again!")
        continue
    else:
        break
        
while True:
    before = input("Odometer reading at the start: ").strip()
    after = input("Odometer reading at the end: ").strip()
    
    if not before.isdigit() or not after.isdigit():
        print("Odometer reading is wrong. Try again!")
        continue
    
    before = int(before)
    after = int(after)
    
    if after < before:
        print("Odometer start reading is greater that end reading. Try again!")
        continue
    else: 
        break
        

while True:
    days = input("Type number of days: ").strip()
    if not days.isdigit():
        print("Number of days is wrong. Try again!")
        continue
    else:
        days = int(days)
        break
        
mileage = after - before

billing = 0
if category == 'b':
    billing = days * 40
    billing += mileage * 0.25
elif category == 'd':
    billing = days * 60
    if mileage > days * 100:
        mileage -= days * 100
        billing += mileage * 0.25
elif category == 'w':
    import math
    
    billing = 190
    weeks = math.ceil(days / 7)
    if mileage > weeks * 900 and mileage <= weeks * 1500:
        billing += 100
    elif mileage > weeks * 1500:
        billing = weeks * 200
        mileage -= weeks * 1500
        billing += mileage * 0.25
        
print("Your billing:", billing, "$")
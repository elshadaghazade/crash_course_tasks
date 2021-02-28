def ask_numbers ():
    while True:
        try:
            wall_length = float(input("Type a length of wall:"))
            break
        except:
            print("Data is not a number. Try again!")
            continue
            
    while True:
        try:
            flower_distance = float(input("Distance between flowers: "))
            break
        except:
            print("Data is not a number. Try again!")
            continue
            
    while True:
        try:
            flower_depth = float(input("Depth of flowerbed: "))
            break
        except:
            print("Data is not a number. Try again!")
            continue
            
    while True:
        try:
            grayplace_depth = float(input("Depth of gray area: "))
            break
        except:
            print("Data is not a number. Try again!")
            continue
            
    return wall_length, flower_distance, flower_depth, grayplace_depth


def calculate_flowers_count(wall_length, flower_distance):
    import math
    
    steps = wall_length / flower_distance
    
    triangle = ((steps / 2) ** 2) / 2
    circle = math.pi * (steps / 2) ** 2
    flower_total_counts = triangle * 4 + circle
    
    return triangle, circle, flower_total_counts


def calculate_sands(wall_length, flower_total_counts, flower_depth, grayplace_depth):
    import math
    
    grayplace_area = wall_length / 2


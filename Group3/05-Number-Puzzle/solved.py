number = "12995678"
split = 4
step = len(number) // split

is_progressive = True

start = 0
tmp = 0

while True:
    tmp2 = number[start:start + step]
    if int(tmp2) < tmp:
        is_progressive = False
        break
    else:
        tmp = int(tmp2)
        
    start += step
    if start >= len(number):
        break
        
print(is_progressive)
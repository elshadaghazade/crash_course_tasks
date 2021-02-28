# istifadəçinin doğulduğu ili soruşun və neçə yaşda olduğunu hesablayıb print edin
# ==============================================
year = input("Doğulduğunuz ili qeyd edin:")
age = 2018 - int(year)
print("Sizin yaşınız:", age)
# ==============================================

# 2022-ci ildə neçə yaşı olacaq?
# ==============================================
age_in_2022 = age + 2022 - 2018
print(f"Sizin 2022-ci ildə {age_in_2022} yaşınız olacaq")
# ==============================================

# istifadəçinin yaşının kubunu tapın
# ==============================================
age = age ** 3
print("İstifadəçinin yaşının kubu:", age)
# ==============================================

# 0-dan 100-ə qədər olan bütün cüt rəqəmləri print edin
# ==============================================
for i in range(100):
    if not i % 2:
        print(i)
# ==============================================

# 1-dən 100-ə qədər bütün 3-ə və 5-ə bölünən ədədlərin cəmini tapın (terner operatoru istifadə etməklə)
# ==============================================
sum = 0
for i in range(1,100):
    sum = sum + i if not i % 3 or not i % 5 else sum
print("Cəmi:", sum)
# ==============================================

# iki rəqəmin ən böyük ortaq bölünənini tapın
# ==============================================
a = input("birinci rəqəmi daxil edin: ")
b = input("ikinci rəqəmi daxil edin: ")

a = int(a)
b = int(b)

bigger = a if a > b else b
ebob = 0
for i in range(1,bigger):
    if not a % i and not b % i and ebob < i:
        ebob = i

print(f"{a} və {b} rəqəmlərinin ən böyük ortaq böləni:", ebob)
# ==============================================
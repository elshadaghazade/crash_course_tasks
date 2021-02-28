a = 1144

# bin() funksiyasının gördüyü işin eynisini edən kodlar yazın
# ===========================================================
remainder = a % 2
binary = str(remainder)

while a > 1:
    a //= 2
    remainder = a % 2
    binary += str(remainder)   

binary = "0b" + binary[::-1]
print(binary)
# ===========================================================

# oct() funksiyasının gördüyü işin eynisini edən kodlar yazın
# ===========================================================
remainder = a % 8
octal = str(remainder)

while a > 1:
    a //= 8
    remainder = a % 8
    octal += str(remainder)   

octal = "0b" + octal[::-1]
print(octal)
# ===========================================================

# hex() funksiyasının gördüyü işin eynisini edən kodlar yazın
# ===========================================================
remainder = a % 8
hexadecimal = str(remainder)

while a > 1:
    a //= 8
    remainder = a % 8
    hexadecimal += str(remainder)   

hexadecimal = "0b" + hexadecimal[::-1]
print(hexadecimal)
# ===========================================================

# int() funksiyasının gördüyü işin eynisini edən kodlar yazın
# ===========================================================
a = bin(1144)
print("a dəyişənin dəyəri", a, "\na dəyişənin tipi", type(a))

base = 2
# decimal dəyişəninə bütün hesablamalarımızı yığacayıq.
# başlanğıc dəyəri sıfır edirik
decimal = 0

# sətrin əvvəlindən 0b, 0o və ya 0x prefikslərini silirik
# və hesablamaq üçün sətri reverse edirik. 10-luq say sisteminə çevirmə
# qaydasını yadınıza salın
a = a[:1:-1]
print("a dəyişənin reversed dəyəri", a)

# sətrin hər bir simvolunu sadalayırıq
for index, value in enumerate(a):
    # base-ə əsasən dərəcəni çıxarırıq
    power = base ** index
    # əgər base 2-lik say sistemidirsə onda o yalnızca 1 və sıfırlardan ibarətdir
    if base == 2:
        if value == "1":
            decimal += 1 * power
        elif value == "0":
            decimal += 0 * power
    # əgər base 8-likdirsə onda value 0-dan 7-yə qədər dəyər ala bilər
    elif base == 8:
        if value == "1":
            decimal += 1 * power
        elif value == "2":
            decimal += 2 * power
        elif value == "3":
            decimal += 3 * power
        elif value == "4":
            decimal += 4 * power
        elif value == "5":
            decimal += 5 * power
        elif value == "6":
            decimal += 6 * power
        elif value == "7":
            decimal += 7 * power
    # əgər base 16-lıqdırsa onda value 0-dan 9-a və A,B,C,D,E,F dəyərləri ala bilər
    elif base == 16:
        if value == "1":
            decimal += 1 * power
        elif value == "2":
            decimal += 2 * power
        elif value == "3":
            decimal += 3 * power
        elif value == "4":
            decimal += 4 * power
        elif value == "5":
            decimal += 5 * power
        elif value == "6":
            decimal += 6 * power
        elif value == "7":
            decimal += 7 * power
        elif value == "8":
            decimal += 8 * power
        elif value == "9":
            decimal += 9 * power
        elif value == "A":
            decimal += 10 * power
        elif value == "B":
            decimal += 11 * power
        elif value == "C":
            decimal += 12 * power
        elif value == "D":
            decimal += 13 * power
        elif value == "E":
            decimal += 14 * power
        elif value == "F":
            decimal += 15 * power
            
print("decimal dəyişənin dəyəri", decimal, "\ndecimal dəyişənin tipi", type(decimal))
# ===========================================================
# Listi tərsinə çevirən (reverse) rekursiv funksiya yazın
# =============================================================

# =============================================================

# Aşağıdakı listin tərkibindəki rəqəmlərin cəmini hesablayıb qaytaran rekursiv funksiya yazın. Əgər element string olarsa onda həmən stringin uzunluğunu rəqəm götürün (cavab 5102 olacaq)
# =============================================================
somelist = [12, 45, 87, 
                [65, 34, 76],
                [34, 76, 43,
                    [8, 446, 23, 48,
                        [23,56,43,787],
                        {"key1": 543, "key2": 65, "key3": [54,2,335,76]}
                    ],
                    54, 23, 76, 32
                ],
                23, 65, 
                {"key1": 54, "key2": 234, "key3": {"key1": 234, "key2": [1,245, 56, 45, (45,3,34,56)]}}
                ,23, 765, 22, "techacademy", "python", "coding", "bootcamp"
           ]

def calc(somelist):
    summ = 0

    for i in somelist:
        if isinstance(i, int) or isinstance(i, float):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, dict):
            summ += calc(list(i.values()))
        elif isinstance(i, list) or isinstance(i, tuple):
            summ += calc(i)
            
    return summ

print(calc(somelist))
# =============================================================

# Aşağıdakı listin tərkibindəki rəqəmlərdən ancaq 3-ə və 5-ə bölünənlərin cəmini hesablayıb qaytaran rekursiv funksiya yazın. Əgər element string olarsa onda həmən stringin uzunluğunu rəqəm götürün (cavab 900 olacaq)
# =============================================================
somelist = [12, 45, 87, 
                [65, 34, 76],
                [34, 76, 43,
                    [8, 446, 23, 48,
                        [23,56,43,787],
                        {"key1": 543, "key2": 65, "key3": [54,2,335,76]}
                    ],
                    54, 23, 76, 32
                ],
                23, 65, 
                {"key1": 54, "key2": 234, "key3": {"key1": 234, "key2": [1,245, 56, 45, (45,3,34,56)]}}
                ,23, 765, 22, "techacademy", "python", "coding", "bootcamp"
           ]

def calc(somelist):
    summ = 0

    for i in somelist:
        if isinstance(i, int) or isinstance(i, float):
            if not i % 3 and not i % 5:
                summ += i
        elif isinstance(i, str):
            if not len(i) % 3 and not len(i) % 5:
                summ += len(i)
        elif isinstance(i, dict):
            summ += calc(list(i.values()))
        elif isinstance(i, list) or isinstance(i, tuple):
            summ += calc(i)
            
    return summ

print(calc(somelist))
# =============================================================

# Aşağıdakı listin tərkibində minimum integeri tapıb qaytaran rekursiv funksiya yazın
# =============================================================
somelist = [12, 45, 87, 
                [65, 34, 76],
                [34, 76, 43,
                    [8, 446, 23, 48,
                        [23,56,43,787],
                        {"key1": 543, "key2": 65, "key3": [54,2,335,76]}
                    ],
                    54, 23, 76, 32
                ],
                23, 65, 
                {"key1": 54, "key2": 234, "key3": {"key1": 234, "key2": [1,245, 56, 45, (45,3,34,56)]}}
                ,23, 765, 22, "techacademy", "python", "coding", "bootcamp"
           ]

def find_minimum(somelist):
    pass

print(find_minimum(somelist))
# =============================================================

# Aşağıdakı listin tərkibində verilmiş rəqəmi axtaran və onun bütün koordinatlarını qaytaran funksiya yazın
# =============================================================
somelist = [12, 45, 87, 
                [65, 34, 76],
                [34, 76, 43,
                    [8, 446, 23, 48,
                        [23,56,43,787],
                        {"key1": 543, "key2": 65, "key3": [54,2,335,76]}
                    ],
                    54, 23, 76, 32
                ],
                23, 65, 
                {"key1": 54, "key2": 234, "key3": {"key1": 234, "key2": [1,245, 56, 45, (45,3,34,56)]}}
                ,23, 765, 22, "techacademy", "python", "coding", "bootcamp"
           ]

def find_number(somelist, n):
    pass

print(find_number(somelist, 234))
# =============================================================

# İnteger tipini string tipinə çevirəcək rekursiv funksiya yazın (base nəzərə alınsın)
# =============================================================
def to_string(n, base=10):
       convert_string = "0123456789ABCDEF"
   if n < base:
      return convert_string[n]
   else:
      return to_string(n//base,base) + convert_string[n % base]

print(to_string(2835,16))
# =============================================================

# Parametrdən gələn inteqerin rəqəmlərinin cəmini hesablayan rekursiv funksiya yazın (integeri stringə çevirmədən)
# Nümunə: 
# sum_digits(345) -> 12
# sum_digits(45) -> 9 
# =============================================================
def sum_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_digits(int(n / 10))

print(sum_digits(345)) # -> 12
print(sum_digits(45)) # -> 9
# =============================================================

# Parametrdən gəlmiş integerdən sıfıra qədər hər ikinci rəqəmi rekursiv cəmləyəcək funksiya yazın: n + (n - 2) + (n - 4) ...
# Nümunə: 6 -> 6 + 4 + 2 + 0 = 12
# sum_series(6) -> 12
# sum_series(10) -> 30 
# =============================================================
def summ(n):
    if n < 1:
        return 0
    else:
        return n + summ(n - 2)

print(summ(6))
print(summ(10))
# =============================================================

# Parametrdən gələn integerin harmonik cəmini tapın.
# Nümunə:

# n = 7
# 1/7 + 1/6 + 1/5 + ... + 1 = 2.5928571428571425 
# =============================================================
def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))
    
print(harmonic_sum(7))
print(harmonic_sum(4))
# =============================================================
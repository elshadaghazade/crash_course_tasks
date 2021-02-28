# Əvvəlcə math modulunu import edirik.
# Əks halda onun imkanlarından yararlana bilməyəcəyik
import math

# math.ceil(x) - kəsr ədədini yuxarıya doğru yuvarlaqlaşdırma
# ====================================================
x = 12.1
print(f"{x} ədədinin yuxarı yuvarlaqlaşdırılmış dəyəri:", math.ceil(x))
# ====================================================

# math.ceil(x) funksiyasını özünüz yazmağa çalışın
# ====================================================
# 1. x dəyişəninin tam hissəsini çıxardırıq
tam = x // 1
# 2. "yuvarlaq" dəyişəni yaradıb müvəqqəti olaraq 0 dəyəri mənimsədirik
yuvarlaq = 0
# 3. Əgər tam hissəsi x dəyişənin özündən kiçikdirsə deməli x ədədi həqiqətən də kəsr ədədidir
if tam < x:
    # 3.1. tam hissənin üzərinə 1 əlavə edib onu yuvarlaq dəyişəninə mənimsədirik
    yuvarlaq = tam + 1
# 4. Əks halda x dəyişəni kəsr yox tam ədəd özündə saxlayır. Buna görə də onun yuvarlaqlaşdırılmış dəyəri elə özünə bərabərdir. yuvarlaq dəyişəninə sadəcə tam hissəni mənimsətmək kifayətdir.
else:
    yuvarlaq = tam

print(f"Süni yaratdığımız ceil {x} kəsr ədədini yuxarıya doğru yuvarlaqlaşdırdı:", yuvarlaq)
# =====================================================

# math.floor(x) - kəsr ədədini aşağıya doğru yuvarlaqlaşdırır
# ====================================================
x = 12.1
print(f"{x} ədədinin aşağıya yuvarlaqlaşdırılmış dəyəri:", math.floor(x))
# ====================================================

# math.floor(x) funksiyasını özünüz yazmağa çalışın
# ====================================================
# 1. x dəyişəninin tam hissəsini çıxardırıq
tam = x // 1
# 2. kəsr hissəni atırıq, yalnızca tam hissəni saxlayırıq
yuvarlaq = tam

print(f"Süni yaratdığımız ceil {x} kəsr ədədini aşağıya doğru yuvarlaqlaşdırdı:", yuvarlaq)
# ====================================================

# math.fabs(x) - ədədin müsbət dəyərini qaytarır
# ====================================================
x = -12.1
print(f"{x} ədədinin müsbət dəyəri:", math.fabs(x))
# ====================================================

# math.fabs(x) funksiyasını özünüz yazmağa çalışın
# ====================================================
# 1. əgər ədəd 0-dan kiçikdirsə onda onu mənfi birə vururuq və müsbət dəyəri alırıq
x = -12.1
result = 0
if x < 0:
    result = -1 * x
# 2. əgər ədəd sıfra bərabərdirsə və ya sıfırdan böyükdürsə onda ədədin özü bizə lazım olan cavabdır
else:
    result = x

print(f"Süni yaratdığımız fabs {x} ədədinin müsbət dəyərini qaytardı:", result)
# ====================================================

# math.isclose(a, b, rel_tol) - ədədlərin yaxınlığını hesablayır
# ====================================================
a = 1
b = 2
rel_tol = 0.5
print(f"{a} və {b} ədədləri", "yaxındır" if math.isclose(a, b, rel_tol=rel_tol) else "yaxın deyil")
# ====================================================

# math.isclose(a, b, rel_tol) funksiyasını özünüz yazmağa çalışın
# ====================================================
a, b = 1, 2
rel_tol = 0.5
result = False

# a və b dəyişənlərinin dəyərlərini onların böyük və kiçik olmalarına görə yerdəyişmə edirik
a, b = (a, b) if a > b else (b, a)

# iki dəyişən arasındakı fərqi tapırıq
difference = a - b
percent = difference / a
# tapılan fəqrin böyük dəyişənin neçə faizi etdiyini tapırıq percent = difference / a
# əgər fərq faizi rel_tol dəyişənin dəyərinə bərabər və ya kiçikdirsə onda bu dəyişənlər yaxındır
if percent <= rel_tol:
    result = True
else:
    result = False
    
print(f"{a} və {b} ədədləri", "yaxındır" if math.isclose(a, b, rel_tol=rel_tol) else "yaxın deyil")
# ====================================================
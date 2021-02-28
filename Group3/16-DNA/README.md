# DNA

Alimlər iki DNA-ların protein ardıcıllıqlarını yoxlayaraq aralarındakı oxşarlıq və fərqlilikləri tapırlar. DNA-lar arasındakı protein oxşarlığı nə qədər çox olarsa iki genin bir birinə yaxın olduğunu təsbit edirlər. Bu prosesə ardıcıllıq ortalaması (sequence alignment) deyilir. Bu qarşılaşmanı etmək üçün hər bir protein əlifbanın xüsusi hərfləri ilə işarələnir. 

## Example

iki DNA verilmişdir:

DNA 1: AA<span style="color:red;">T</span>A<span style="color:red;">ACG</span>AAA

DNA 2: AA<span style="color:red;font-weight:bold;">A</span>A<span style="color:red;">CGA</span>AAA

İndiki halda iki DNA arasındakı uyğunluq 6-dır, fərqlilik isə 4-dür.
Alim bu ortalamanı **-** (dash) əlavə edərək və ya silərək dəyişə bilər:

DNA 1: AA<span style="color:blue;">T</span>AACGAAA<span style="color:blue;">-</span>

DNA 2: AA<span style="color:blue;">-</span><span style="color:black;font-weight:bold;">A</span>ACGAAAA

Bu yerdəyişmə sayəsində uyğunluq daha da artır. İndi iki DNA arasında uyğunluq 9-dur, fərqlilik isə 2-dir.

## Program Specification

Sizin proqram istifadəçidən:

1. Ardıcıl olaraq iki fərqli uzunluqda string daxil etməsini istəməlidir. Stringlər əlifbada olan istənilən simvol ola bilər. Lakin elmi qaydada A, T, C, G olsa daha yaxşı olar.
2. Daha sonra istifadəçidən 4 komandadan birini daxil etməsini tələb etməlidir:
    - "a" - add, **-** (dash) daxil etmək üçün
    - "d" - delete, daxil edilmiş **-** (dash) işarələri silmək üçün
    - "s" - score, müqayisənin nəticəsini göstərmək üçün
    - "q" - quit, proqramdan çıxmaq üçün
3. **"a"** ***(Add)*** seçilən zaman zaman aşağıdakıları soruşmaq lazımdır:
    - hansı string-ə dash artırmaq istədiyini soruşmaq
    - seçilən string-də dash-i hasnı indeksə artırmaq. Əgər verilən index string-də yoxdursa onda **Error** çıxardaraq yenidən soruşmaq
4. **"d"** ***(Delete)*** seçilən zaman aşağıdakıları soruşmaq lazımdır
    - hansı string-dən dash-i silmək istədiyini soruşmaq
    - hansı indeksdən dash-i silmək. Əgər verilən index string-də yoxdursa onda **Error** çıxardaraq yenidən soruşmaq
5. **"s"** ***(Score)*** seçilən zaman iki sətir arasında oxşarlıqları və fərqləri hesablamaq.
    - Hər bir dash uyğunsuzluğu göstərir
    - Əgər bir string digərindən qısadırsa, avtomatik olaraq çatışmayan simvolların yerinə dash-lər artırmaq lazımdır
    - Hesabladıqdan sonra hər iki string-i alt-alta print etmək lazımdır.
        - Uyğun olan simvollar kiçik hərflərlə yazılmalıdır, hətta istifadəçi həmən simvolları böyük hərflərlə daxil etsə belə
        - Uyğun olmayan simvollar böyük hərflərlə yazılmalıdır, hətta istifadəçi həmən simvolları kiçik hərflərlə daxil etsə belə

## Example

```
String 1: aaabbbccc
String 2: aabbbccc

What do you want to do:
                    a (add)
                    d (delete)
                    s (score)
                    q (quit): s
Matches: 6 Mismatches: 3
Str1: aaAbbBccC
Str2: aaBbbCcc-

What do you want to do:
                    a (add)
                    d (delete)
                    s (score)
                    q (quit): a
Work on which string (1 or 2):2
Before what index: 2

What do you want to do:
                    a (add)
                    d (delete)
                    s (score)
                    q (quit): s
Matches: 8 Mismatches: 1
Str1: aaAbbbccc
Str2: aa-bbbccc

What do you want to do:
                    a (add)
                    d (delete)
                    s (score)
                    q (quit): d
Work on which string (1 or 2): 2
Delete what index: 2

What do you want to do:
                    a (add)
                    d (delete)
                    s (score)
                    q (quit): s
Matches: 6 Mismatches: 3
Str1: aaAbbBccC
Str2: aaBbbCcc-

What do you want to do:
                    a (add)
                    d (delete)
                    s (score)
                    q (quit): q
```



---

***Powered by [Elşad Ağazadənin Proqramlaşdırma Məktəbi](https://elshadaghazade.com)***

***Originally posted by Elshad Agayev***

***Please follow instructions on how you should solve this task***
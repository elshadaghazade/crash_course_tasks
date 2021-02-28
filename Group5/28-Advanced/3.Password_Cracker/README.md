# Password Cracker

Son on illikdə bütün kompüter sistemləri konfidensiallığı və təhlükəsizliyi qorumaq məqsədi ilə **password** konsepsiyasına keçid etdilər. Lakin bu bariyeri aşmaq üçün də müxtəlif yollar fikirləşildi. Bu tapşırıqda istifadə edəcəyimiz yollardan biri **brute force** üsuludur, digəri isə isə **dictionary**

**brute force** üsulu mümkün olan bütün simvol kombinasiyalarını bir araya gətirərək passcode-u tapmaqdır. Adətən hər çox insanlar şifrələri kiçik rəqəmlərdən təyin etdiyinə, sizin proqram ilk kombinasiyanı 4 rəqəmdən başlamalıdır (0000, 0001, 0002 və s.).

**dictionary** üsulu əvvəlcədən toplanmış və ehtimal edilmiş şifrələrin əsasında aparılır. Həmən şifrələr fayla yazılır, proqram isə o şifrələri bir bir oxuyaraq yoxlayır, doğru olanı tapır. Bu tapşırıq üçün şifrələrin siyahısına buradan baxa bilərsiniz: [rockyou.txt](./rockyou.txt) və [short_dict.txt](./short_dict.txt)

## Program Specification

Sizin proqram:
1. Əvvəlcə **brute force** metodundan istifadə edərək [brute_force.zip](./brute_force.zip) arxivinin şifrəsini qırmalıdır. Bunun üçün **itertools** və **string** modulundan istifadə edə bilərsiniz.
2. Daha sonra **dictionary** metodundan istifadə edərək [dictionary_attach.zip](./dictionary_attack.zip) arxivinin şifrəsini qırmalıdır. Bu şifrəni qırmaq üçün [rockyou.txt](./rockyou.txt) və ya [short_dict.txt](./short_dict.txt) fayllarından istifadə edə bilərsiniz.

## Assignment Notes

Divide-and-conquer qaydası siyasətdə olduğu kimi proqramlaşdırmada da çox vacibdir. Bu səbəbdən də siz proqramınızı aşağıdakı funksiyalara parçalasaz daha çox effektiv olar:

1. <span style="color:#666;">open_dict_file()</span> - Bu funksiya heç bir arqument qəbul etmir. Sadəcə dictionary faylını açaraq onun pointerini qaytarır.
2. <span style="color:#666;">open_zip_file(file_name)</span> - Bu funksiya açmaq istədiyiniz zip faylı açaraq onun pointerini sizə qaytarır.
3. <span style="color:#666;">brute_force_attack(zip_file)</span> - Arqument olaraq zip faylının pointerini qaytarır. Brute force üsulu ilə zip faylının şifrəsini taparaq qaytarır
4. <span style="color:#666;">dictionary_attack(zip_file, dict_file)</span> - funksiya iki arqument qəbul edir: 1. zip faylın pointerini 2. dictionary faylın pointerini.
5. Bütün açılan faylları **close()** etmək lazımdır.
# Roman Numerals

Rum qərəmləri 10-luq say sisteminə çevirəcək proqram yazın.

## Assignment Overview

Rum rəqəmləri I = 1, V = 5, X = 10, L = 50 və C = 100 simvollarından ibarətdir [http://en.wikipedia.org/wiki/Roman_numerals](http://en.wikipedia.org/wiki/Roman_numerals)

Bu simvolların kombinasiyasından digər ədədlər alınır. Misal üçün, CLXVII bizə 100 + 50 + 10 + 5 + 1 + 1 = 167 ədədi verəcək. Adətən bu simvollar dəyəri çox olandan az olana doğru düzülür, ona görə də biz hesablayarkən onları cəmləyirik. Lakin bəzi hallarda dəyəri kiçik olan rəqəm dəyəri böyük olan simvoldan əvvəl gələ bilir. Bu zaman böyükdən kiçik çıxılır və nəticəsi digərlərin üzərinə gəlinir. Misal üçün, XLIV rum rəqəmində X (10) simvolunun dəyəri L (50) simvolunun dəyərindən kiçikdir, I (1) isə V (5) simvolundan kiçikdir. Ona görə də hesablama bu qaydada aparılır: 50 - 10 + 5 - 1 = 40 + 4 = 44. Lakin dəyəri kiçik simvol dəyəri böyük olan simvoldan qabaq bircə dəfə gəlməlidir. Misal üçün, XL doğru kombinasiyadır, amma XXL yalnışdır. Çün ki, dəyəri kiçik olan X dəyəri böyük olan L-dən əvvəl iki dəfə təkrarlanır. XXX isə doğru kombinasiyadır, dəyəri isə: 10 + 10 + 10 = 30

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-|---|---|---|---|---|---|---|---|---|
| təkliklər | I | II | III | IV | V | VI | VII | VIII | IX |
| onluqlar | X | XX | XXX | XL | L | LX | LXX | LXXX | XC |
| yüzlüklər | C | CC | CCC |


## Program Specification

Sizin proqram:

1. İstifadəçidən rum rəqəmi daxil etməsini tələb etməlidir
2. Rum rəqəmi doğru deyilsə (kiçik rəqəm böyükdən əvvəl birdən çox gəlirsə və ya rum rəqəmi olmayan simvol daxil edilmişdirsə) onda istifadəçiyə xəbərdarlıq mesajı çıxararaq təkrar daxil etməsini tələb etməlidir. Bu hal doğru daxil olunana qədər davam etməlidir.
3. Rum rəqəminin onluq say sistemində olan qarşılığı print edilməlidir
4. İstifadəçiyə davam etmək istədiyini soruşmalıdır

---

***Powered by [Elşad Ağazadənin Proqramlaşdırma Məktəbi](https://elshadaghazade.com)***

***Originally posted by Elshad Agayev***

***Please follow instructions on how you should solve this task***
# Caesar Cypher

Yuli Sezar gizli məktublarda indiki dövr üçün çox sadə kriptoqrafiyadan istifadə edirdi. Əlifbada olan bütün hərfləri rəqəmləyirdi. Daha sonra bu hərfləri bir neçə dəfə əvvələ və ya axıra sürüşdürürdü. Bu zaman yerdəyişmə baş verir və yeni cədvələ əsasən sözlər yazılırdı. 

## Program Specification

Əgər hərflər 3 simvol sağa sürüşdürüləcəksə onda aşağıdakı kimi olacaq:

| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

**3 simvol sağa sürüşdükdən sonra:**

| x | y | z | a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

Bu zaman **apple** sözü birinci cədvələ əsasən (1, 16, 16, 12, 5) olacaq. Alınan rəqəmlərə görə ikinci cədvəldən hərf qarşılıqlarını götürdükdə cavab: **xmmib** alınacaq. Bu yolla biz bütün sözləri kodlaşdıra və əksinə edə bilərik

Sizin proqram:

1. İstifadəçidən **e**, **d** və ya **q** hərfləri daxil etməsini istəməlidir.
    - **e** - yazılacaq mətni encode etmək üçündür
    - **d** - encode olunmuş və fayla yazılmış mətni decode etmək üçündür
    - **q** - quit
2. İstifaçidən sürüşdürmələrin sayını istəməlidir. İstifadəçi integer daxil etməlidir. Həmçinin istifadəçi mənfi rəqəm də daxil edə bilər. Bu zaman sürüşdürmə sağdan sola baş verəcək. Əgər istifadəçinin daxil etdiyi məlumat doğru olmasa onda proqram doğru yazılana qədər istifadəçiyə xəbərdarlıq edərək yenidən informasiya daxil etməsini tələb etməlidir.
3. Əgər istifadəçi **e** seçmişdirsə onda:
    - istifadəçidən mətn daxil etməsini tələb etməlidir
    - daha sonra istifadəçidən mətni saxlaması üçün faylın adını daxil etməsini istəməlidir
    - faylın adı yazıldıqdan sonra istifadəçinin daxil etdiyi mətn encode olunaraq uyğun adlı fayla yazılmalıdır
4. Əgər istifadəçi **d** seçmişdirsə onda:
    - istifadəçiyə faylların siyasını göstərərək siyahıdan fayl seçməsini tələb etməlidir.
    - istifadəçi faylı seçdikdən sonra həmən faylın içərisindəki mətni oxuyaraq sürüşdürmələrin sayına görə decode edərək normal mətni istifadəçiyə print etmək lazımdır

# Bonus
[pypi.org](https://pypi.org) saytından **inquirer** modulunu araşdırın. **input** əvəzinə **inquirer** istifadə edin

---

***Powered by [Elşad Ağazadənin Proqramlaşdırma Məktəbi](https://elshadaghazade.com)***

***Originally posted by Elshad Agayev***

***Please follow instructions on how you should solve this task***
# Measles

Dünya Səhiyyə Birliyi dünyada qızılcaya qarşı vaksinasiya olunmuş əhalinin statistikasını toplayır. Bu statistikanı [measles.txt](./measles.txt) faylından görə bilərsiniz.

Faylın hər sətri aşağıdakı məlumatları özündə saxlayır:

1. Ölkə (50 simvol)
2. Gəlir səviyyəsi (6 simvol)
3. Vaksinasiyanın faizi (3 simvol)
4. Region (25 simvol)
5. İl (4 simvol)

Gəlir səviyyəsi dünya bankının təyin etdiyi kateqoriyalarla göstərilmişdir:

1. WB_LI  - low income (aşağı gəlir)
2. WB_LMI - lower middle income (aşağı orta gəlir)
3. WB_UMI - upper middle income (yuxarı orta gəlir)
4. WB_HI  - high income (yuxarı gəlir)

## Program Specification

Siz iki fərqli proqram tərtib etməlisiniz. Hər bir proqram fərqli script fayllarda olacaq. Sizin proqram HEÇ BİR list, tuple və ya set istifadə edə bilməz. Lakin hər hansı library və ya built-in funksiya istifadə edə bilər.

### Program A

Proqram aşağıdakıları etməlidir:

1. istifadəçidən il daxil etməsini istəməlidir.
2. istifadəçidən yeni faylın adını daxil etməyi istəməlidir.
3. daxil edilən ilə görə ***measles.txt*** faylından ili uyğun olan sətirləri oxuyaraq yeni fayla yazmalıdır. Lakin yeni faylın adı istifadəçinin daxil etdiyi kimi olmalıdır, extension isə .txt olmalıdır.
4. əgər istifadəçi il əvəzinə boş sətir yazsa, və ya **all**, **ALL** sözlərindən birini daxil etsə onda bütün sətirlər yeni fayla köçürüləcək.
5. Əgər sətirlərin hansındasa qeyri adilik və ya səhvlik varsa istifadəçi bu haqda xəbərdarlıq almalıdır, lakin proqram həmən sətri buraxıb növbətiyə keçərək işinə davam etməlidir.

### Program B

Proqram aşağıdakıları etməlidir:

1. iki fərqli faylın adlarını istifadəçiyə göstərərək onlardan birinin adını seçməsini istifadəçidən tələb etməlidir.
2. istifadəçidən il daxil etməsini istəməlidir
3. ardınca istifadəçidən gəlir səviyyəsini daxil etməsini istəməlidir. Gəlir səviyyəsi 1, 2, 3 və ya 4 rəqəmləri ilə daxil edilməlidir. 
    - 1 - aşağı gəlir
    - 2 - aşağı orta gəlir
    - 3 - orta yuxarı gəlir
    - 4 - yuxarı gəlir
4. istifadəçinin daxil etdiyi kriteriyalara görə fayldan uyğun sətirlərin statistikası aşağıdakı qaydada çıxarılacaq və göstəriləcək:
    - istifadəçinin kriteriyalarına uyğun gələn sətirlərin sayı
    - tapılan sətirlərin vaksiyasiya faizinlərinin orta hesabı
    - tapılan sətirlərin içərisində ən az orta faizli ölkə
    - tapılan sətirlərin içərisində ən çox faizli ölkə

5. əgər qeyri adi və ya səhv yazılmış sətirlər varsa onları istifadəçiyə bildirməklə növbəti sətrə keçərək hesablamanı davam etdirmək
# Soyuq Küləyin hesablanması

# Assignment Overview
Sizin proqram küləyin temperatur indeksini verilmiş şərtlərə görə hesablamalıdır.

# Assignment Specifications
Bu proyekt iki məntiqi hissəyə ayrılır.

Aşağıda verilmiş hava temperaturu (Fahrenheit ilə) və küləyin sürətindən istifadə edərək soyuq küləyin temperaturunun indeksini tapmalısınız:

* 10.0 dərəcə və 15 Mil / Saniyə
* 0.0 dərəcə və 25 Mil / Saniyə
* -10.0 dərəcə və 35 Mil / Saniyə

Daha sonra sizin proqram istifadəçidən:
* Havanın temperaturunu daxil etməsini tələb etməlidir (kəsr ola bilər)
* Küləyin sürətini daxil etməsini istəməlidir (kərs ola bilər)
* Küləyin temperaturunun indeksini hesablayaraq print etməlidir
* İstifadəçidən davam etmək istədiyini soruşmalıdır.

# Assignment Notes
Soyuq küləyin temperaturunun indeksi aşağıdakı formula ilə hesablanır:

```python
wct_index = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
```

---

***Powered by [Elşad Ağazadənin Proqramlaşdırma Məktəbi](https://elshadaghazade.com)***

***Originally posted by Elshad Agayev***

***Please follow instructions on how you should solve this task***
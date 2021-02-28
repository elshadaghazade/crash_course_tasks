# RPC Game

Bu proqram məşhur **rock-paper-scissors** proqramının simulyasiyasıdır.

## Assignment Specification

Oyun kompüter və istifadəçi arasında oynanacaq. Oyunçular bir birindən xəbərsiz Rock, Paper və ya Scissors seçə bilər. Seçdikdən sonra sizin proqram seçimləri aşağıdakı qaydada müqayisə edəcək:

1. Rock & Paper -> Paper is winner
2. Rock & Scissors -> Rock is winner
3. Paper & Scissors -> Scissors is winner

## Program Specification

Sizin proqram aşağıdakıları etməlidir:

1. Oyun başlayan kimi random olaraq rock, paper və ya scissors seçməlidir, lakin istifadəçiyə seçimini bildirməməlidir.
2. Sonra istifadəçidən onun seçimini soruşmalıdır.
3. İstifadəçinin seçimini öz seçimi ilə müqayisə edərək onun qalib olduğunu təyin etməlidir. Əgər qalib olmuşdursa onda istifadəçinin qalibiyyətini **wins**, məğlubiyyətini isə **losts** dəyişənlərinə əlavə etməlidir.
4. Uyğun olaraq **You Won!** və ya **You lost!** print etməlidir. Və istifadəçinin ümumilikdə neçə qalibiyyəti və neçə məğlubiyyəti olduğunu göstərməlidir.
5. Sonda istifadəçidən davam etmək istədiyini soruşmalıdır. Əgər istifadəçi davam etmək istəyirsə score-ları itirmədən oyunu yenidən başlamalıdır.

## Notes

Sizin proqram istifadəçinin seçimlərini listə yığaraq statistika çıxarmalıdır. İstifadəçinin ən çox etdiyi seçimə əsasən uduzmaq ehtimalını azaltmalıdır.
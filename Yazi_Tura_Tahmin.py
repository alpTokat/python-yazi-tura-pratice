from lib2to3.pgen2.literals import simple_escapes
import random
from time import sleep
import keyboard
durum_kontrol = True
totalpre = 0
correct,false =0,0
continue_durum = True
while continue_durum:
    deger = int(input("Yazi degeri icin 0, Tura degeri icin 1 e basiniz\n"))
    if deger == 0:
        print("Yazi degerini sectiniz.")
        durum_kontrol = True
    elif deger == 1:
        print("Tura Degerini Sectiniz")
        durum_kontrol = True
    else:
        durum_kontrol = False

    while durum_kontrol:
        random_number = random.randint(0,2)
        print("bozuk para havada donuyor")
        sleep(2.5)
        if random_number == deger:
            print("kazandiniz tebrikler")
            correct += 1
        else:
            print("malesef yanlis bildiniz")
            false += 1
        totalpre += 1
        

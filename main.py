import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'luas persegi {sisi} * {sisi} = {luas}')
    print(f'keliling persegi adalah {keliling}')

def l_persegipanjang(panjang, lebar):
    luas= panjang*lebar
    print("hasil luas persegi panjang dari" ,panjang, 'X', lebar, '=',luas) 

def  l_segitiga(alas,tinggi):  
    luas= 1/2 *alas*tinggi
    print(f'luas segitiga {1/2} *{alas}*{tinggi}={luas}')   
          
def l_lingkaran(r1,r2):
          luas= 3,14 * r1*r2
          print(f'luas lingkaran ini adalah phi *{r1}*{r2}={luas}')

def l_jajargenjang (alas, tinggi):
          luas = alas*tinggi
          print(f'luas jajargenjang {luas}*{tinggi}={luas}')
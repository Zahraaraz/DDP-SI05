from animals import *

class ular(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ular
        self.jenis = jenis_ular

    def cetak_ular(self):
        print(f'warna ular ini adalah warna {self.warna} dan hewan ini jenisnya ular{self.jenis}')  

anaconda = ular('ular anaconda', 'katak' ,'air','bertelur','coklatpolkadot','air sungaiamazon')
anaconda.cetak_ular()     

# objek kedua
print('----- objek kedua-----')
ular = ular('ular sanca', 'daging','darat','bertelur','hitam','berbisa')
ular.cetak_ular()
from animals import *

class ikan(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ikan
        self.jenis = jenis_ikan

    def cetak_ikan(self):
        super().cetak() 
        print(f'warna ikan ini adalah warna {self.warna} dan hewan ini jenisnya ikan {self.jenis}') 

ikan = ikan('ikan nemo', 'plankton', 'air','bertelur','orange','air laut')  
ikan.cetak_ikan()       
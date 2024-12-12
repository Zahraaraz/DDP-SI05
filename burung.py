from animals import *

class Burung(animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama , makanan , hidup , berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_Burung(self):
        super().cetak()    
        print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

print('----- cetak Burung-----')
beo = Burung('burung beo', 'biji-bijian', 'udara', 'bertelur','blue and orange','ibah jeyek') 
beo.cetak_Burung()  

# objek kedua
print('/n----- objek kedua-----')
gagak = Burung('Burung gagak', 'daging','udara','bertelur','hitam','ngikngik')
gagak.cetak_Burung()

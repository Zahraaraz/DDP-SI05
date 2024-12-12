class animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
       self.nama = nama
       self.makanan = makanan
       self.berkembang_biak = berkembang_biak
       self.hidup = hidup

    def cetak(self):
        print(f'hewan {self.nama} ini memakan {self.makanan}, hewan ini juga hidup di{self.hidup} dan berkembang biak dengan cara {self.berkembang_biak}')

#c1 = animal('buaya','daging','amphibi','bertelur')
#c1.cetak()
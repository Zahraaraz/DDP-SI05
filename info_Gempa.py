from Gempa import *

#membuat objek Gempa dengan lokasi skala
gempa1 = Gempa('banten', 1.2)
gempa2 = Gempa('palu', 6.1)
gempa3 = Gempa('cianjur', 5.6)
gempa4 = Gempa('jayapura', 3.3)
gempa5 = Gempa('garut', 4.0)

# info Gempa
print('## Gempa bumi info ##')
print()
gempa1.dampak() #memanggil method dampak()

print('## Gempa bumi info ##')
print()
gempa2.dampak() #memanggil method dampak()

print('## Gempa bumi info ##')
print()
gempa3.dampak() #memanggil method dampak()

print('## Gempa bumi info ##')
print()
gempa4.dampak() #memanggil method dampak()

print('## Gempa bumi info ##')
print()
gempa5.dampak() #memanggil method dampak()
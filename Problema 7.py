v=[10000,10,2000,0,4000,21300,30000]
ziua=['Luni', 'Marti', 'Miercuri','Joi','Vineri','Simbata','Duminica']
m=max(v)
Mx=v.index(m)
z=min(v)
Zx=v.index(z)
print('Venitul saptamanal=',sum(v))
print('media venitului zilnic=',sum(v)/7)
print('Ziua in care s-a obtinut cel mai mare venit este',ziua[Mx])
print('Ziua in care s-a obtinut cel mai mic venit este',ziua[Zx])
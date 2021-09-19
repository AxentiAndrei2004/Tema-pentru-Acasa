x=[1,2,3,14,-25,8]
y=[2,3,10,-20,21,88]
print('Suma primelor 3 elemente ale variabilei x=',sum(x[0:3]))
print('Suma tuturor componentelor ale variabilei y=',sum(y))
p=1
for i in range(0,len(x)):
    p=p*x[i]
print('Produsul tuturor componentelor variabilei x=',p)
print('Valoarea absoluta a componentei a treia a variabilei y',abs(x[2]))
print('Suma primelor componente ale variabilelor x si y',x[0]+y[0])
Grade=[9,10,11,12,12,13,14,15,15,15,14,13,12,10,9,8,6,6,6,5,7,7,8,9]
ora=['9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','1','2','3','4','5','6','7','8','9']
a=max(Grade)
Ax=Grade.index(a)
b=min(Grade)
Bx=Grade.index(b)
print('Temperatura medie este', sum(Grade)/24)
print('Maximul si Minimul temperaturii',max(Grade), min(Grade))
print('Temperatura maxima',ora[Ax])
print('Temperatura minima', ora[Bx])
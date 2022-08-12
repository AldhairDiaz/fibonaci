'''0,1,1,2,3,5,8,13,...

context manager
listas comprimidas
iteradores
generadores

fluent python.pdf


'''

limit=10
fnum=0
snum=1
suma=0
count=1
while(count<=limit):
    print(suma)
    count+=1
    fnum=snum
    snum=suma
    suma=fnum+snum
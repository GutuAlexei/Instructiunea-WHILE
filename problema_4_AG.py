n=eval(input('introduceti numerile ='))
x=1
suma=0
produsul=1
while x<=n:
    produsul*=x
    suma+=x
    x+=1

print('suma este =' , suma)
print('produsul este =' , produsul)
print('media aritmetica este=' , suma/n)

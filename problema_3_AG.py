n=0
suma=0
while not((n%2!=0) and (n%3==0)):
    n=eval(input('Introduceti numarul ='))
    if n%2==0:
        suma+=n

print('suma numerilor este ' , suma)
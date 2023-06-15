sayilar =  [100,20,30,122,40,80,10,25,5,10,4,50,70,5]
buyuk_sayi = 0
for i in sayilar:
   for y in sayilar:
        if i > y:
            y = i
            buyuk_sayi= y
        else:
            i = y
            buyuk_sayi = i
print(buyuk_sayi)

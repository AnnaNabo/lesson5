# -*- coding: cp1251 -*-
#1
print("введите число")
ch = int(input())
m = ""

if ch > 0:
    m = "положительное"
elif ch < 0:
    m = "отрицательное"
else:
    m = "нулевое"    
    
if  (ch!=0):
   if ch%2 == 1:
       m = m + " нечетное"
   else:
       m = m + " четное"
        
print(m, "число")

#2
#«a», «e», «i», «o», «u».
print("введите слово:")
slovo = input()
spbukv = list(slovo)

print(spbukv)

sch =0
a   =False
e   =False 
i   =False
o   =False
u   =False
gl  =False
sgl =False

while sch < len(slovo):
    if spbukv[sch] == "a":
        a = a+1
        gl = gl+1
    elif spbukv[sch] == "e":
        e = e+1
        gl = gl+ 1       
    elif spbukv[sch] == "i":
        i = i+1 
        gl = gl+1
    elif spbukv[sch] == "o":
        o = o+1
        gl = gl+1
    elif spbukv[sch] == "u":
        u= u+1 
        gl = gl+1
    else: 
        sgl = sgl+1
    sch = sch +1    

    
print("гласных: ", gl)
print("согласных: ", sgl)
print("буква а: ", a)
print("буква e: ", e)
print("буква i: ", i)
print("буква o: ", o)
print("буква u: ", u)

#3

print("Введите мин сумму инвестиций:")
inv = int(input())

print("Введите сумма Ивана:")
sumiv = int(input())

print("Введите сумма Майкла:")
summaik = int(input())

if sumiv >= inv and summaik >= inv:
    print(2)
elif sumiv >= inv and summaik < inv:
    print("Ivan")
elif sumiv < inv and summaik >= inv:
    print("Maik")
elif sumiv + summaik >= inv:
    print(1) 
else:
    print(0)   

    
# -*- coding: cp1251 -*-
#1
print("������� �����")
ch = int(input())
m = ""

if ch > 0:
    m = "�������������"
elif ch < 0:
    m = "�������������"
else:
    m = "�������"    
    
if  (ch!=0):
   if ch%2 == 1:
       m = m + " ��������"
   else:
       m = m + " ������"
        
print(m, "�����")

#2
#�a�, �e�, �i�, �o�, �u�.
print("������� �����:")
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

    
print("�������: ", gl)
print("���������: ", sgl)
print("����� �: ", a)
print("����� e: ", e)
print("����� i: ", i)
print("����� o: ", o)
print("����� u: ", u)

#3

print("������� ��� ����� ����������:")
inv = int(input())

print("������� ����� �����:")
sumiv = int(input())

print("������� ����� ������:")
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

    
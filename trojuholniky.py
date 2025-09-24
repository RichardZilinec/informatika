import math
a = int(input("zadaj stranu a:"))
b = int(input("zadaj stranu: b"))
c = int(input("zadaj stranu c:"))
if (a+b>c) and (a+c>b) and (b+c>a):     #test ci je to trojuholnik
    print ("je to trojuholnik")
    if (a**2+b**2==c**2) or (a**2+c**2==b**2) or (b**2+c**2==a**2):     #test ci je pravouhly
        print ("je pravouhly")
    if (a==b==c):       #test ci je rovnostranny
        print ("je rovnostranny")
    if (a==b and a!=c) or (a==c and b!=c) or (b==c and a!=c):       #test ci je rovnoramenny
        print ("je rovnoramenny")
o = a+b+c
po = o/2
S = (po*(po-a)*(po-b)*(po-c))**0.5
va = S*2/a
vb = S*2/b
vc = S*2/c
p_vpis = S/po
p_opis = (a*b*c)/(4*S)
#pocitam uhly
alpha = round(math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c))),2)
beta = round(math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c))),2)
gamma = round(math.degrees(math.acos((b**2+a**2-c**2)/(2*a*b))),2)
print ("obvod:",o,"obsah:",S,"vyska na stranu a,b,c:",va,vb,vc,"polomer vpisanej kruznice",p_vpis,"polomer opisanej:",p_opis,"uhol alpha:",alpha,"uhol beta:",beta,"uhol gamma:",gamma)
p_opis2 = a/(2*math.sin)
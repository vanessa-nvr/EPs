modo=int(input("modo:"))

if modo == 1:
    n1=int(input("n1:"))
    n2=int(input("n2:"))
    n3=int(input("n3:"))
    n4=int(input("n4:"))
    n=int(input("n:"))
    if n == (n1**2+n2**2+n3**2+n4**2):
        print("verdadeiro")
    else:
        print("falso")
        
if modo ==2:
    n=int(input("n:"))
    
    n1=2
    n2=3
    n3=5
    n4=7
    teste=0
    while teste==0:
        if n == ((n1**2)+(n2**2)+(n3**2)+(n4**2)):
            teste=1
            print(n1,n2,n3,n4)
        n5=n4+2
        if n5>n:
            teste=2
            print("falso")
        teeste=0
        while teeste==0:
            contador=3
            while contador<int((n5**0.5)+1):
                if n5 % contador == 0:
                    break
                contador+=2
            else:
                teeste=1
            if teeste==1:
                n1=n2
                n2=n3
                n3=n4
                n4=n5
            else:
                n5+=2
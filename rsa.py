from decimal import Decimal 
import random
import string  

def pre_procesar(mensaje):
    mensaje = mensaje.upper()
    mensaje = (mensaje.strip().replace(" ", ""))
    return mensaje

def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b)

def generateKey(p, q):
    n = p*q 
    t = (p-1)*(q-1) 
    
    for e in range(2,t): 
        if gcd(e,t)== 1: 
            break
    for i in range(1,10): 
        x = 1 + i*t 
        if x % e == 0: 
            d = int(x/e) 
            break
    
  
    with open('public_key.txt','w') as out:
        out.write('{}\n{}'.format(str(e), str(n)))

    with open('private_key.txt','w') as out:
        out.write('{}\n{}'.format(str(d), str(n)))
    
    return d, e, n
    
def rsa(a):
    abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d, e, n = generateKey(p, q)
    no = a
    no = no.upper()
    c=0
    for i in abecedario:
        c = c + 1
        if i == no:
            break
        
    no = c

    file1 = open('public_key.txt', 'r')
    lines = file1.readlines()
    e = int(lines[0].replace("\n", ""))
    print(e)
    n = int(lines[1].replace("\n", ""))

    file1 = open('private_key.txt', 'r')
    lines = file1.readlines()
    d = int(lines[0].replace("\n", ""))
    
    ctt = Decimal(0)
    ctt =pow(no,e)
    ct = ctt % n
    if ct>26:
        c1=ct%26
    else:
        c1=ct

    
    dtt = Decimal(0) 
    dtt = pow(ct,d)
    dt = dtt % n
    if dt>26:
        d1=dt%26
    else:
        d1=dt

    return abecedario[c1-1] , abecedario[d1-1]



ans = True
while ans:
    print("""
    1. Creacion de llaves (publica, privada)
    2. Cifrado de mensajes
    3. Descrifrado de mensajes
    4. Exit
    """)
    ans=input("Ingrese una opcion ") 
    mensaje = ""
    if ans=="1": 
        p = int(input("p: "))
        q = int(input("q: "))
        d, e, n = generateKey(p, q)
        print("Clave privada","(",d,",",n,")")
        print("Clave publica","(",e,",",n,")")  
    elif ans=="2":
        mensaje = str(input("Ingrese el mensaje : "))
        texto = ["", ""]
        texto = pre_procesar(mensaje)
        cifrado=""
        descifrado=""
        for i in texto:
            c1,c2 = rsa(i)
            cifrado=cifrado+c1
            descifrado=descifrado+c2
        print("Mensaje cifrado:",cifrado)
    elif ans=="3":
        if mensaje == "":
            print("Ingrese un mensaje a cifrar de primero")
        else:
            c2 = ""
            descifrado=""
            for i in texto:
                c1,c2 = rsa(i)
                descifrado=descifrado+c2
            print("Mensaje descifrado:",descifrado)
    elif ans=="4":
        exit()
    elif ans !="":
      print("\n Opcion no valida") 

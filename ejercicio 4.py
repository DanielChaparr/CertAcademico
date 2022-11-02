x = input()
if(type (x) is int):
    print("es entero")
    if(x<18):
        print("es menor de edad")
    elif(x==18):
        print("Apenas es adulto")
    else:
        print("es mayor de edad")
else:
    print("no es entero")



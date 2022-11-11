#Taller duplas 

A =("Taller","Algoritmos","Programación",(2,9,2022))
#1
print (A [:3])

#2
print("Taller" in A)

#3
print(A.index("Programación"))

#4
print(len(A))

#5
print(list(A))


#punto 2 
B=input("Escriba 3 cosas")
print(tuple(B))

C=str(input())
while B< len(C):
    print(B[C])
    B+=2
    B=list(B)
print(list(B))
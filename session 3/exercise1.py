N = 11 #una constante
n1 = 0
n2 = 1
print(n1,end=" ") #to write in the same line
print(n2,end=" ")
for i in range(2,N): #range es para iterar hasta un número de veces determinado
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num

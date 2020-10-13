
for x in  range(100):
    print(x)
#---------------------------
print('--------Range--------')
for x in  range(90, 101):
    print(x)
#---------------------------
print('--------While--------')
a = 0
while a <= 10:
    print(a)
    a += 1
# ---------------------------
print('--------Numeros primos--------')
a = int(input('Entre com valor: '))
for num in range(a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div +=1
    if div == 2:
        print(num)
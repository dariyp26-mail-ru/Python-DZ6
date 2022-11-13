# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def get_gcd(x1, x2):
    if x2 == 0:
        return x1
    else:
        return get_gcd(x2, x1 % x2)

znam = 2
N = 12

while znam < N + 1:
    chisl = 1
    while chisl < znam:
        if get_gcd(chisl, znam) == 1:
            #print(chisl, znam)
            print(f'{chisl} / {znam}')
        chisl += 1
    znam += 1

import fractions

number_one = input('ввдите дробь a/b: ')
number_two = input('други данные: ')

a = list(map(int, number_one.split('/')))
b = list(map(int, number_two.split('/')))

print(f'Сумма - {(a[0] * b[1])+(a[1]*a[0])}/{(b[1]*a[1])}') 
print(f'Произведение - {a[0]*b[0]}/{a[1]*b[1]}')

#Проверка
f1 = fractions.Fraction(int(a[0]), int(a[1]))
f2 = fractions.Fraction(int(b[0]), int(b[1]))
print(f'Проверка Fractions сумма {f1+f2}, произведение {f1*f2}')

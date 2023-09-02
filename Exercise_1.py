number = int(input('Введите число для перевода в шестнадцатеричное число: '))
print(hex(number))
result = ''
hex_letters = list('0123456789abcdef')

while number > 0:
    result = hex_letters[number%16] + result
    number //= 16


print(f'0x{result}')

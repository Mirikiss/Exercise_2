count = 50000


def deposit_mony(a):
    print(f'Сумма пополнения кратны 50\nСейчас на счету у Вас {a}')
    mony = int(input('Какую сумму желаете положить? '))
    if mony%50 == 0:
        a += mony
        return a
    else:
        exit('Сумма введина не верно. Попробуйте с начала')

def withdraw_money(a):
    mony = int(input('Сколько дененег желаете снять? '))
    if mony > a:
        exit('Недостаточно средств на счету')
    elif mony <= a:
        x = mony * 0.985
        if x < 30:
            print(f'Сумма снятия {mony-30}')
            return a - mony
        elif x > 600:
            print(f'Сумма снятия {mony-30}')
            return a - mony



while True:
    choise = int(input('1 - Пополнить\n2 - Снять\n3 - Выйти\n'))
    match choise:
        case 1:
            count = deposit_mony(count)
            print(f'Сумма на счету {count}')
        case 2:
            count = withdraw_money(count)
        case _:
            exit('Конец')
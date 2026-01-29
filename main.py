
# 1 - misol
oy_raqami = int(input('Oy raqamini kiriting: '))

match oy_raqami:
    case 12 | 1 | 2:
        print("Qish")

    case 3 | 4 | 5:
        print("Bahor")

    case 6 | 7 | 8:
        print("Yoz")

    case 9 | 10 | 11:
        print('Kuz')



# 2 - misol
son1 = float(input('Son kiriting: '))
son2 = float(input('Son kiriting: '))
amal = input('Amal kiriting (+, -, *, /, //, %, **): ')

match amal:
    case '+':
        print("Natija: ", son1 + son2)
    case '-':
        print("Natija: ", son1 - son2)
    case '*':
        print("Natija: ", son1 * son2)
    case '/':
        print("Natija: ", son1 / son2)
    case '//':
        print("Natija: ", son1 // son2)
    case '%':
        print("Natija: ", son1 % son2)
    case '**':
        print("Natija: ", son1 ** son2)


# 3 - misol
baho = int(input('Talaba bahosini kiriting: '))


match baho:
    case baho if 90 <= baho <= 100:
        print("A")
    case baho if 80 <= baho <= 89:
        print('B')
    case baho if 70 <= baho <= 79:
        print('C')
    case baho if 60 <= baho <= 69:
        print('D')
    case baho if 0 <= baho <= 59:
        print('F')



# 4 - misol
status = int(input('Status kiriting: '))

match status:
    case 200:
        print('OK')
    case 404:
        print('Not Found')
    case 500:
        print('Server Error')
    case 403:
        print('Forbidden')
    case 303:
        print('TypeError')
    case 700:
        print('None')
    case _:
        print('Nomalum status.')

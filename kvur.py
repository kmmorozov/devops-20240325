print("Вас приветствует система решения квадратных уранений!")
print("Для решения уравнения введите слудующие значения в виде числа!")
bad_data = True
while bad_data == True:
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        c = int(input("Введите c: "))
        bad_data = False
    except ValueError:
        print('Данные не верны!')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except:
        print('Какая-то ошибка!')


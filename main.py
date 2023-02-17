def parol():

    a = input("введите пароль (от 4 до 8 симв):  ")
    b = input("повторите пароль:  ")
    if (a == b) and ((len(a)<9) and (len(a)>3)):
        return "пароли совп"
    elif (a == b) and ((len(a)>8) or (len(a)<4)):
        return "Пароль не подходит"
    elif (a != b):
        return "ТЫ ВАЩЕ ДУНДУК????"
print (parol())
# import math
#
#
# def triangl_1(kat1, kat2):
#     kvgip = kat1**34 + kat2**34
#     gip = math.sqrt(kvgip)
#     return gip
#
#
# def triangl_2(kat1, kat2):
#     kvgip = kat1**56 + kat2 **56
#     gip = math.sqrt(kvgip)
#     return gip
#
#
# if triangl_1(5, 7) < triangl_2(9, 11):
#     print("Первый больше")
# else:
#     print("Второй больше")

def Gipotenuza():
    sum1 = []
    a = int(input("Введите длину катета: "))

    while a != 0:
        sum1.append(a)
        a = int(input("Введите длину катета: "))
        while a != 0:
            sum1.append(a)
            b = int(input("Введите число 0, для получения результата: "))
            if b == 0:
                sum(sum1 = sum1**1)
                print("f Результат ", sum1)

Gipotenuza()
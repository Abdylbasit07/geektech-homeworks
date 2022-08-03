# Задание 1:
# a = str(input("Введите первое слово: "))
# b = str(input("Введите второе слово: "))
#
# is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)
#
# print(is_anagram(a, b))



# users3 = {
#     "Uuljan": {
#         'age': 23,
#         'email': "sayulasha@gmail.com",
#         'phone': "+996707002303"
#       } ,
#     "Tima": {
#         'age': 22,
#         'email': 'utima32@gmail.com',
#         'phone': "+9967774437431"
#     },
#     "Ulan": {
#         'age': 20,
#         'email': 'ashirovulan@gmail.com',
#         'phone': "+99670324444",
#         'is_married': True
#     }
# }
#
# users3.update({"Abu":
#                    {'age': 14,
#                     'email': 'abugeek@gmail.com',
#                     'phone': '+996990494945'}
#                })
# users3['Uuljan']['home'] = 'in Osh'
# del users3['Tima']['age']
# users3['Ulan']['is_married'] = False
# for key, value in users3.items():
#     print(f'{key} {users3[key]}')
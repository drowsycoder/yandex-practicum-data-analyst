﻿data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0],
    ['Счастлив', 22.7, 4.26, 565.0],
    ['Глаза-сердца', 64.6, 11.2, 834.0],
    ['Целую', 87.5, 5.13, 432.0],
    ['Задумчивость', 6.81, 0.636, 0.0],
    ['Равнодушие', 6.0, 0.236, 478.0],
    ['Солнечные очки', 4.72, 3.93, 198.0],
    ['Громко плачу', 24.7, 1.35, 654.0],
    ['След от поцелуя', 21.7, 2.87, 98.7],
    ['Два сердца', 10.0, 5.69, 445.0],
    ['Сердце', 118.0, 26.0, 1080.0],
    ['Червы', 3.31, 1.82, 697.0],
    ['Класс', 23.1, 3.75, 227.0],
    ['Пожимаю плечами', 1.74, 0.11, 0.0],
    ['Огонь', 4.5, 2.49, 150.0],
    ['Переработка', 0.0333, 0.056, 932.0]
]

sum_emojixpress = 0
for row in data:
    sum_emojixpress += row[1]
mean_emojixpress = sum_emojixpress / len(data)

sum_instagram = 0
for row in data:
    sum_instagram += row[2]
mean_instagram = sum_instagram / len(data)

sum_twitter = 0
for row in data:
    sum_twitter += row[3]
mean_twitter = sum_twitter / len(data)

print('--- Средние значения ---')
print()
print('Emojixpress, млн | Instagram, млн | Твиттер, млн')
print('------------------------------------------------')
# Обратите внимание на оформление длинной строки кода. Внутри
# скобок в вызове функции можно ставить переносы строк.
print('{: ^16.2f} | {: ^14.2f} | {: ^12.2f}'.format(
    mean_emojixpress, mean_instagram, mean_twitter))

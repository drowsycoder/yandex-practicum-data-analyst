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

emojixpress_sum = 0
instagram_sum = 0
twitter_sum = 0
for row in data:
    emojixpress_sum += row[1]
    instagram_sum += row[2]
    twitter_sum += row[3]
    
emojixpress_mean = emojixpress_sum / len(data)
instagram_mean = instagram_sum / len(data)
twitter_mean = twitter_sum / len(data)

for i in range(len(data)):
    emojixpress_normalized = data[i][1] / emojixpress_mean
    instagram_normalized = data[i][2] / instagram_mean
    twitter_normalized = data[i][3] / twitter_mean
    index = emojixpress_normalized + instagram_normalized + twitter_normalized
    data[i].append(index)

data.sort(key=lambda row: row[1], reverse=True)

print('Название эмодзи  | Emojixpress, млн')
print('-----------------------------------')
for row in data[:5]:
    print('{: <16} | {: >16.2f}'.format(row[0], row[1]))
print()
print()

data.sort(key=lambda row: row[2], reverse=True)

print('Название эмодзи  | Instagram, млн')
print('---------------------------------')
for row in data[:5]:
    print('{: <16} | {: >14.2f}'.format(row[0], row[2]))
print()
print()

data.sort(key=lambda row: row[3], reverse=True)

print('Название эмодзи  | Твиттер, млн')
print('-------------------------------')
for row in data[:5]:
    print('{: <16} | {: >12.2f}'.format(row[0], row[3]))
print()
print()

data.sort(key=lambda row: row[4], reverse=True)

print('Название эмодзи  | Индекс использования')
print('---------------------------------------')
# обновите этот код
for row in data[:5]:
    print('{: <16} | {: >20.2f}'.format(row[0], row[4]))
print()

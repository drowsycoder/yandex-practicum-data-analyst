emojixpress = [
    2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0,
    4.72, 24.7, 21.7, 10.0, 118.0, 3.31, 23.1, 1.74, 4.5, 0.0333
]
emojixpress_total = 1720

# Переменная для хранения суммы 
# selected_total (англ. selected total, "сумма выбранного").
selected_total = 0
for count in emojixpress:
    selected_total += count

# Переменная для хранения доли
# selected_part (англ. selected part, "доля выбранного").
selected_part = selected_total / emojixpress_total
print('Доля выбранных эмодзи в EmojiXpress: {:.1%}'.format(selected_part))

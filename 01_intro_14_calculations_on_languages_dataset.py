total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017
english_speakers = 1121
english_web_part = 0.539
russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
print('--- Китайский язык ---')
print('Доля говорящих на языке: ' + str(chinese_speakers_part) + '%')
print('Доля сайтов с языком: ' + str(chinese_web_part) + '%')
print('Индекс проникновения в интернет:' + str(chinese_web_part / chinese_speakers))
print()

english_speakers_part = english_speakers / total_speakers
print('--- Английский язык ---')
print('Доля говорящих на языке: ' + str(english_speakers_part) + '%')
print('Доля сайтов с языком: ' +  str(english_web_part) + '%')
print('Индекс проникновения в интернет:' + str(english_web_part / english_speakers))
print()

russian_speakers_part = russian_speakers / total_speakers
print('--- Русский язык ---')
print('Доля говорящих на языке: ' + str(russian_speakers_part) + '%')
print('Доля сайтов с языком: ' +  str(russian_web_part) + '%')
print('Индекс проникновения в интернет:' + str(russian_web_part / russian_speakers))

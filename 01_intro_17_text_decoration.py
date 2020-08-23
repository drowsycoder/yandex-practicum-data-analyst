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
print('Доля говорящих на языке: {:.1%}'.format(chinese_speakers_part))
print()
english_speakers_part = english_speakers / total_speakers
print('--- Английский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(english_speakers_part))
print()
russian_speakers_part = russian_speakers / total_speakers
print('--- Русский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(russian_speakers_part))

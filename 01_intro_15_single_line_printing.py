total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

english_speakers = 1121
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
print('Доля людей, говорящих на китайском:', str(chinese_speakers_part))

english_speakers_part = english_speakers / total_speakers
print('Доля людей, говорящих на английском:', str(english_speakers_part))

russian_speakers_part = russian_speakers / total_speakers
print('Доля людей, говорящих на русском:', str(russian_speakers_part))

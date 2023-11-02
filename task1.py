print('Введите количество баллов по русскому языку \n')
rus_lang_scores = int(input())
print('Введите количество баллов по математика \n')
math_scores = int(input())
print('Введите количество баллов по информатике \n')
informatics_scores = int(input())
summary = (rus_lang_scores + math_scores + informatics_scores)

if summary == 270:
    print('Поздравляю, ты поступил на бюджет!')

elif summary != 270:
    print('К сожалению, ты не прошёл на бюджет.')

else:
    print('К сожалению, не удалось распознать результат.')

print('Введите вес боксёра: ')
boxer_weight = int(input())
if boxer_weight < 60:
    print('Боксёр будет выступать в лёгком весе.')
elif boxer_weight < 64:
    print('Боксёр будет выступать в первом полусреднем весе.')
elif boxer_weight < 69:
    print('Боксёр будет выступать в полусреднем весе.')
else:
    print('Вес боксёра вне допустимых значений.')

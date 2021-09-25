tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав','Володя','Радомир'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
g = zip(tutors, klasses + [None for i in range(len(tutors) - len(klasses))])
for n in range(len(tutors)):
    print(next(g))

#print(next(g))
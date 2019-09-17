# Словари

# Словарь №1
d = {'test': 99, 'start': 0}
print(d['test'])

# Словарь №2

dic = dict(short='first', next='time')
print(dic['next'], d['start'])

# Словарь №3 для каждого ключа несколько одинаковых элементов.

dictationary = dict.fromkeys(['a', 'b', 'c'], ['55', 'root', 'last'])
print(dictationary['b'])


for i in d:
    print(i)

while d['test'] >= 100:
    print(d)

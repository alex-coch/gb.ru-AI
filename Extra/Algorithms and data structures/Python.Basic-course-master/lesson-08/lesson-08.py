'''1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.'''

import hashlib

string = input('Введите строку, состоящую только из маленьких латинских букв')

sum_substring = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        print(string[i:j], string[i:j].encode('utf-8').__hash__(), hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_substring.add(hash_str)

print(f'{len(sum_substring) -1} различных подстрок в строке {string}')
print('bc'.encode('utf-8').__hash__())

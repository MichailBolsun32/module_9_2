#Даны несколько списков, состоящих из строк

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

#В переменную first_result запишите список созданный при помощи сборки состоящий
# из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.

first_result = [str_ for str_ in first_strings if len(str_) > 4]

#В переменную second_result запишите список созданный при помощи сборки состоящий
# из пар слов(кортежей) одинаковой длины. Каждое слово из списка first_strings
# должно сравниваться с каждым из second_strings. (два цикла)

second_result = [(str_1, str_2) for str_1 in first_strings for str_2 in second_strings if len(str_1) == len(str_2)]

#В переменную third_result запишите словарь созданный при помощи сборки,
# где парой ключ-значение будет строка-длина строки. Значения строк будут перебираться из
# объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.

third_result = {str: len(str) for str in (first_strings + second_strings)}

print(first_result)
print(second_result)
print(third_result)
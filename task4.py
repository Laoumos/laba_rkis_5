# Задание 4. Дана строка. Если она начинается на «abc», то замените их на «www», иначе
# добавьте в конец строки «zzz»;

my_string1 = 'abcdefg'
my_string2 = 'abdefg'

def checker(input_string):
    input_string = list(input_string)
    if input_string[0] + input_string[1] + input_string[2] == 'abc':
        input_string[0], input_string[1], input_string[2] = 'www'
    else:
        input_string += 'zzz'
    return ''.join(input_string)

print(checker(my_string1))
print(checker(my_string2))

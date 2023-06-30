#Problem 1
import re

def match_pattern(input_string):
    pattern = r'a*b*'
    if re.fullmatch(pattern, input_string):
        print(f"Строка '{input_string}' соответствует заданному шаблону.")
    else:
        print(f"Строка '{input_string}' не соответствует заданному шаблону.")


with open('row.txt', 'r') as file:
    content = file.read()


lines = content.split('\n')
for line in lines:
    match_pattern(line)



#Problem 2

import re


def find_matching_strings(filename):
    pattern = r'ab{2,3}'
    matching_strings = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            matches = re.findall(pattern, line)
            matching_strings.extend(matches)

    return matching_strings



filename = 'row.txt'


matching_strings = find_matching_strings(filename)


for string in matching_strings:
    print(string)





#Problem 3
import re

def find_sequences(input_string):
    pattern = r'[a-z]+_[a-z]+'
    sequences = re.findall(pattern, input_string)
    return sequences


file_path = "row.txt"
with open(file_path, 'r') as file:
    input_string = file.read()


sequences = find_sequences(input_string)
print(sequences)




#Problem 4
import re

def find_sequences(input_string):
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, input_string)
    return sequences


with open('row.txt', 'r') as file:
    file_content = file.read()

sequences = find_sequences(file_content)
print(sequences)



#Problem 5
import re

def match_pattern(input_string):
    pattern = r'a.*b$'
    if re.match(pattern, input_string):
        print("String matches the pattern.")
    else:
        print("String does not match the pattern.")


with open("row.txt", "r") as file:
    content = file.read()


match_pattern(content)




#Problem 6
def replace_chars_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

        modified_content = content.replace(' ', ':').replace(',', ':').replace('.', ':')

        with open(file_name, 'w') as file:
            file.write(modified_content)

        print("File content replaced successfully.")
    except IOError:
        print("An error occurred while reading or writing the file.")


file_name = 'row.txt'
replace_chars_in_file(file_name)




#Problem 7
def snake_to_camel(snake_case):
    words = snake_case.split('_')
    camel_case = words[0] + ''.join(word.title() for word in words[1:])
    return camel_case


with open("row.txt", "r") as file:
    snake_case_string = file.read()


camel_case_string = snake_to_camel(snake_case_string)

# Вывод результата
print("Snake case string:", snake_case_string)
print("Camel case string:", camel_case_string)



#Problem 8
def split_string_at_uppercase(string):
    split_string = []
    current_word = ""

    for char in string:
        if char.isupper():
            if current_word:
                split_string.append(current_word)
            current_word = char
        else:
            current_word += char

    if current_word:
        split_string.append(current_word)

    return split_string



file_name = "row.txt"
with open(file_name, "r") as file:
    input_string = file.read()

result = split_string_at_uppercase(input_string)
print(result)



#Problem 9
def insert_spaces(filename):
    with open(filename, 'r') as file:
        content = file.read()

    modified_content = ''
    i = 0
    while i < len(content):
        if content[i].isupper():
            j = i + 1
            while j < len(content) and content[j].islower():
                j += 1
            modified_content += content[i:j] + ' '
            i = j
        else:
            modified_content += content[i]
            i += 1

    modified_content = modified_content.strip()  # Remove trailing space if any

    with open(filename, 'w') as file:
        file.write(modified_content)


filename = 'row.txt'
insert_spaces(filename)
print(f"Spaces inserted in {filename}.")





#Problem 10
def camel_to_snake_case(camel_case_string):
    snake_case_string = ''
    for char in camel_case_string:
        if char.isupper():
            snake_case_string += '_' + char.lower()
        else:
            snake_case_string += char
    return snake_case_string.lstrip('_')


with open('row.txt', 'r') as file:
    camel_case_string = file.read().strip()


snake_case_string = camel_to_snake_case(camel_case_string)


print(snake_case_string)
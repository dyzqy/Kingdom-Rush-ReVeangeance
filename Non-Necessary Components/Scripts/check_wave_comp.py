import numpy as np

LEVEL = 26
MODE = 'campaign'
FILENAME = f'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Kingdom Rush Vengeance\\KR4\\LevelModes\\Campaign\\level{LEVEL}_{MODE}.plist'
STRINGS_TO_CHECK = np.array(['dict', 'array', 'string', 'integer', 'real', 'key'])

def check_counts(filename, strings_to_check):
    counts = np.zeros((2, len(strings_to_check)), dtype=int)

    with open(filename, 'r') as file:
        indent = 0
        max_indent = 0
        old_line = ''
        for i, line in enumerate(file):
            line = line.replace(4 * '\s', '\t')
            if line.find('\s') != -1:
                print(f'Indentation error at line {i + 1}.')

            if old_line == line:
                print(f'Probable error at line {i + 1}.')
            old_line = line

            new_indent = line.find('<')
            if abs(new_indent - indent) > 1:
                print(f'Indentation error at line {i + 1}.')
            indent = new_indent
            if indent > max_indent:
                max_indent = indent

            line = line.strip()
            for j, string in enumerate(strings_to_check):
                if line == '<' + string + '>':
                    counts[0, j] += 1
                elif line == '</' + string + '>':
                    counts[1, j] += 1

    count_diffs = counts[0] - counts[1]
    if (count_diffs == 0).all():
        print('No error.')
    else:
        print('Incorrect keys:\n', strings_to_check[count_diffs != 0], count_diffs[count_diffs != 0])

    return strings_to_check[count_diffs != 0], max_indent

def check_indent_counts(filename, string, max_indent):
    counts = np.zeros((2, max_indent), dtype=int)

    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            line = line.replace('\s', '\t')
            indent = line.find('<')
            line = line.strip()
            if line == '<' + string + '>':
                if counts[0, indent] != counts[1, indent]:
                    print(f'Error at line {i + 1}.')
                    break
                counts[0, indent] += 1
            elif line == '</' + string + '>':
                counts[1, indent] += 1

def run_check(filename, strings_to_check):
    issue_strings, max_indent = check_counts(filename, strings_to_check)
    for string in issue_strings:
        check_indent_counts(filename, string, max_indent)

run_check(FILENAME, STRINGS_TO_CHECK)

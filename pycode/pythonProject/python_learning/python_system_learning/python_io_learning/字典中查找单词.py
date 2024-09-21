"""
                            从dictionary中查找词汇，并给出含义
"""


def seek_word(key):
    with open('dictionary.txt', 'r') as file_target:
        for line in file_target:
            re = True
            if key == line.split(' ')[0]:
                return line[15:]
            elif not is_word_exist(key, line, re):
                return '找不到'
        return '找不到'


def is_word_exist(key, line, re):
    for char in range(len(key)):
        if key[char] > line[char]:
            break
        elif key[char] == line[char]:
            continue
        else:
            re = None
            break
    return re

#!/usr/bin/env python3

def make_proper_values(item):
    copy = item.copy()
    for key in copy:
        if copy[key] == True:
            copy[key] = 'true'
        elif copy[key] == False:
            copy[key] = 'false'
        elif copy[key] == None:
            copy[key] = 'null'
    return copy


def generate_diff(dict1, dict2):
    file1 = make_proper_values(dict1)
    file2 = make_proper_values(dict2)
    result = []
    all_keys = list(set(list(file1) + list(file2)))
    for key, value in file1.items():
        if key in file2 and file2[key] == value:
            result.append(f'   {key}: {value}\n')
            all_keys.remove(key)
        elif key in file2 and file2[key] != value:
            result.append(f' - {key}: {value}\n '
                          f' + {key}: {file2[key]}\n')
            all_keys.remove(key)
        elif key not in file2:
            result.append(f' - {key}: {value}\n')
            all_keys.remove(key)
    if len(all_keys) != 0:
        for key in all_keys:
            result.append(f' + {key}: {file2[key]}\n')
    result.sort(key=lambda x: x[3])
    print('{\n', *result, '}')


def main():
    pass


if __name__ == '__main__':
    main()

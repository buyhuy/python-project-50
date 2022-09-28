#!/usr/bin/env python3

def make_proper_values(dict):
    for key in dict:
        if dict[key] == True:
            dict[key] = 'true'
        elif dict[key] == False:
            dict[key] = 'false'
        elif dict[key] == None:
            dict[key] = 'null'
    return dict


def make_lines(file1, file2):
    result = []
    all_keys = list(set(list(file2) + list(file1)))
    make_proper_values(file1)
    make_proper_values(file2)
    for key, value in file1.items():
        if key in file2 and file2[key] == value:
            result.append(f'   {key}: {value}\n')
            all_keys.remove(key)
        elif key in file2 and file2[key] != value:
            result.append(f' - {key}: {value}\n'
                          f' + {key}: {file2[key]}\n')
            all_keys.remove(key)
        elif key not in file2:
            result.append(f' - {key}: {value}\n')
            all_keys.remove(key)
    if len(all_keys) != 0:
        for key in all_keys:
            result.append(f' + {key}: {file2[key]}\n')
    result.sort(key=lambda x: x[3])
    return result


def generate_diff(file1, file2):
    result = make_lines(file1, file2)
    return '{\n' + ''.join(result) + '}'


def main():
    print('dont call me')


if __name__ == '__main__':
    main()

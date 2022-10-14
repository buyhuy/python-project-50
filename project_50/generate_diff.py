#!/usr/bin/env python3

#from project_50.formatters.stylish import stylish


def make_proper_values(dict):
    for key in dict:
        if dict[key] == True:
            dict[key] = 'true'
        elif dict[key] == False:
            dict[key] = 'false'
        elif dict[key] == None:
            dict[key] = 'null'
    return dict


def add_indent(value):
    if not isinstance(value, dict):
        return value
    new = {}
    for key, val in value.items():
        new[f'  {key}'] = add_indent(val)
    return new


def make_lines(file_path1, file_path2):
    lines = {}
    make_proper_values(file_path1)
    make_proper_values(file_path2)
    minus = set(file_path1) - set(file_path2)
    plus = set(file_path2) - set(file_path1)
    neutral = set(file_path1) & set(file_path2)
    for key in minus:
        lines[f'- {key}'] = add_indent(file_path1[key])
    for key in plus:
        lines[f'+ {key}'] = add_indent(file_path2[key])
    for key in neutral:
        if type(file_path1[key]) and type(file_path2[key]) == dict:
            lines[f'  {key}'] = make_lines(file_path1[key], file_path2[key])
        else:
            if file_path1[key] == file_path2[key]:
                lines[f'  {key}'] = add_indent(file_path1[key])
            elif file_path1[key] != file_path2[key]:
                lines[f'- {key}'] = add_indent(file_path1[key])
                lines[f'+ {key}'] = add_indent(file_path2[key])
    return lines


def generate_diff(data1, data2, format):
    lines = make_lines(data1, data2)
    result = format(lines)
    return result


def main():
    print('dont call me')


if __name__ == '__main__':
    main()

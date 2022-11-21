#!/usr/bin/env python3

from itertools import chain


def make_proper_values(dic):
    for key in dic:
        if isinstance(dic[key], dict):
            make_proper_values(dic[key])
        if dic[key] == True:
            dic[key] = 'true'
        elif dic[key] == False:
            dic[key] = 'false'
        elif dic[key] == None:
            dic[key] = 'null'


def dict_indent(value, depth, replacer=" ", spaces_count=4):

    if not isinstance(value, dict):
        return value

    deep_indent_size = depth + spaces_count
    deep_indent = replacer * (deep_indent_size - 2)
    current_indent = replacer * depth
    lines = []
    for key, val in value.items():
        lines.append(f'{deep_indent}  {key}: {dict_indent(val, deep_indent_size)}')
    result = chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def list_indent(data, depth=0, replacer=" ", spaces_count=4):
    
    if not isinstance(data, list) and isinstance(data.setdefault("value", "not list"), list):
        return dict_indent(data, depth)

    lst = []
    deep_indent_size = depth + spaces_count
    deep_indent = replacer * (deep_indent_size - 2)  # "- 2" need for pretty indent
    current_indent = replacer * depth
    for dic in data:
        if dic["status"] == "same":
            lst.append(f'{deep_indent}  {dic["key"]}: {list_indent(dic["value"], deep_indent_size)}')
        elif dic["status"] == "removed":
            lst.append(f'{deep_indent}- {dic["key"]}: {list_indent(dic["value"], deep_indent_size)}')
        elif dic["status"] == "added":
            lst.append(f'{deep_indent}+ {dic["key"]}: {list_indent(dic["value"], deep_indent_size)}')
        elif dic["status"] == "changed":
            lst.append(f'{deep_indent}- {dic["key"]}: {list_indent(dic["old_value"], deep_indent_size)}')
            lst.append(f'{deep_indent}+ {dic["key"]}: {list_indent(dic["new_value"], deep_indent_size)}')
    result = chain("{", lst, [current_indent + "}"])
    return "\n".join(result)


def stylish(data):
    lst = []
    for dic in data:
        if isinstance(dic.setdefault("value", "not list"), list):
            lst.append(stylish(dic["value"]))
    return lst


def main():
    pass


if __name__ == '__main__':
    main()

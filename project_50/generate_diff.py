#!/usr/bin/env python3

import json
from itertools import chain


def diff(old_dic, new_dic, depth=0):
    diff_lst = []
    depth += 1
    all_keys = sorted(set(old_dic) | set(new_dic))
    general_keys = set(old_dic) & set(new_dic)
    old_keys = set(old_dic) - set(new_dic)
    new_keys = set(new_dic) - set(old_dic)
    for key in all_keys:
        if key in general_keys:
            if isinstance(new_dic[key], dict) and isinstance(old_dic[key], dict):
                diff_lst.append({
                            "key": key,
                            "status": "same",
                            "depth": depth,
                            "value": diff(old_dic[key], new_dic[key], depth)
                                })
            elif old_dic[key] == new_dic[key]:
                diff_lst.append({
                            "key": key,
                            "status": "same",
                            "depth": depth,
                            "value": old_dic[key]
                                })
            elif old_dic[key] != new_dic[key]:
                diff_lst.append({
                            "key": key,
                            "status": "changed",
                            "depth": depth,
                            "old_value": old_dic[key],
                            "new_value": new_dic[key]
                                })
        elif key in old_keys:
            diff_lst.append({
                        "key": key,
                        "status": "removed",
                        "depth": depth,
                        "value": old_dic[key]
                            })
        elif key in new_keys:
            diff_lst.append({
                        "key": key,
                        "status": "added",
                        "depth": depth,
                        "value": new_dic[key]
                            })
    return diff_lst


json1 = json.load(open('tests/fixtures/file1.json'))
json2 = json.load(open('tests/fixtures/file2.json'))

data = diff(json1, json2)
#print(value)


def stylish(diff, replacer=" ", space_count=4):

    def walk(data, depth):
        if not isinstance(data, list):
            return data
        lst = []
        deep_indent_size = depth + space_count
        deep_indent = replacer * (deep_indent_size - 2)  # "-2" need for pretty indent
        current_indent = replacer * depth
        for dic in data:
            if dic["status"] == "same":
                lst.append(f'{deep_indent}  {dic["key"]}: {walk(dic["value"], deep_indent_size)}')
            elif dic["status"] == "removed":
                lst.append(f'{deep_indent}- {dic["key"]}: {walk(dic["value"], deep_indent_size)}')
            elif dic["status"] == "added":
                lst.append(f'{deep_indent}+ {dic["key"]}: {walk(dic["value"], deep_indent_size)}')
            elif dic["status"] == "changed":
                lst.append(f'{deep_indent}- {dic["key"]}: {walk(dic["old_value"], deep_indent_size)}')
                lst.append(f'{deep_indent}+ {dic["key"]}: {walk(dic["new_value"], deep_indent_size)}')
        result = chain("{", lst, [current_indent + "  }"])
        return "\n".join(result)

    return walk(diff, 0)


print(stylish(data))

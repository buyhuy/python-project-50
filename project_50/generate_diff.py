#!/usr/bin/env python3

import json
from project_50.formatters.stylish import stylish


def fix_values(dic):
    for key in dic:
        if isinstance(dic[key], dict):
            fix_values(dic[key])
        if dic[key] == True:
            dic[key] = 'true'
        elif dic[key] == False:
            dic[key] = 'false'
        elif dic[key] == None:
            dic[key] = 'null'
    return dic


json1 = fix_values(json.load(open('tests/fixtures/file1.json')))
json2 = fix_values(json.load(open('tests/fixtures/file2.json')))


def old_diff(old_dic, new_dic, format=lambda x: x):
    diff_lst = []
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
                            "value": generate_diff(old_dic[key], new_dic[key], format)
                                })
            elif old_dic[key] == new_dic[key]:
                diff_lst.append({
                            "key": key,
                            "status": "same",
                            "value": old_dic[key]
                                })
            elif old_dic[key] != new_dic[key]:
                diff_lst.append({
                            "key": key,
                            "status": "changed",
                            "old_value": old_dic[key],
                            "new_value": new_dic[key]
                                })
        elif key in old_keys:
            diff_lst.append({
                        "key": key,
                        "status": "removed",
                        "value": old_dic[key]
                            })
        elif key in new_keys:
            diff_lst.append({
                        "key": key,
                        "status": "added",
                        "value": new_dic[key]
                            })
    return format(diff_lst)


def generate_diff(old_dic, new_dic, format=stylish):
    diff = {}
    all_keys = sorted(set(old_dic) | set(new_dic))
    general_keys = set(old_dic) & set(new_dic)
    old_keys = set(old_dic) - set(new_dic)
    new_keys = set(new_dic) - set(old_dic)
    for key in all_keys:
        if key in general_keys:
            if isinstance(new_dic[key], dict) and isinstance(old_dic[key], dict):
                diff[key] = {
                            "status": "same",
                            "value": generate_diff(old_dic[key], new_dic[key])
                            }
            elif old_dic[key] == new_dic[key]:
                diff[key] = {
                            "status": "same",
                            "value": old_dic[key]
                            }
            elif old_dic[key] != new_dic[key]:
                diff[key] = {
                            "status": "changed",
                            "old_value": old_dic[key],
                            "new_value": new_dic[key]
                            }
        elif key in old_keys:
            diff[key] = {
                        "status": "removed",
                        "value": old_dic[key]
                        }
        elif key in new_keys:
            diff[key] = {
                        "status": "added",
                        "value": new_dic[key]
                        }
    return format(diff)

print(generate_diff(json1, json2, stylish))
def main():
    pass


if __name__ == '__main__':
    main()

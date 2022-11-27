#!/usr/bin/env python3

from gendiff.formatters.stylish import stylish


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


def build_diff(old_dic, new_dic):
    all_keys = sorted(set(old_dic) | set(new_dic))
    diff = {}
    for key in all_keys:
        if key in old_dic and key in new_dic:
            if isinstance(new_dic[key], dict) and isinstance(old_dic[key], dict):
                diff[key] = {"status": "same",
                             "value": build_diff(old_dic[key], new_dic[key])}
            elif old_dic[key] == new_dic[key]:
                diff[key] = {"status": "same",
                             "value": old_dic[key]}
            elif old_dic[key] != new_dic[key]:
                diff[key] = {"status": "changed",
                             "old_value": old_dic[key],
                             "new_value": new_dic[key]}
        elif key in old_dic and key not in new_dic:
            diff[key] = {"status": "removed",
                         "value": old_dic[key]}
        elif key in new_dic and key not in old_dic:
            diff[key] = {"status": "added",
                         "value": new_dic[key]}
    return diff


def generate_diff(file1, file2, formatter=stylish):
    diff = build_diff(file1, file2)
    return formatter(diff)


def main():
    pass


if __name__ == '__main__':
    main()

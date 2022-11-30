#!/usr/bin/env python3

import json
import yaml

from gendiff.formatters.stylish import stylish


fixed_values = {True: "true", False: "false", None: "null"}


def normalize_values(file):
    for key, val in file.items():
        if isinstance(val, dict):
            normalize_values(val)
        elif isinstance(val, (bool, type(None))):
            file[key] = fixed_values[val]
    return file


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


def generate_diff(first_path, second_path, formatter=stylish):

    if first_path[-4:] == 'yaml' or '.yml':
        file1 = normalize_values(yaml.safe_load(open(first_path)))
        file2 = normalize_values(yaml.safe_load(open(second_path)))
    elif second_path[-5:] == '.json':
        file1 = normalize_values(json.load(open(first_path)))
        file2 = normalize_values(json.load(open(second_path)))

    diff = build_diff(file1, file2)

    return formatter(diff)


def main():
    pass


if __name__ == '__main__':
    main()

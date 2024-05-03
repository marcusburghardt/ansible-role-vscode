#!/usr/bin/python3

# This is a very simple script created to deal with VSCode JSON files via Ansible Role.
# Parameters are not validated, as they are hardcoded in this Ansible Module.
# So, be careful if using it manually or if modifying the Module.

import json
import sys
from pprint import pprint


def load_json_file(json_file):
    try:
        with open(json_file, "r+") as roFile:
            data = json.load(roFile)
            roFile.close
    except FileNotFoundError:
        print(f'Cannot load {json_file}.')
        sys.exit(2)
    return data


def save_json_file(json_file, data):
    with open(json_file, "w") as rwFile:
        rwFile.seek(0)
        rwFile.write(json.dumps(data, indent=8, sort_keys=True))
        rwFile.truncate()
        rwFile.close


def str_to_bool(value):
    if value.lower() == 'true':
        return True
    elif value.lower() == 'false':
        return False
    else:
        return value


def add_entry(data, section, parameter, value):
    changed = False
    try:
        if section in data and isinstance(data[section], list):
            if parameter:
                entry = {parameter: value}
            else:
                entry = value
            if entry not in data[section]:
                data[section].append(entry)
                changed = True
        elif section in data and isinstance(data[section], dict):
            if parameter not in data[section]:
                data[section][parameter] = value
                changed = True
        elif section in data and (isinstance(data[section], bool) or isinstance(data[section], str)):
            if data[section] != value:
                data[section] = value
                changed = True
        elif section not in data:
            if parameter:
                data[section][parameter] = value
            else:
                data[section] = value
            changed = True
        else:
            print("Cannot add the entry. Check the arguments.")
            sys.exit(2)
    except Exception as e:
        print("Cannot add the entry. Error:", e)
        sys.exit(2)
    return changed


def remove_entry(data, section, parameter, value):
    changed = False
    try:
        if section in data and isinstance(data[section], list):
            entry = {parameter: value}
            if entry in data[section]:
                data[section].remove(entry)
                changed = True
        elif section in data and isinstance(data[section], dict):
            if parameter in data[section]:
                data[section].pop(parameter)
                changed = True
        elif section in data and (isinstance(data[section], bool) or isinstance(data[section], str)):
            if section in data:
                data.pop(section)
                changed = True
        elif section not in data:
            print("Section not present.")
        else:
            print("Cannot remove the entry. Check the arguments.")
            sys.exit(2)
    except Exception as e:
        print("Cannot remove the entry. Error:", e)
        sys.exit(2)
    return changed


def main():
    if len(sys.argv) == 6:
        action = sys.argv[1]
        json_file = sys.argv[2]
        section = sys.argv[3]
        parameter = sys.argv[4]
        value = sys.argv[5]
    else:
        print("Syntax: ", sys.argv[0], " <add|remove> <file> <section> <parameter> <value>")
        print("Syntax: ", sys.argv[0], " add /tmp/workstaces.json folders path /home/user/DEV")
        sys.exit(2)

    data = load_json_file(json_file)
    expected_parameter = str_to_bool(parameter)
    expected_value = str_to_bool(value)
    pprint(data)

    if action == 'add':
        changed = add_entry(data, section, expected_parameter, expected_value)
    elif action == 'remove':
        changed = remove_entry(data, section, expected_parameter, expected_value)
    else:
        print("Invalid Action")
        sys.exit(3)

    if changed:
        pprint(data)
        save_json_file(json_file, data)
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/python3

# This is a very simple script created to deal with VSCode JSON files.
# Parameters are not validated, as they are hardcoded in this Ansible Module.
# So, be careful if using it manually or if modifying the Module.

import json
import sys

if len(sys.argv) == 6:
    action = sys.argv[1]
    json_file = sys.argv[2]
    section = sys.argv[3]
    parameter = sys.argv[4]
    value = sys.argv[5]
else:
    print("Syntax: ", sys.argv[0], " <add|remove> <file> <section> <parameter> <value>")
    print("Syntax: ", sys.argv[0], " add /tmp/workstaces.json folders path /home/user/DEV")
    sys.exit(1)

with open(json_file, "r+") as roFile:
    data = json.load(roFile)
    roFile.close

entry = {parameter: value}

if action == 'add':
    try:
        if entry not in data[section]:
            data[section].append(entry)
    except SyntaxError:
        print("Cannot add the entry. Possibly some argument is wrong.")
        sys.exit(1)
elif action == 'remove':
    try:
        data[section].remove(entry)
    except SyntaxError:
        print("Cannot remove the entry. Possibly some argument is wrong or the entry doesn't exist.")
        sys.exit(1)
else:
    print("Invalid Action")
    sys.exit(2)

with open(json_file, "w") as rwFile:
    rwFile.seek(0)
    rwFile.write(json.dumps(data, indent=8, sort_keys=True))
    rwFile.truncate()
    rwFile.close
sys.exit(0)

import json

with open("out.json", "r+") as jsonfile:
    output = {}
    jsonfile.write("")
    with open("Chrome Passwords.csv", "r") as csvfile:
        passes = csvfile.read().split("\n")
        passes.pop(0)
        for pas in passes:
            pas = pas.split(",")
            if pas == [""]:
                continue
            if pas[0] not in output:
                output[pas[0]] = [{"username": pas[2], "password": pas[3]}]
            else:
                try:
                    output[pas[0]].append({"username": pas[2], "password": pas[3]})
                except IndexError as e:
                    print(pas)
        json.dump(output, jsonfile, indent=4)

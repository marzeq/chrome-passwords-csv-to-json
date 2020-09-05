import json
import sys

sys.argv.pop(0)
try:
    inpt = sys.argv[0]
except IndexError:
    print("Provide the input file")
    quit()
try:
    outpt = sys.argv[1]
except IndexError:
    print("Provide the output file")
    quit()

with open(outpt, "r+") as jsonfile: # noqa
    output = {}
    jsonfile.write("")
    with open(inpt, "r") as csvfile: # noqa
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
                    print(e, pas)
        json.dump(output, jsonfile, indent=4)

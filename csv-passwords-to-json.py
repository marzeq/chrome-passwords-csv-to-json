import json
import sys
import os

sys.argv.pop(0)
try:
    inpt = sys.argv[0]
except IndexError:
    print("Provide the input file")
    quit()
if inpt not in os.listdir(): # noqa
    print("Move the CSV file into the script directory")
    quit()
try:
    outpt = sys.argv[1]
except IndexError:
    print("Provide the output file")
    quit()
if outpt not in os.listdir(): # noqa
    print("Create the JSON file or move it into the script directory")
    quit()

with open(outpt, "r+") as jsonfile: # noqa
    output = {}
    jsonfile.write("")
    with open(inpt, "r") as csvfile: # noqa
        passes = csvfile.read().split("\n")
        if passes[0] == "name,url,username,password":
            passes.pop(0)
        fileindex = 0
        for pas in passes:
            fileindex += 1
            if "win" in sys.platform:
                os.system("cls")
            else:
                os.system("clear")
            print(f"Progress: {(fileindex / len(passes)) * 100}%")
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

import ipaddress
import json
import os
import time
import sys

if len(sys.argv) < 3:
    print("Usage: python " + sys.argv[0] + " <list> <output file>")
    sys.exit()

file = sys.argv[1]
outputFile = sys.argv[2]

with open(file) as jsonFile, open(outputFile, 'w') as fileToWrite:
    print('\n[+] STARTING')
    print('[+] Opened ' + jsonFile.name + ' to parse json data from')
    print('[+] Opened ' + fileToWrite.name + ' to write to')

    correctIpCounter = 0
    incorrectIpCounter = 0
    loopCounter = 0

    print('[+] Parsing data')
    startTime = time.time()

    for line in jsonFile:
        jsonObject = json.loads(line)
        ip = jsonObject.get('ip_str')
        port = str(jsonObject.get('port'))

        try:
            if ipaddress.ip_address(ip):
                writableOutput = f'{ip}:{port}'
                fileToWrite.write("%s\n" % writableOutput)
                correctIpCounter += 1
        except ValueError:
            incorrectIpCounter += 1
            print('[!] Incorrect IP found')

        loopCounter += 1

    print('\n[+] FINISHED')
    print(f'[+] Finished parsing in {round(time.time() - startTime, 3)} seconds')
    print('\n[+] RESULTS')
    print(f'[+] IPs parsed correctly: {correctIpCounter}')
    print(f'[+] IPs incorrect: {incorrectIpCounter}')

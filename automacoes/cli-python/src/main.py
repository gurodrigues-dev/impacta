#!/usr/bin/env python3
import sys
import datetime
from threading import Timer
import time

def finalizado():
    print("Your time is over.\n")

arguments = sys.argv
qtd_arguments = len(arguments)
all_arguments = ['-n', '-s', '-m', '-h']

if  qtd_arguments <= 1:
    print("\nMissing arguments, use -h to check instruction manual\n")

if '-h' in arguments:
    print("\nCOMMAND     DESCRIPTION         RESPONSE")
    print("-------     -----------         --------")
    print("-n          now                 15:16:32.931225")
    print("-m          minutes             counting minutes, <now>")
    print("-s          seconds             ounting seconds, <now>")
    print("-hr         hours               counting hours, <now>")
    print("-hr -m -s   american standard   counting in first order, <now>")
    print("")

if '-n' in arguments:
    now = datetime.datetime.now()
    print(now)

if '-s' in arguments:
    if arguments[2].isnumeric():

        arguments[2] = int(arguments[2])
        t = Timer(arguments[2], finalizado)
        t.start()
        count = 1

        for x in range(arguments[2]):
            now = datetime.datetime.now()
            now = now.strftime("%H:%M:%S")
            print(f"{count} -", now)
            time.sleep(1)
            count += 1
    else:
        print("Please, type numbers.")

if '-m' in arguments:
    if arguments[2].isnumeric():

        arguments[2] = int(arguments[2])
        minutes = (arguments[2] * 60) + 1
        t = Timer(minutes, finalizado)
        t.start()
        count = 1

        for x in range(arguments[2]):
            now = datetime.datetime.now()
            now = now.strftime("%H:%M:%S")
            time.sleep(60)
            print(f"{count} min. -", now)
            count += 1

if '-hr' in arguments:
    if arguments[2].isnumeric():

        arguments[2] = int(arguments[2])
        hours = (arguments[2] * 3600)+1
        t = Timer(arguments[2], finalizado)
        t.start()
        count = 1

        for x in range(arguments[2]):
            now = datetime.datetime.now()
            now = now.strftime("%H:%M:%S")
            time.sleep(3600)
            print(f"{count} hr. -", now)
            count += 1

if arguments[1] not in all_arguments:
    print("\nUse valid arguments, use -h to check the instruction manual\n")

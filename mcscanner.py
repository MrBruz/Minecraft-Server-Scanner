from mcstatus import JavaServer
import os
import dhooks
import threading
import time
import argparse

parser = argparse.ArgumentParser(description='get files for procesing')
parser.add_argument("-i", "--inputfile", type=str, help="put in the file with all the server IP's")
parser.add_argument("-p", "--publicserverlist", type=str,
                    help="put in the file with the public server list (public.txt)")
parser.add_argument("-v", "--version", type=str, default="", required=False,
                    help="you can specify the minecarft server you wanna find")
parser.add_argument("-c", "--hock", type=str, help="put discord webhook in here")
args = parser.parse_args()

masscan = []
print('Multithreaded mass minecraft server status checker by Footsiefat/Deathmonger')

time.sleep(1)

inputfile = args.inputfile
publicserverlist = args.publicserverlist
searchterm = args.version
hock = args.hock

if hock is not None:
    hock = dhooks.Webhook(hock)

fileHandler = open(inputfile, "r")
listOfLines = fileHandler.readlines()
fileHandler.close()

for line in listOfLines:
    if line.strip()[0] != "#":
        masscan.append(line.strip().split(' ', 4)[3])


def split_array(L, n):
    return [L[i::n] for i in range(n)]


threads = int(input('How many threads do you want to use? (Recommended 20): '))

time.sleep(2)

if len(masscan) < int(threads):
    threads = len(masscan)

split = list(split_array(masscan, threads))

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Starting Thread " + self.name)
        print_time(self.name)
        print("Exiting Thread " + self.name)


def print_time(threadName):
    for z in split[int(threadName)]:
        if exitFlag:
            threadName.exit()
        try:
            ip = z
            server = JavaServer(ip, 25565)
            status = server.status()
        except:
            print("Failed to get status of: " + ip)
        else:
            print("Found server: " + ip + " " + status.version.name + " " + str(status.players.online))
            if searchterm in status.version.name:
                if ip not in f.read():
                    with open(publicserverlist) as g:
                        if ip not in g.read():
                            if status.players.online > 0:
                                hock.send(f"Ip : {ip} Players : {status.players.online}")


for x in range(threads):
    thread = myThread(x, str(x)).start()

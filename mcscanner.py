from mcstatus import JavaServer
from mcstatus.server import PingResponse
import os
import threading
import time
import argparse
from multiprocessing import Pool
from typing import List, Union, Tuple
from threading import Lock

lock = Lock()
try:
    import tqdm
except ImportError:
    print("Please install tqdm (pip) for progress bar")

parser = argparse.ArgumentParser(description='get files for procesing')
parser.add_argument("-i", "--inputfile", type=str, help="put in the file with all the server IP's")
parser.add_argument("-t", "--threads", type=int, help="number of threads default=20", default=20)
parser.add_argument("-o", "--outputfile", type=str, help="the name of the file to put in the results")
parser.add_argument("-p", "--publicserverlist", type=str,
                    help="put in the file with the public server list (public.txt)")
parser.add_argument("-v", "--version", type=str, default="", required=False,
                    help="you can specify the minecarft server you wanna find")
parser.add_argument("-min", "--minplayers", type=int, default=0, required=False,
                    help="you can specify the minecarft server you wanna find")
parser.add_argument("-d", "--debug", type=bool, default=False, required=False,
                    help="If specified, each request will be printed with response and reasxon")
args = parser.parse_args()

print('Multithreaded mass minecraft server status checker by Footsiefat/Deathmonger')

time.sleep(1)

inputfile = args.inputfile
f = open(args.publicserverlist, 'r')
public_server_ips = set(f.read().split(" "))
f.close()
outfile = open(args.outputfile, 'a+')
existing_server_ips = set(outfile.read().split(" "))
outfile.close()
searchterm = args.version
thread_count = args.threads
minplayers = args.minplayers
fileHandler = open(inputfile, "r")
masscan_output = fileHandler.readlines()
fileHandler.close()
server_ips = [line.strip().split(' ', 4)[3] for line in masscan_output if line.strip()[0] != "#"]
exitFlag = 0

total_servers = len(server_ips)


def ping_server(ip) -> Tuple[bool, Union[str, PingResponse]]:
    try:
        # raise Exception
        return True, JavaServer(ip, 25565).status()
    except Exception as e:
        return False, f"[ FAIL ] IP: {ip} failed with exception: {e}"


def log_data(ip):
    success, resp = ping_server(ip)

    if success and (
            resp.players.online > minplayers and (searchterm == "" or searchterm == resp.version.name.split(' ')[0])):
        log = f"{ip} {resp.version.name.replace(' ', '_')} {resp.players.online}"
        with lock:
            with open(args.outputfile,'a')as f:
                f.write(str(log))
        print(f'[ SUCC ] {log}')
    elif args.debug:
        print(resp)



with Pool(thread_count) as p:
    for _ in tqdm.tqdm(p.imap_unordered(log_data, server_ips), total=len(server_ips)):
        pass


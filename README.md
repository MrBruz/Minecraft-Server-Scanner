# Minecraft-Server-Scanner

Let's you scan the entire internet in a couple of hours and identify all Minecraft servers on IPV4

**Installation:**

```
sudo apt install masscan (Or distro specific installer command)
wget https://raw.githubusercontent.com/robertdavidgraham/masscan/master/data/exclude.conf
pip3 install mcstatus
pip3 install dhooks
```

**start scanning for servers:**

```
sudo masscan -p25565 0.0.0.0/0 --max-rate <maxrate> --excludefile exclude.conf -oL masscan.txt (Set maxrate to a limit that you are comfortable with and won't melt your router)
```

**find real minecraft servers from the results of the scan:**

```
python mcscanner.py -i masscan.txt -o result.txt -p public.txt -c dicord hock adress
```

###### for more infomation you can always get help by typing ```python mcscanner.py -h```

- For filtering out public servers you can use my public.txt file but it will probably be a bit outdated by now
- Hit enter and wait for my program to check and grab the metadata for all the servers found, once this is done you will
  have a massive amount of servers (A lot of them being private ones) to have some fun with. The output file includes
  the IP Address, Version and Current Players online of found servers.

**DISCLAIMER: THIS IS FOR EDUCATIONAL PURPOSES ONLY AND I AM NOT RESPONSIBLE FOR ANY MISUSE OF THESE TOOLS!**

# Minecraft-Server-Scanner
Lets you scan the entire internet in a couple of hours and identify all Minecraft servers on IPV4


**Installation:**
```
sudo bash install.sh
```

**start scanning for servers:**
```
sudo masscan -p25565 0.0.0.0/0 --max-rate <maxrate> --excludefile exclude.conf -oL masscan.txt (Set maxrate to a limit that you are comfortable with and won't melt your router)
```

**find real minecraft servers from the results of the scan:**
```
mcscanner -i masscan.txt -o result.txt -p public.txt
```

###### for more information you can always get help by typing ```mcscanner -h```

- For filtering out public servers you can use my public.txt file, but it will probably be a bit outdated by now
- Hit enter and wait for my program to check and grab the metadata for all the servers found, once this is done you will have a massive amount of servers (A lot of them being private ones) to have some fun with. The output file includes the IP Address, Version and Current Players online of found servers.

**DISCLAIMER: THIS IS FOR EDUCATIONAL PURPOSES ONLY AND I AM NOT RESPONSIBLE FOR ANY MISUSE OF THESE TOOLS!**

This program is license unter the [GNU GENERAL PUBLIC LICENSE](LICENSE)
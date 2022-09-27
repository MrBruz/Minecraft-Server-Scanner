#!/usr/bin/bash
mkdir /usr/local/bin
# Copy python file into /usr/bin
cp ./mcscanner.py /usr/local/bin/mcscanner

# get the disctro specific package manager
declare -A osInfo;
osInfo[/etc/redhat-release]=yum install
osInfo[/etc/arch-release]=pacman -S
osInfo[/etc/gentoo-release]=emerge --ask --verbose
osInfo[/etc/SuSE-release]=zypper install
osInfo[/etc/debian_version]=apt-get install
osInfo[/etc/alpine-release]=apk add
 
# I stall masscan
for f in ${!osInfo[@]}
do
    if [[ -f $f ]];then
        sudo ${osInfo[$f]} masscan python pip
    fi
done

cd /usr/local/bin/ || exit

# Get exclude file
wget https://raw.githubusercontent.com/robertdavidgraham/masscan/master/data/exclude.conf

# Install mcstatus from pip
pip install mcstatus

echo "Successfully installed mc-scanner!"
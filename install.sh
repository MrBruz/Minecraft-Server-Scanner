#!/usr/bin/bash
mkdir /usr/local/bin
# Copy python file into /usr/bin
cp ./mcscanner.py /usr/local/bin/mcscanner

# Install masscan
sudo apt install masscan

cd /usr/local/bin/ || exit

# Get exclude file
wget https://raw.githubusercontent.com/robertdavidgraham/masscan/master/data/exclude.conf

# Install mcstatus from pip
pip3 install mcstatus

echo "Successfully installed mc-scanner!"
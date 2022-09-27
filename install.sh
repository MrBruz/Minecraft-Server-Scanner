#!/usr/bin/bash
mkdir /usr/bin

# Copy python file into /usr/bin
cp ./mcscanner.py /usr/bin/mcscanner

# get the distro specific package manager
packagesNeeded='masscan python pip'
# shellcheck disable=SC2086
if [ -x "$(command -v apk)" ];       then sudo apk add --no-cache $packagesNeeded
elif [ -x "$(command -v apt-get)" ]; then sudo apt-get install "$packagesNeeded"
elif [ -x "$(command -v dnf)" ];     then sudo dnf install "$packagesNeeded"
elif [ -x "$(command -v zypper)" ];  then sudo zypper install "$packagesNeeded"
else echo "FAILED TO INSTALL PACKAGE: Package manager not found. You must manually install: $packagesNeeded">&2; fi

cd /usr/bin/ || exit

# Make file globally executable
chmod +x mcscanner

# Get exclude file
wget https://raw.githubusercontent.com/robertdavidgraham/masscan/master/data/exclude.conf

# Install mcstatus from pip
pip install mcstatus

echo "Successfully installed mc-scanner!"
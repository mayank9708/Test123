#!/bin/bash
Host_file="host.txt"
if [[ ! -f "$Host_file" ]]; then
	echo "FILE NOT FOUND : $Host_file"
	exit 1
fi
while IFS= read -r HOST;do
	echo " Pinging $HOST..."
	ping -c 4 "$HOST"
done < "$Host_file"

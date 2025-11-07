#!/bin/bash

# Prompt User
read -p "What hosts to ping? " -a hosts

for ip in "${hosts[@]}"
do
  (
    if [[ "$1" == "-4" || -z "$1" ]]; then
        result=$(ping -4 -c 1 "$ip" 2>/dev/null)
    elif [[ "$1" == "-6" ]]; then
        result=$(ping -6 -c 1 "$ip" 2>/dev/null)
    fi

    # Extract full IPv4 or IPv6 address
    host_ip=$(echo "$result" | sed -n 's/^PING[^(]*(\([^)]*\)).*/\1/p')


    if echo "$result" | grep -q "time="; then
        echo "$ip ($host_ip) replied"
    else
        echo "$ip ($host_ip) failed"
    fi
  ) &
done

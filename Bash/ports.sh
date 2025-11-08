#!/bin/bash
host="$1"
shift
ports=("$@")

if [[ -z "$host" || ${#ports[@]} -eq 0 ]]; then
  echo "Usage: $0 <host> <port1> <port2> ..."
  exit 1
fi

for port in "${ports[@]}"; do
  (echo >/dev/tcp/$host/$port) &>/dev/null && \
    echo "Port $port open on $host"
done

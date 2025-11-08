#!/bin/bash
iface="${1:-eth0}"
outfile="capture_$(date +%F_%H%M).pcap"

sudo tcpdump -i "$iface" -w "$outfile"

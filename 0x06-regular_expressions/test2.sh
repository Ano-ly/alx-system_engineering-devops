#!/bin/bash

# Get IPv4 addresses using ifconfig and filter out loopback and inactive interfaces
ipv4_addresses=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | awk '{print $2}' | grep -v '^127\.' | grep -v '^0\.' | grep -v '^255\.' | grep -v '^10\.' | grep -v '^172\.[16-31]\.' | grep -v '^192\.168\.')

# Print the IPv4 addresses
echo "Active IPv4 addresses:"
echo "$ipv4_addresses"

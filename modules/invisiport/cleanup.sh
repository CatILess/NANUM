#!/bin/bash

#simple cleanup script
#will flush iptables

iptables -F
iptables -t nat -F
> /tmp/blacklist

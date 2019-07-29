#!/usr/bin/env python
import socket
import os
import argparse
import re




#get whitelist
parser = argparse.ArgumentParser()

parser.add_argument('-c', dest='config', help = 'config file path', required=True)

args = parser.parse_args()

config = {} 


rx_dict = {
    'blacklist': re.compile(r'blacklist\s?:\s?(?P<blacklist>.*)\n'),
    'whitelist': re.compile(r'whitelist\s?:\s?(?P<whitelist>.*)\n'),
	'bindport': re.compile(r'bindport\s?:\s?(?P<bindport>.\d+)\n'),
	'fakeport' : re.compile(r'fakeport\s?:\s?(?P<fakeport>.*)\n'),
    'chainport' : re.compile(r'chainport\s?:\s?(?P<chainport>.*)\n'),
	'chain' : re.compile(r'chain\s?:\s?(?P<chain>.*)\n')
	}

def get_config():

	with open(args.config,"r") as fi:
		line = fi.readline()
		while line:
			key, match = _parse_line(line)

			if key == 'blacklist' :
				config['blacklist']= match.group('blacklist')
				
			elif key == 'whitelist' :
				config['whitelist'] = match.group('whitelist').split(',')

			elif key == 'bindport' :
				config['bindport'] = int(match.group('bindport'))

			elif key == 'fakeport' :
				ports = match.group('fakeport').split(',')
				config['fakeport'] = []
				for p in ports:
					config['fakeport'].append(int(p.strip()))
			if key == 'chainport' :
				ports = match.group('chainport').split(',')
				config['chainport'] = []
				for p in ports:
					config['chainport'].append(int(p.strip()))
			if key == 'chain':
				chain = match.group('chain').split(',')
				config['chain'] = []
				for c in chain :
					pair = c.strip().split('-')
					pair[0] = int(pair[0])
					pair[1] = int(pair[1])

					config['chain'].append(pair)

			line = fi.readline()

	fi.close()


def _parse_line(line):

    for key, rx in rx_dict.items():
        match = rx.search(line)
        if match:
            return key, match
    # if there are no matches
    return None, None

##############################

get_config()

print (config['chain'])

#hosts to avoid blacklisting
whitelist = config['whitelist']

#ports to show as up to blacklisted clients
#Think about what the attacker will think if he sees different profiles before and after a scan
ports = config['fakeport']


#IP to bind to.  Leave as empty string to bind to all available IPs
addr=''

#Port to bind to.  This will be the listening port.  A scan here will trigger the defenses
bp = config['bindport']


#Name of blacklist file
filename = config['blacklist']

def add_blacklist(ip):
	fi = open(filename,"a")
	fi.write(" "+ip)
	fi.close()

def check_blacklist(ip):
	
	fi = open(filename,"a+")
	data = fi.read()
	fi.close()
	return ip in data

def blacklist(ip):
	if ip in whitelist or check_blacklist(ip):
		return False
	else:
		#drop except cowrie and portspoof
		query = "iptables -I INPUT 1 -s %s -p tcp -m multiport ! --destination-port " % (ip)
		query += ','.join(str(x) for x in config['chainport'])
		query += " -j DROP"
		print (query)
		os.system(query)

		for chain in config['chain']:
			query = "iptables -t nat -A PREROUTING -s %s -p tcp --dport %d -j REDIRECT --to-port %d" % (ip,chain[0], chain[1])
			os.system(query)
			print (query)
		add_blacklist(ip)
	return True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((addr,bp))
s.listen(5)

while True:
	con, adr = s.accept()
	try:
		data = con.recv(2048)
		con.send("Protocol Error")
		con.close()
	except:
		print "Socket error"
	blacklist(adr[0])

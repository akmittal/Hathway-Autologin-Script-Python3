import sys, time, socket, urllib.request

userName="username"
password="password"

sleepTime=30
socket.setdefaulttimeout(sleepTime)

hostname = ['login.hathway.com', '203.212.193.60', '203.212.193.61']
url = "/bsp/login.do?action=doLoginSubmit&flowId=UserLogin&username=" + userName + "&password=" + password

file=None
if file is None:
	#try:
	fh = open("hathway.log", 'w')
	#except IOError:
	#	print "Couldn't write to file /tmp/hathway.log";
else:
	try:
		fh = open(file, 'w')
	except IOError:
		print ("Couldn't write to file %s\n" % (file))

def setup():
	if len(sys.argv) > 1:
		userName=sys.argv[1]
		password=sys.argv[2]
		sleepTime=sys.argv[3]
	
def local_write(str):
	sys.stdout.write(str)
	fh.write(str)
	fh.flush()

def checkInternetConnectivity():
	x = 1
	try:
		socket.create_connection( ("www.google.com", 443) )
	except:
		x = 0
	finally:
		return x

def connectToHathway():

	if len(hostname) == 0:
		sys.exit(1)
	else:
		for host in hostname:
			real_host = "http://" + host + url
			try:
			    opener = urllib.request.build_opener()
			    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
			    opener.open(real_host)
			    print(real_host)
			except:
				local_write("%s\tFailed to connect to %s Retrying\n" % (time.ctime(), real_host) )
				continue
	
setup()
while 1==1:
	if checkInternetConnectivity() == 0:
		local_write("%s\tInternet connectivity is dead. Trying to contact Hathway auth severs.\n" % (time.ctime() ) )
		connectToHathway()
		time.sleep(sleepTime)
		continue
	else:
		local_write("%s\tInternet connectivity alive. Sleeping for %s seconds.\n" % (time.ctime(), sleepTime) )
		time.sleep(sleepTime)
		continue 
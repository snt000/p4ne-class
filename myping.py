import pyping

response = pyping.ping("8.8.8.8")
if response.ret_code == 0:
	print "reachable"
else:
	print "unreachable"

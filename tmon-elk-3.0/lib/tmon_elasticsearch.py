import httplib
def InsertIndex( document ):
	conn = httplib.HTTPConnection("www.google.com")
	conn.request("GET", "index.html?gfe_rd=cr&amp;ei=WU9OVpL2L4eq8wfek5bYCA")
	r1 = conn.getresponse()
	print r1.status, r1.read()
	data1 = r1.read()
	conn.close()

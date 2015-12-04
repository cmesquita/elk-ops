import httplib, urllib
def InsertIndex():
	params = "{\"nome\": \"cesar\" , \"idade\" : \"33\" }"  
	headers = {"Content-type": "application/json","Accept": "text/plain"}
	conn = httplib.HTTPConnection("192.168.47.197:9200")
	conn.request("PUT", "/arrayind5/test/2", params, headers)
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	print data
	conn.close()
if __name__ == "main":
	InsertIndex()

import httplib, urllib
def InsertIndex( stacklist ):
	for i in stacklist:
		#print i[0]
		x = str(i[1])
		newstr = x.replace("\'", "")
		newstr = newstr.replace("\"", "")
		newstr = newstr.replace("\n","")
		newstr = newstr.replace("\t","")	
		params = "{ \"hash\":\"" + i[0] + "\",\"stack\":\"" + str(newstr) + "\" }"
		#print params
		#print newstr
		headers = {"Content-type": "application/json","Accept": "text/plain"}
		conn = httplib.HTTPConnection("192.168.47.197:9200")
		conn.request("PUT", "/tmon3/stackhash/"+ i[0] , params, headers)
		response = conn.getresponse()
		print response.status, response.reason
		data = response.read()
		#this prints the elasticsearch response data		
		#print data
		conn.close()
if __name__ == "main":
	InsertIndex()

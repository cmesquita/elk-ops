inFile = open("data.txt")
outFile = open("result.txt", "w")
buffer = ""
keepCurrentSet = False
for line in inFile:
	#if line.find('INSTANCE 1'):
	if "INSTANCE 1" in line:
        	#---- starts a new data set
		buffer += line
		keepCurrentSet = True
	else:
		if ( line == '\n' and keepCurrentSet == True ):
			break
		elif keepCurrentSet:
			buffer += line
print "aqui e o valido"
print buffer	
outFile.write(buffer)
inFile.close()
#outFile.close()

def extractStackTrace( file, threadid ):
	inFile = open("data.txt")
	buffer = ""
	keepCurrentSet = False
	for line in inFile:
		#if line.find('INSTANCE 1'):
		if threadid in line:
        		#---- starts a new data set
			buffer += line
			keepCurrentSet = True
		else:
			if ( line == '\n' and keepCurrentSet == True ):
				break
			elif keepCurrentSet:
				buffer += line
	return buffer	
	inFile.close()

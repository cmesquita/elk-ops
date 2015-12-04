def extractStackTrace( file, threadid ):
	inFile = open( file )
	print "opening: " + file
	buffer = ""
	keepCurrentSet = False
	for thread in threadid:
		print "iniciando thread:  " + thread
		keepCurrentSet = False
		inFile = open( file )
		for line in inFile:
			#if line.find('INSTANCE 1'):
			if thread in line:
        			#---- starts a new data set
				buffer += line
				keepCurrentSet = True
			else:
				if ( line == '\n' and keepCurrentSet == True ):
					buffer += line
					break
				elif keepCurrentSet:
					buffer += line
		inFile.close()
	return buffer
	#inFile.close()

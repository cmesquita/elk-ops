def extractStackTrace( file, threadid ):
	inFile = open( file )
	print "opening: " + file
	keepCurrentSet = False
	stack_list = []
	for thread in threadid:
		keepCurrentSet = False
		inFile = open( file )
		buffer = ""
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
		stack_list.append( buffer )
	return stack_list
	#inFile.close()

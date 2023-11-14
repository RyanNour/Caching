

def printMenu():
	print("choose an option: \n")
	print("browser caching\t  1")
	print('Client Server\t  2')
	print('Peer-To-Peer\t  3')
	print("Exit \t\t  4")
	# just add the rest 

def browserCaching():
	print("Welcome to the browser caching time solver-er")
	RTT = input('Start with the RTT time: ')
	NUM_PACKETS = input('Now the number of packets: ')
	PERCENT_NOT_CACHED = input('What is the percentage cached\n (Note: just the number, no \% symbol)')
	TRANS_DELAY = input('Finally, the server transmission delay: ')

	PERCENT_NOT_CACHED = 100 - int(PERCENT_NOT_CACHED)
	answer = (int(RTT) * int(NUM_PACKETS)) + (int(NUM_PACKETS) * (PERCENT_NOT_CACHED / 100) * float(TRANS_DELAY))
	formatAnswer(round(answer, 2))

def peerToPeer():
	print('lets gather some info')
	
	fileSize = input('Size of the File (just the number):\t')
	
	# use this as a multiplyer later
	unitOfMeasure = input('Is that in gbits or mbits? \t')
	
	if unitOfMeasure == 'gbits':
		unitMultiplier = 1000
	else: 
		unitMultiplier = 1

	numberOfPeers = input('Number Of Peers: ')
	serverUpload = input('Server Upload speed:\t')
	slowestPeerDownSpeed = input('Slowest Peer download speed:\t')
	slowestPeerNum = input('What is the number of the slowest peer?\t')
	sumOfPeerUploads = input('Sum of all the peer upload speeds:\t')
	
	# start the math here
	# server upload
	serverSpeed = (int(fileSize)/float(serverUpload)) * int(unitMultiplier)

	#client download
	clientDownSpeed = (int(fileSize)/float(slowestPeerDownSpeed)) * int(unitMultiplier)

	# all to gether now
	peersSpeed = (int(numberOfPeers) * int(fileSize))/(float(serverUpload) + float(sumOfPeerUploads)) * unitMultiplier
	answer = max(float(peersSpeed), float(clientDownSpeed), float(serverSpeed))
	if answer == serverSpeed:
		rootCause = 'ServerSpeed'
	elif answer == clientDownSpeed:
		rootCause = 'Client Download Speed'
	elif answer == peersSpeed:
		rootCause = 'Peer Speed (Combined Upload)'
	formatAnswer(round(answer, 2))
	print('The root cause:\t ' + str(rootCause))


def clientServer():
	print('\n\n**************CLIENT SERVER MODEL***********************\n\n ')
	fileSize = input('Size of the File (just the number):\t')
	unitOfMeasure = input('Is that in gbits or mbits? \t')
	numberOfPeers = input('total number of peers:\t')
	serverUploadRate = input('Server Upload rate:\t')
	slowestPeerDownSpeed = input('Slowest Peer download speed:\t')
	slowestPeerNum = input('What is the number of the slowest peer?\t')
	upBottleNeck = (int(numberOfPeers) * int(fileSize))/float(serverUploadRate)
	downBottleNeck = int(fileSize) / float(slowestPeerDownSpeed)
	if upBottleNeck > downBottleNeck :
		finalAnswer = upBottleNeck
		rootCause = upBottleNeck
	else :
		finalAnswer = downBottleNeck
		rootCause = downBottleNeck
	if unitOfMeasure == 'gbits':
		finalAnswer = finalAnswer * 1000
	
	if rootCause == downBottleNeck:
		rootCause = 'Cliient number: ' + str(slowestPeerNum)
	elif rootCause == upBottleNeck:
		rootCause = 'Server Upload Speed'
	print('==================================================================\n\n')
	print('it will take ' + str(round(finalAnswer, 2)) + 'ms')
	print('Root Cause of the bottleneck is: ' + rootCause)

def formatAnswer(answer):
	print('==================================================================\n\n')
	print('**\t\tIt should take: ' + str(answer) + 'ms\t\t\t**')
	print('\n\n==================================================================\n\n')


# just a flag to break the loop
quit = False

# this is the main loop
while quit == False:
	printMenu()
	choice = input('Your choice:\t')

	if choice == '4':
		quit = True
		print('Bye')
	elif choice == '1':
		browserCaching()
	elif choice == '2':
		clientServer()
	elif choice =='3':
		peerToPeer()

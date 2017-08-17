filename = 'port-harcourt-weather.txt' 
with open(filename) as file:
	next(file)
	next(file)
	dayList = []
	dailyTempSpread = []
	for line in file:
		splitted_line = line.split()
		#print splitted_line[0], splitted_line[1], splitted_line[2]
		#dayList.append(splitted_line[0])
		try:
			dayListNum = int(splitted_line[0])
			dailyHigh = int(splitted_line[1])
			dailyLow = int(splitted_line[2])
			#print int(splitted_line[0])
		except ValueError:
			pass
		dailyTempSpread.append(dailyHigh - dailyLow)
		dayList.append(dayListNum)
		#dailyTempSpread.append(int(splitted_line[1]) - int(splitted_line[2])
	weatherDict = dict(zip(dayList, dailyTempSpread))
	print weatherDict
	#print len(dayList)
	#print len(dailyTempSpread)	

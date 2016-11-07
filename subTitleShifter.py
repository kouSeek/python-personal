import re

def main():
	subFileName = raw_input("Enter the Subtitle full name: ")
	shiftAmount = input("Enter the time to be shifted in seconds(+/-): ")

	subHandle = open(subFileName, 'r')
	subTitle = subHandle.read()
	shiftedSubTitle = re.sub(r'(\d\d:\d\d:\d\d)', lambda m: shiftTime(m.group(1), shiftAmount), subTitle)

	shiftedSubFileHandle = open('synced_' + subFileName, 'w')
	shiftedSubFileHandle.write(shiftedSubTitle)
	shiftedSubFileHandle.close()

def shiftTime(time, shift):
	timeArray = map(int, time.split(':'))
	if shift >= 0:
		if timeArray[2] + shift >= 60:
			timeArray[2] += shift - 60
			if timeArray[1] + 1 >= 60:
				timeArray[1] = 0
				timeArray[0] += 1
			else:
				timeArray[1] += 1
		else:
			timeArray[2] += shift
	else:
		if timeArray[2] + shift <= 0:
			timeArray[2] += shift + 60
			if timeArray[1] == 0:
				timeArray[1] = 59
				timeArray[0] -= 1
			else:
				timeArray[1] -= 1
		else:
			timeArray[2] += shift

	return ":".join(str("%02d"%i) for i in timeArray)



if __name__ == '__main__':
	main()

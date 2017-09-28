import urllib.request
import re


def find_power(s):
	p = re.compile("\^")
	match = p.search(s)
	if match:
		match = match.span()[0]
		return s[:match], s[match+1:]
	else:
		return None


link = "http://mersennus.net/fibonacci/f1000.txt"
fileName, headers = urllib.request.urlretrieve(link)
file = open(fileName, "r")


numbers = []
for line in file.readlines():
	line = line.strip(" \n")
	line = line.split("= ")
	line = line[1].split(" * ")
	newLine = []
	for l in line:
		power = find_power(l)
		if power:
			for i in range(int(power[1])):
				newLine.append(power[0])
		else:
			newLine.append(l)
	numbers.append(newLine)


with open("fibonacci.txt", "w") as f:
	for line in numbers:
		for l in line:
			f.write(l + " ")
		f.write("\n")
			
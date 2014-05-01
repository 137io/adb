
""" Euler 79
->Sample Output:
Inet time: 0.384672880173
Real run time 0.000158071517944
73162890
-> Why this problem:
I like security stuff in general. Also, I was able to solve this by hand faster and writing an algorithm for it was not 
resolved in a few brain cycles,which made it interesting.

-> A description of the process you followed in solving the problem:
Given fact is that input is an orderedList, each record upto three characters (numbers). Started with a different approach but quickly realized
that using a static 1..9 will not work. Graphed out each character's reach with other numbers from the set and from there a simple depth count
of each character did the trick. 
-> Sources:
http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value
https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions
-> Time Spent:
~20 minutes + 15 minutes documenting,beautifying .
"""
import urllib2, timeit, httplib

def bankpass79():
""" Main function.
Download the file"""
	url="http://projecteuler.net/project/keylog.txt"
	s=timeit.default_timer()
	try:
		print "Fetching from Internet"
		response = urllib2.urlopen(url)
		html=response.read()
	except Exception, e:
	    print('generic exception:' + str(e))

	e=timeit.default_timer()
	print "Inet time:",e-s

	if not html:
		print "network issues?	"
		exit

	# Input verbatim, uncomment if network issues, comment the code above.
	#inputList=['319', '680', '180', '690', '129', '620', '762', '689', '762', '318', '368', '710', '720', '710', '629', '168', '160', '689', '716', '731', '736', '729', '316', '729', '729', '710', '769', '290', '719', '680', '318', '389', '162', '289', '162', '718', '729', '319', '790', '680', '890', '362', '319', '760', '316', '729', '380', '319', '728', '716']
	inputList=[]
	s=timeit.default_timer()
	inputList=html.strip().split("\n")
	l=sorted(set(inputList))

	possibleList=set() #only uniques
	connectedSet={}
	for i in inputList: #all inputs []
		for j in i: # each input ex: 3,1,9
			possibleList.add(j)

	for e in possibleList: 
		connectedSet[e]=set() # going to record unique subsets

	for sCode in l:
			connectedSet[sCode[0]].add(sCode[1]) #a,b
			connectedSet[sCode[0]].add(sCode[2]) #a,c
			connectedSet[sCode[1]].add(sCode[2]) #b,c

	#for set in connectedSet, sort items by the number of characters they are connected to:
	passcode=''
	for e in sorted(connectedSet.items(),key= lambda setLength: setLength[1], reverse=True):
		passcode+=e[0]
	e=timeit.default_timer()

	print "Real run time",e - s
	print passcode

if __name__ == "__main__":
	bankpass79()
#print topLevelSet

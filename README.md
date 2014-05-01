Euler 112
->Sample Output:
1587000
5.39340400696
[Finished in 5.4s]
-> Why this problem:
Seemed like a good start.
-> A description of the process you followed in solving the problem:
This was easy - OK. Most of my time was spent on figuring out the pattern but then I just brute forced my wa$
to submit for this test. Will revisit soon.
First iteration was typecasting number to a string and using built-in functions to manipulate parts.
Second thought - teration was to use a list (sort)
Third iteration, use simple mod and div functions and compare selective parts of the number with former and $
A simple optimization was to use the info given in problem statement.
-> Sources:
-> Time Spent:
~1 hour.

Euler 59
->Sample Output:
107359
0.0134971141815
-> Why this problem:
I like security stuff in general.
-> A description of the process you followed in solving the problem:
Wrote down the "Givens" in problem statement. Mind raced towards a brute solution easily but I spent next 30-60 seconds analysing the cryption 
rules to find a weak link. 
This is the second iteration (beautified version, no change in logic). Have added code to extend this to characters other than ASCII 32. 
Very simple: Language is English (given), 3 characters key (given), all lower case key (given). Loop over cipher in blocks of 3,  evaluate 'XOR cipher code with possibleKeyChars == space'  while populating 
a list with match/notmatch counts. Retrieve the key by maximum count.
-> Sources:
-> Time Spent:
~5 minutes + 35 minutes documenting,beautifying .

Euler 79
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

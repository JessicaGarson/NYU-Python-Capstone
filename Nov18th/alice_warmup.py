#! usr/bin/env python

def vowel():
	s='make a function that removes all vowels from a sentense.'
	vowels = ('a', 'e', 'i', 'o', 'u', 'y')
	s1=[]
	for l in s:
		if l in vowels:
			s1=s.replace(l, "")
			return s1
	print (s1)

s='make a function that removes all vowels from a sentense.'

if __name__ == "__main__":
	vowel()
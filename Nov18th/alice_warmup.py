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
	
# #! usr/bin/env python

# def vowel(sentance):
# 	vowels = ('a', 'e', 'i', 'o', 'u', 'y')
# 	s1 = []
# 	for l in s:
# 		if l not in vowels:
# 			s1.append(l)
# 	return ''.join(s1)
# if __name__ == "__main__":

# 	s='make a function that removes all vowels from a sentense.'
# 	print(vowel(s))

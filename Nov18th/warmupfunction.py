#!/usr/bin/env python



def vowel(s):
	result = []
	vowels = ['a', 'o', 'i', 'u', 'e']
	for i in s:
		if i in vowels:
			continue
		else:
			result.append(i)
	r2 = ''.join(result)
	return r2

sentence = 'Hi I am a sentence, who are you, where are you going and at what speed'
print(vowel(sentence))

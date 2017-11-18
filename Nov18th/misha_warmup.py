# remove vowels from a sentance

def remove_vowels(sentance):
	vowels = ( 'a', 'e', 'i', 'o', 'u')
	return ''.join([l for l in sentance if l not in vowels])

if __name__ == '__main__':
	print(remove_vowels('what are you up to?'))
# remove vowels from a sentance

def remove_vowels(sentance):
	return ''.join([l for l in sentance if l not in ('a','e','i','o','u')])

if __name__ == '__main__':
    print(remove_vowels(input('Enter a sentence: ')))

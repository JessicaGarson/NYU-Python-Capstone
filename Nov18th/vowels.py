def del_vowels(sentence):
    sentence = list(str(sentence))
    vowels = ['a','e','i','o','u']
    for letter in sentence:
        if letter in vowels:
            sentence.remove(letter)
    return ''.join(sentence)

def get_sentence():
    sentence = input('Enter a sentence: ')
    return sentence

if __name__ == "__main__":
    sentence = get_sentence()
    sentence_no_vowels = del_vowels(sentence)
    print(sentence_no_vowels)
    

def del_vowels(sentence):
    sentence = str(sentence)
    vowels = ['a','e','i','o','u']
    sentence_no_vowels = sentence
    for letter in sentence:
        if letter in vowels:
            sentence_no_vowels = sentence_no_vowels.replace(letter, "")
    return sentence_no_vowels

def get_sentence():
    sentence = input('Enter a sentence: ')
    return sentence

if __name__ == "__main__":
    sentence = get_sentence()
    sentence_no_vowels = del_vowels(sentence)
    print(sentence_no_vowels)
    

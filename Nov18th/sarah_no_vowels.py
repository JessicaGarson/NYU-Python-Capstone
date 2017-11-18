def no_vowels(sentence):
    vowels = 'aeiou'
    new_sentence = []
    for x in sentence:
        if x not in vowels:
            new_sentence.append(x)
    print(''.join(new_sentence))

sentence = "I love python class!"

if __name__ == '__main__':
    no_vowels(sentence)

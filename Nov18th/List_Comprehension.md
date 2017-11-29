# List Comprehension

## A traditional for loop
```python
for (set of values to iterate):
  if (conditional filtering):
    output_expression()
```

## List Comprehension
```python
[ output_expression() for(set of values to iterate) if(conditional filtering) ]
```

## Without List Comprehension
```python
def no_vowels(sentence):
    vowels = 'aeiou'
    filtered_list = []
    for l in sentence:
        if l not in vowels:
            filtered_list.append(l)
    return ''.join(filtered_list)
```

## With List Comprehension
```python
def no_vowels_lc(sentence):
    vowels = 'aeiou'
    return ''.join([ l for l in sentence if l not in vowels])
```

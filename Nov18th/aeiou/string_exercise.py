vowels=["o","u","a","i","e"]
text="ana is awesome"
new_text=[]

def rm_vowels(x):
	for t in text:
		if t not in vowels:
			new_text.append(t)
	print("".join(new_text))

		




rm_vowels(text)


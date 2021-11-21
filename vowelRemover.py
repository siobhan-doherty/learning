# Program takes some text & returns a list of all characters
# that are non-vowel sorted in alphabetical order.

vowels = "aeiouAEIOU"
text = input("Enter text: ")
sample_set = set(text).difference(vowels)
print(sorted(sample_set))

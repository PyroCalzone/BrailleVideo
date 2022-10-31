import unicodedata

dictionary = {}

braille_start = 0x2800
braille_end = 0x28ff

for i in range(braille_start, braille_end+1):
    c = chr(i)
    name = unicodedata.name(c)
    number = name.rsplit('-')[-1]
    dictionary[number] = c

sortedList = sorted(dictionary.items(), key=lambda x: x[0])

sortedDictionary = {}
for key, value in sortedList:
    sortedDictionary[key] = value

print("brailleDictionary = {")
for key, value in sortedDictionary.items():
    print(f"'{key}': '{value}',")
print("}")
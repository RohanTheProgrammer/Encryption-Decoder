str1 = input(u"\u001b[1m\u001b[36mEnter the encoded value:\n\u001b[0m")
array = str1.split('.')
array.pop(0)
nsentence = []
for i in range(2,len(array),3):
    char = int(array[i])+int(array[i-1])+int(array[i-2])
    nsentence.append(char)
# print(nsentence)
# Program to find most frequent number
def most_frequent(List):
	return max(set(List), key = List.count)

# result
Key = most_frequent(nsentence)-32
print(u"\u001b[1m\u001b[33mKey Value:\u001b[32m", str(Key), u"\u001b[0m")

# Decoding Sentence
string = ''
for i in nsentence:
    string = string + chr(i-Key)
print(u"\u001b[1m\u001b[33mDecoded String:\u001b[32m", string, u"\u001b[0m")

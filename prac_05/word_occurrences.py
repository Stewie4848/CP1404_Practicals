text = input("Text: ")
words = text.split(" ")
words.sort()
word_dict = {}
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

max_length = max((len(word) for word in words))

for word in word_dict:
    print("{:{}} = {}".format(word, max_length, word_dict[word]))

text = input("Text: ")
words = text.split(" ")
words.sort()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_length = max((len(word) for word in words))

for word in sorted(list(word_count.keys())):
    print("{:{}} = {}".format(word, max_length, word_count[word]))

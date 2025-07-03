"""
Word Occurrences
Estimate: 30 minutes
Actual:   16 minutes
"""

text = input("Enter the text: ")
words = text.split()
word_count = {}

for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word,0) + 1

max_len = max(len(word) for word in word_count)
sorted_count = sorted(word_count)
for word in sorted_count:
    print(f"{word:<{max_len}} : {word_count[word]}")

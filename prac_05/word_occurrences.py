"""
Word Occurrences
Estimate: 30 minutes
Actual:   32 minutes
"""

text = input("Enter the text: ")
words = text.split()
word_count = {}

for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word,0) + 1

max_len = max(len(word) for word in word_count)
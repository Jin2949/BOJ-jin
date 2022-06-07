import sys

word_1 = input()
word_2 = word_1[::-1]

if word_1 == word_2:
    print(1)
else:
    print(0)
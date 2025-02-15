def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())
word1 = input().strip()
word2 = input().strip()
if are_anagrams(word1, word2):
    print("Слова являются анаграммами.")
else:
    print("Слова не являются анаграммами.")
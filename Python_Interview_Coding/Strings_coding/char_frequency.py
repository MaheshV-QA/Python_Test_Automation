def char_count(s):
    freq = {}
    for char in s.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(char_count("Automation"))
# ===================================================================================================================================
word = "Automation"
freq = {}

for char in word:
    if char in freq:
        freq[char] +=1

    else:
        freq[char] =1

print(freq)
#output: {'a': 2, 'u': 1, 't': 1, 'o': 1, 'm': 1, 'i': 1, 'n': 1}

# ==============================================================================================

from collections import Counter

word = "Automation"
char_count = Counter(word.lower())
print(char_count)
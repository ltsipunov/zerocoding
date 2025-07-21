def count_vowels(s):
    is_vowel = lambda c: c.lower() in 'aeiouy'
    return sum( [  [0,1][is_vowel(c)] for c in s ] )
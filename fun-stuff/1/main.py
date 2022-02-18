class WordDictionary:
    def __init__(self, words):
        self.words = words

    def is_word(self, word):
        return word in self.words
      
    def word_starts_with(self, partial_word):
        for word in self.words:
            if word.startswith(partial_word):
                return True
        return False

dictionary = WordDictionary([
    "A", 
    "ACT", 
    "ACTION",
    "ALARM",
    "BICYCLE", 
    "CAR",
  	"LLAMA",
  	"MALL",
    "PAT",
    "PEEK",
    "QUOTE", 
    "TAP", 
])

letters = "MALR"

# Print all words that
# can be made using the letters in `letters`

# Using the dictionary above and the letters above, output should be:
# 
# A
# ALARM
# LLAMA
# MALL

# Your Code Goes Here

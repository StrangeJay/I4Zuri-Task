# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("race car") --> True

def find_anagrams(night, thing):

    if sorted(night) == sorted(thing):

        return True

    return False

print(find_anagrams('night', 'thing'))

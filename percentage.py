from difflib import SequenceMatcher

str1 = "Hello frozen World"
str2 = "frozen jelly world"

similarity_percentage = SequenceMatcher(None, str1, str2).ratio() * 100

print(similarity_percentage)

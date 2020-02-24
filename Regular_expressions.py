import re

text_to_search='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ ( )

nmims.edu

982-512-6754
886.765.5342

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = "Start a sentence and then bring it to an end"
#pattern = re.compile(r"abc")
#pattern = re.compile(r".")
#pattern = re.compile(r"\.")
#pattern = re.compile(r"nmims\.edu")
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

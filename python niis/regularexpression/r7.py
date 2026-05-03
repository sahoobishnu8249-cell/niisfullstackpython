import re
txt = "The rain in spain"
x = re.findall("[^a-z]",txt)
print(x)

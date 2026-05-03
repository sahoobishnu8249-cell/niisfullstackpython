import re
txt = "The rain in456 sp45ain"
x = re.findall("[0-9][0-9]",txt)
print(x)

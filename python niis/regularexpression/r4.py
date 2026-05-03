import re
result = re.sub(r'\d+', 'X', '123abcde56f')
print(result)
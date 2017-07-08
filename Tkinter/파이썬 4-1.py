import re

text="abc 123 def 456 dot map pat"

print(re.findall('d[a-z]\w|p[a-z]\w',text))

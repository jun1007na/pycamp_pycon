import calc as c
import re

print(c.add(1, 2))

m = re.search('(P(yth|l)|Z)o[pn]e?', 'Python')
print(m)

print(m.group())
print(m.group(0))
print(m.group(1))

# Lookahead = positive → (?=active) → (?!active) → (?=.*[^in]active)
# Lookbehind = negative → (?!active)
# Elas só checam se existe a palavra, a expressão regular que vai retornar o que está procurando.

import re
from pprint import pprint

texto = '''
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK inactive
OFFLINE 192.168.0.6 GHIJK active
'''

# Positive Lookahead verifica uma palavra depois, para retornar o que etá antes:
#pprint(re.findall(r'\w+\s*(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

# Negative Lookahead verifica uma palavra antes, para retornar o que etá depois:
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# Positive Lookahead:
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive Lookbehind:
# pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Negative Lookbehind:
# pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Positive Lookbehind:
#pprint(re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))

# Negative Positive:
pprint(re.findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))
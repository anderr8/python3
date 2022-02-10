# Greedy = guloso 
# No Greedy + não guloso

# Meta caractere: ^ $ ( )
# * 0 ou n
# + 1 ou n
# ? 0 ou n

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frae</p> <div></div>
'''
print(re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', texto))
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto)) 

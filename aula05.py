# Grupos e Retrovisores
# Meta Caracteres ^ $
# () -> grupos \1 -> retrovisores
# () ()   \1 \2
# (())    \1 \2 \3
# ?: -> indica que não é preciso ser salvo na memória
# \. -> representa um ponto

import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
'''

#print(re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', texto))

#tags = re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', texto)
#print(tags)
#pprint(tags)

#for tag in tags:
    #print(tag)
    #um, dois = tag
    #print(um, dois)
#    print(um)

#tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', texto)

#for tag in tags:
#    um, dois, tres = tag
#    print(tres)

#tags = re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', texto)
# pega só o texto
#pprint(tags)

#cpf = '147.852.963-12'
#print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}',cpf))
#print(re.findall(r'(([0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
#print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# grupo nominado:
#tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)
#tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
#pprint(tags)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS"\3 COISAS" \4', texto))
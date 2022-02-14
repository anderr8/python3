# Shorthands e flags importantes:
# shorthans → \w → representa todos e mais Maiúscula e minúsculas caracteres exemplo: [a-zA-Z0-9À-ú_]
# \w → [a-zA-Z0-9_] → flags=re.A ou flags=re.ASCII
# \W → [^a-zA-Z0-9À-ú_] → a letra maiscúla representa a negação
# \d → [0-9] representa número
# \D → [^0-9] → a letra maiúscula representa a negação dos números
# \s → [ \r\n\f\v\t] → representa os espaços em branco e quebras de linhas
# \S → [^ \r\n\f\v\t] → representa a negação dos espaços em brancos e quebras de linhas
#  \b → significa uma borda, que irá encontrar string vazia no começo ou no fim de cada palavra 
# \B → traz o inverso da palavra , negando a string vazia, não mostra o resto da palavra

import re

texto = '''
    João trouxe   flores para sua amada namorada em 10 de janeiro de 
1970, Maria era o nome dela.

    Foi um ano execelente na vida de joão. Teve 5 filhos todos adultos
atualmente. maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
    Não canso de ouvir a Maria:
    "Joooooooooãooooooo, café está prontinho aqui. Veeem"!
'''

# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z]+', texto))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# print(re.findall(r'\w+', texto, flags=re.I))
# print(re.findall(r'\W+', texto, flags=re.I))
# print(re.findall(r'\d+', texto, flags=re.I))
# print(re.findall(r'\D+', texto, flags=re.I))
# print(re.findall(r'\s+', texto, flags=re.I))
# print(re.findall(r'\S+', texto, flags=re.I))

# Exemplos de retorno de Bordas:
# print(re.findall(r'\be\w+', texto, flags=re.I))
# Inverso:
# print(re.findall(r'\w+e\b', texto, flags=re.I))
# palavras que tenham exatamente o números de letra que eu determinar:
# print(re.findall(r'\b\w{4} \b', texto, flags=re.I))
# negando uma borda:
print(re.findall(r'flo\B', texto, flags=re.I))
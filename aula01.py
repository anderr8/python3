# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

import re

# findall, search, sub => formas de pesquisa
# findall = encontre todas as ocorrências
# search = pesquise as ocorrências
# sub = substitua as palavras -> count=0 => padrão, count=1 => substitua uma palavra

# compile => reutilizo expressões regulares

# Teste ou teste -> palavras diferentes

# Exemplos:
# string = 'Este é um teste de expressões regulares'
# print(re.search(r'teste', string))

# string = 'Este é um teste de expressões teste regulares.'
# print(re.findall(r'teste', string))

string = 'Este é um teste de expressões teste regulares'
print(re.sub(r'teste', 'ABCD', string, count=0))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string, count=1))

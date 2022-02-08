# Meta caractere: . ^ $ * + ? { } \ | ( )
# | = barra reta no teclado paip
#. = significa qualquer caractere (com execeção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
 João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

 Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos 
atualmente. maria, hoje sua esposa, ainda faz café com pão de queijo nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso pão de queijo.
 Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café está prontinho aqui. Veeemm"!
'''


print(re.findall(r'João|Maria|ad....s', texto))
print(re.findall(r'João|joão|Maria', texto))
print(re.findall(r'[Jj]oão|[Mm]aria',texto))
print(re.findall(r'[a-z]aria', texto))
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', texto))
print(re.findall(r'jOÃO|mAriA', texto, flags=re.IGNORECASE))

# Quantificadores:
# Meta caracteres: ^ $ ( )
# * 0 ou n,  0 -> nenhum caractere, n caracteres ilimitados
# + 1 ou n {1,} -> 1 ou mais que um caractreres
# ? 0 ou 1 -> pode ou não existir um caractere
# {n}
# {min, max}
# {10,} 10 ou mais caracteres
# {,10} de 0 à 10
# {10} especificamente 10
# {5,10} de 5 à 10
# ()+ [a-zA-Z0-9]+

import re

texto = '''
    João trouxe flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

    Foi um ano excelente na vida de João. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijos nas tardes de pão de queijo.
    Não canso de ouvir a Maria:
    "joooooooooãooooooo. o café está prontinho aqui. Veeemm veeem veem vem"!
Jã
'''

print(re.findall(r'j[o]+ão', texto, flags=re.I))
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
print(re.sub(r'jo{1,}ão{1}', 'Felipe', texto, flags=re.I))

texto2 = 'joão ama ser amado'
print(re.findall(r'ama[do]*', texto2, flags=re.I))
# [do] ou [od] -> não precisa estar na ordem
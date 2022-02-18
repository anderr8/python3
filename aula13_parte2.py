# Validando Senhas Fortes

# https://regex101.com/r/CH1vOd/1

# https://en.wikipedia.org/wiki/List_of_Unicode_characters

import re

senha_forte_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.MULTILINE
)

string = '''
VÁLIDAS
7}4NJb]u5X|z
76>L_X/1hFpd
J"6.lc1B7j:Y
jvS@G:522U>j
OK}8:dpr1P5%

SEM MINÚSCULAS
)7?VX)2C;15S
S<5F8~_=L5X2
>MA37|=1D1A|
(0*:7Z^6IQ0I
!MX{(4QE=339

SEM MINÚSCULAS E NÚMEROS
\G=Y[MZM]V.{
OUJQ]R&<F@[>
M[MOII"K}>"]
N]| QGG~`W:V
R]C<\A(MQF^%

SEM NÚMEROS, CARACTERES E MINÚSCULAS
ETTHJSTIQWAJ
CNGRFEQFUSUY
NOAHIHEXWDPK
ODBJBFOYBXWB
ZXKOWSQFRSIE

QUANTIDADE INVÁLIDA! (6)
0<omX8
8b4uX~
8gN1y|
5&9jmN
Wc52-t
'''

print(senha_forte_regexp.findall(string))

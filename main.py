
red = '\033[0;31;1m'
green = '\033[0;32;1m'
yellow = '\033[0;33;1m'
magenta = '\033[0;35;1m'
cyan = '\033[0;36;1m'

default = '\033[0m'

print(' '+red+'    _    ____   ____ ___ ___  '+yellow+' ____   '+magenta+'  ____           _ _ _ _  ')    
print(' '+red+'   / \  / ___| / ___|_ _|_ _| '+yellow+'|___ \  '+magenta+' / ___|   _ _ __(_) | (_) ___ ')
print(" "+red+"  / _ \ \___ \| |    | | | |  "+yellow+"  __) | "+magenta+"| |  | | | | '__| | | | |/ __|")
print(' '+red+' / ___ \ ___) | |___ | | | |  '+yellow+' / __/  '+magenta+'| |__| |_| | |  | | | | | (__ ')
print(' '+red+'/_/   \_\____/ \____|___|___| '+yellow+'|_____| '+magenta+' \____\__, |_|  |_|_|_|_|\___|')
print('                                        '+magenta+'     |___/                   ')
print('\033[0;34m          Created by \033[0;35m@0xCoto\033[1;34m - https://github.com/0xCoto/')
print(default+'             '+red+'Exploiting the Punycode Vulnerability...')
print(default)

a = 'а'
b = 'ь'
c = 'с'
d = 'd'
e = 'е'
f = 'f' #ENG
g = 'g' #ENG
h = 'Н'
i = 'І'
j = 'Ј'
k = 'к'
#K = 'К' #UPPERCASE (Alt.)
l = 'ӏ'
m = 'м'
#M = 'М' #UPPERCASE (Alt.)
n = 'и'
o = 'о'
p = 'р'
q = 'ԛ'
r = 'г'
s = 'ѕ'
t = 'т'
u = 'u' #ENG
v = 'v' #ENG
w = 'ԝ'
x = 'х'
y = 'у'
z = 'z' #ENG


try:
    ascii = str(input(cyan+'String to convert to Cyrillic (Case-Insensitive & no symbols): '+green))
    ascii = ascii.lower()
    
    print(default),
    
    print(yellow+'*'+red+' ASCII:                 '+cyan+ascii)
    print(yellow+'*'+magenta+' Unicode (Cyrillic):    '+cyan, end = '')
    
    I = 0
    while I < len(ascii):
        print((ascii.replace(ascii[I], eval(ascii[I]))[I]), end = '')
        I += 1
    
    print(default+'\n')
    
    if ('f' in ascii) or ('g' in ascii) or ('u' in ascii) or ('v' in ascii) or ('z' in ascii):
        print(yellow+'Note: Some characters were not replaced by Cyrillic ones due to their obvious visual difference.'+default+'\n')

except:
    print('\n\n'+red+'Error: Please use characters from the English Alphabet (ASCII) only.'+default+'\n')

#hello.py

'''
Mehrzeilige Kommentare mit 3 '
'''

#Einzeilige Kommentare mit #
#Kein Untershied zwischen ' und "

'''
Python Keywords
False None True
and as assert async await break class continue
def del elif else except finally for from
global if import in is lambda nonlocal not
or pass raise return try while with yield
help() -> keywords
import keyword
print(keyword.kwlist)
print(keyword.softkwlist)
'''


a = 24
b = 43.22
c = 2 + 43
d = "Hello"
e = True
f = None

print(a, b, c, d, e, f)
print(type(a), type(b), type(c), type(d), type(e), type(f))

a = float(a)
b = complex(24, 52)
c = int(-4.11)
d = str(e)
e = bool("Hello")
f = bool()
g = bool("False")

print(a, b, c, d, e, f, g)
variable = 2
#print(variable)
boolVar = True
stringVar = 'napis'
floatVar = 2.15
integerVar = 5
NoneVar = None
print("Nasze zmienne to: {}, {}, {}, {}, {}") \
.format(type(boolVar), \
        type(stringVar), \
        type(floatVar), \
        type(integerVar+integerVar), \
        type(NoneVar))
#type()
zmienna = 2.0 + 5
print(type(zmienna))


if 2+2 < 4:
    print("warunek jest spelniony")
elif 2+2 > 4:
    print("drugi warunek jest spelniony")
else:
    print("zaden z warunkow niespelniony")
    
def setup():
    line(30, 20, 15, 12)

    
def draw():
    print(integerVar)
    print(mousePressed)  
    clear()

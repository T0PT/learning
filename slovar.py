def show(*args,**kwargs):
    for i in args:
        if i<1: print(i)
    for i in kwargs.keys():
        if i[0]!='M': print(kwargs[i])
show(0.15, 764, 63,
     1321, 57.7, 0.05,
     Mars=0.15,
     Saturn=764,
     Uranus=63,
     Jupiter=1321,
     Neptune=57.7,
     Mercury=0.05)




planets = {'Jupiter': 1321, 'Mars': 0.15, 'Saturn': 764}
planets.update(Mercury=0.05,Venus=0.86,Neptune=57.7, Earth=1)
x=input('enter planet ')
print(planets.get(x,'Вы что, ввели Плутон? Плутон – это не планета!'))



planets = ['Jupiter', 1321, 'Mars', 0.15, 'Saturn', 764]
solarsys={planets[i]:planets[i+1] for i in range(0,len(planets)-1, 2)}
print(solarsys)
planets2 = {1321: 'Jupiter', 0.15: 'Mars', 764: 'Saturn'}
planets3={}
for key,val in planets2.items():
    planets3[val]=key
print(planets3)



solsystem={'Jupiter':1321,'Mars':0.15,'Saturn':764,'Uranus':63,'Mercury':0.056, 'Venus':0.86, 'Neptune':57.7,'Pluto':0.059,'Earth':1}
solsystem.pop('Pluto')
for key in solsystem.keys():
    if solsystem[key]>1:
        print(key)
for key in solsystem.keys():
    if key[0]=='M':
        print(solsystem[key])

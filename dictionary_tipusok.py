# ez egy üres dictionary:
my_dict = {}

# olyan lista, amiben több elem lehet,
# és ahol az elemek nem csak index-szel
# hanem labellel (címkével) is el vannak látva

my_dict['my_key'] = 43
print(my_dict)

my_dict = {'pista': '123-123-123', 'kati': '345-345-345'}
print(my_dict['pista'])

my_dict = {'people': ['pista', 'geza', 'tibi'],
           'x': {'a': 'value of a', 'b': [1, 2, 3]}}

print(my_dict['x']['b'][0])
print(my_dict['people'][1])
print(my_dict["people"][1])
print(type(my_dict))

# print(my_dict{'people'}) << ERROR!

# a get metódus szintén key alapján value-t ad vissza
print(my_dict.get('people')[0])

# a kettőspont bal oldalán van a key, a jobb oldalán a value
my_dict = {'myKey': 'value'}

print(my_dict.get('asd'))  # <<< None-t ad, ha nem létezik
# print(my_dict['asdasd']) <<< ERROR, ha nem létezik


# ha nem létezik az adott key, akkor létrehozza a
# key-t és a value-t
# ha létezne már ez a key, akkor új értéket kapna
my_dict['myNewKey'] = True
print(my_dict)

my_dict.pop('myNewKey')
print(my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# a dictionary key-eit adja vissza
print(my_dict.keys())
# a keyekhez tartozó értékeket adja vissza
print(my_dict.values())
# ez tuple-öket ad vissza, páronként a keyt és a value-t
print(my_dict.items())

# copy: másolatot csinál a dictionary-ről
# mert iteráció közben nem módosíthatjuk
# annak a dictionary-nek az elemeit
# amin végig loop-olunk
for key, value in my_dict.copy().items():
    if value == 3:
        my_dict.pop(key)

print(my_dict)

# dictionary egybe olvasztása
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_dict2 = {'e': 1, 'f': 2, 'c': 6, 'g': 4}

my_dict.update(my_dict2)
print(my_dict)

# a key az egyedi, csak egy lehet belőle
my_dict['e'] = 3

# dictionary készítés listákból
l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]
my_dict = dict(zip(l1, l2))
print(my_dict)

l3 = [('a', 1), ('b', 2)]
print(dict(l3))

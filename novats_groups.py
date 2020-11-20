import random
i = 0
group = 1
novat = ['Oriol Castellano Aguilera', 'Ian Perez Medina', 'Pol Besalú', 'Pol Segura', 'Laia Alcalà', 'Zak Soul', 'Ariadna Abad', 'Júlia Roure', 'Mariona Moll', 'Claudia Gil', 'Mireia Torrent', 'Oriol Vergés', 'Janina Estañol ', 'Eva Martín López', 'Ariadna Saez', 'Khaled elgizawi', 'Pablo Alfaro', 'Eric Ribera Martínez', 'Marta Meroño ', 'Iria Espinosa', 'marina fuster', 'Clàudia Valverde', 'Yaiza Serrano', 'Albert Garcia', 'Lluis Gimenez', 'Roger Bosch Unamuno', 'Alba Jimenez', 'Gerard Deuner', 'Pablo Pérez Cano', 'Joaquín Nogales', 'Pol Xavier Pérez Rodríguez', 'Afra Buch', 'David Muiña', 'Cristina Artero Martínez ']
print("lenght list {}".format(len(novat)))
while i < 34:
    a = random.choice(novat)
    novat.remove(a)
    b = random.choice(novat)
    novat.remove(b)
    c = random.choice(novat)
    novat.remove(c)
    d = random.choice(novat)
    novat.remove(d)
    print("---------------Grup {}\n{}\t{}\t{}\t{}".format(group, a, b, c, d))
    group += 1
    i += 4


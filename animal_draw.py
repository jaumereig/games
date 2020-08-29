import random
i = 0
animals = ['Jirafa', 'Leon', 'Hipopotamo', 'Orca', 'E. coli', 'Tiburon blanco', 'Perezoso', 'Rana ojos verdes']
while i < 8:
    a = random.choice(animals)
    animals.remove(a)
    b = random.choice(animals)
    animals.remove(b)
    #print("---\n{}\n\t-vs-\n{}".format(a, b))
    print("---\n{}\n{}".format(a, b))
    i += 2

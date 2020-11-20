import random
i = 0
group = 1
novat = ['Saez', 'Abad', 'Ian', 'Meroño', 'Alcala', 'Yaiza', 'Marina', 'Eva']
while i < 8:
    a = random.choice(novat)
    novat.remove(a)
    b = random.choice(novat)
    novat.remove(b)
    c = random.choice(novat)
    novat.remove(c)
    #print("---\n{}\n\t-vs-\n{}".format(a, b))
    print("---------------\nGrup {}\n{}\t{}\t{}\n".format(group, a, b, c))
    group += 1
    i += 3

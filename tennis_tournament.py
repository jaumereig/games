import random
print("USAGE:\n1st) Choose a draw:\nGrandSlam\nM1000\nATP500\nATP250\nPersonalized\n2nd) A list of ranking numbers is displayed in correct order simulating a real draw.")
print("Choose a draw: ")
draw = input()
#draw = 'ATP250'
follow = 0
while follow == False:
    if draw == 'ATP250' or draw == 'ATP500' or draw == 'M1000' or draw == 'GrandSlam' or draw == 'Personalized':
        follow = True
    else:
        print('***INPUT ERROR***\nMake sure to write the type of draw as it is stated.')
        draw = input()
follow = False
if draw == 'ATP250':
    print("Draw of 32 players:")
    l_seeds = []
    while len(l_seeds) < 8:
        seeds = random.randint(5, 45)
        if seeds not in l_seeds:
            l_seeds.append(seeds)
    #print(len(l_seeds), sorted(l_seeds))
    l_seeds = sorted(l_seeds)

    allplayers = []
    while len(allplayers) < 16:
        players = random.randint(46, 99)
        if players not in allplayers:
            allplayers.append(players)

    #print(len(allplayers), sorted(allplayers))
    allplayers = sorted(allplayers)

    qualyplayers = []
    while len(qualyplayers) < 4:
        qplayers = random.randint(100, 199)
        if qplayers not in qualyplayers:
            qualyplayers.append(qplayers)
    #print(len(qualyplayers), sorted(qualyplayers))
    qualyplayers = sorted(qualyplayers)
    # FIRST 8
    print('Seed #1: {}\nw.o'.format(l_seeds[0]))
    print('Q {}\n{}'.format(qualyplayers[3], allplayers[15]))
    print('{}\n{}'.format(allplayers[7], allplayers[11]))
    print('{}\nSeed #8: {}'.format(allplayers[6], l_seeds[7]))
    #............................................................
    # SECOND 8
    print('Seed #5: {}\nQ {}'.format(l_seeds[4], qualyplayers[2] ))
    print('{}\n{}'.format(allplayers[10], allplayers[0]))
    print('{}\n{}'.format(allplayers[5], allplayers[2]))
    print('w.o.\nSeed #3: {}'.format(l_seeds[2]))
    #............................................................
    # THIRD 8
    print('Seed #4: {}\nw.o'.format(l_seeds[3]))
    print('{}\n{}'.format(allplayers[13], allplayers[4]))
    print('{}\n{}'.format(allplayers[9], allplayers[1]))
    print('Q {}\nSeed #6: {}'.format(qualyplayers[1], l_seeds[5]))
    #............................................................
    # FOURTH 8
    print('Seed #7: {}\n{}'.format(l_seeds[6], allplayers[3]))
    print('{}\n{}'.format(allplayers[8], allplayers[12]))
    print('Q {}\n{}'.format(qualyplayers[0], allplayers[14]))
    print('w.o.\nSeed #2: {}'.format(l_seeds[1]))

elif draw == 'ATP500':
    print("ATP500 can either have a draw of size 32 or size 64. Choose one.")
    size_draw = input()
    while follow == False:
        if size_draw == '32' or size_draw == '64':
            follow = True
        else:
            print("***INPUT ERROR***\nInput should be an integer. Options 32 and 64.")
            size_draw = input()
    if size_draw == '32' and follow:
            print("Draw of 32 players:")
            l_seeds = []
            while len(l_seeds) < 8:
                seeds = random.randint(1, 32)
                if seeds not in l_seeds:
                    l_seeds.append(seeds)
            #print(len(l_seeds), sorted(l_seeds))
            l_seeds = sorted(l_seeds)

            allplayers = []
            while len(allplayers) < 18:
                players = random.randint(33, 90)
                if players not in allplayers:
                    allplayers.append(players)

            #print(len(allplayers), sorted(allplayers))
            allplayers = sorted(allplayers)

            qualyplayers = []
            while len(qualyplayers) < 2:
                qplayers = random.randint(91, 150)
                if qplayers not in qualyplayers:
                    qualyplayers.append(qplayers)
            #print(len(qualyplayers), sorted(qualyplayers))
            qualyplayers = sorted(qualyplayers)
            # FIRST 8
            print('Seed #1: {}\nw.o'.format(l_seeds[0]))
            print('Q {}\n{}'.format(qualyplayers[1], allplayers[17]))
            print('{}\n{}'.format(allplayers[7], allplayers[11]))
            print('{}\nSeed #8: {}'.format(allplayers[6], l_seeds[7]))
            #............................................................
            # SECOND 8
            print('Seed #5: {}\n{}'.format(l_seeds[4], allplayers[15] ))
            print('{}\n{}'.format(allplayers[10], allplayers[0]))
            print('{}\n{}'.format(allplayers[5], allplayers[2]))
            print('w.o.\nSeed #3: {}'.format(l_seeds[2]))
            #............................................................
            # THIRD 8
            print('Seed #4: {}\nw.o'.format(l_seeds[3]))
            print('{}\n{}'.format(allplayers[13], allplayers[4]))
            print('{}\n{}'.format(allplayers[9], allplayers[1]))
            print('{}\nSeed #6: {}'.format(allplayers[14], l_seeds[5]))
            #............................................................
            # FOURTH 8
            print('Seed #7: {}\n{}'.format(l_seeds[6], allplayers[3]))
            print('{}\n{}'.format(allplayers[8], allplayers[12]))
            print('Q {}\n{}'.format(qualyplayers[0], allplayers[16]))
            print('w.o.\nSeed #2: {}'.format(l_seeds[1]))
    elif size_draw == '64' and follow:
            print("Draw of 64 players:")
            l_seeds = []
            while len(l_seeds) < 16:
                seeds = random.randint(1, 40)
                if seeds not in l_seeds:
                    l_seeds.append(seeds)
            #print(len(l_seeds), sorted(l_seeds))
            l_seeds = sorted(l_seeds)

            allplayers = []
            while len(allplayers) < 27:
                players = random.randint(41, 80)
                if players not in allplayers:
                    allplayers.append(players)

            #print(len(allplayers), sorted(allplayers))
            allplayers = sorted(allplayers)

            qualyplayers = []
            while len(qualyplayers) < 5:
                qplayers = random.randint(81, 150)
                if qplayers not in qualyplayers:
                    qualyplayers.append(qplayers)
            #print(len(qualyplayers), sorted(qualyplayers))
            qualyplayers = sorted(qualyplayers)
            # FIRST 8
            print('Seed #1: {}\nw.o'.format(l_seeds[0]))
            print('{}\n{}'.format(allplayers[26], allplayers[13]))
            print('{}\n{}'.format(allplayers[16], allplayers[8]))
            print('w.o.\nSeed #15: {}'.format(l_seeds[14]))
            #............................................................
            # SECOND 8
            print('Seed #10: {}\nw.o'.format(l_seeds[9]))
            print('Q {}\n{}'.format(qualyplayers[4], allplayers[1]))
            print('{}\n{}'.format(allplayers[3], allplayers[6]))
            print('w.o.\nSeed #5: {}'.format(l_seeds[4]))
            #............................................................
            # THIRD 8
            print('Seed #3: {}\nw.o'.format(l_seeds[2]))
            print('{}\n{}'.format(allplayers[23], allplayers[15]))
            print('Q {}\n{}'.format(qualyplayers[3], allplayers[25]))
            print('w.o.\nSeed #14: {}'.format(l_seeds[13]))
            #............................................................
            #  FOURTH 8
            print('Seed #12: {}\nw.o'.format(l_seeds[11]))
            print('{}\n{}'.format(allplayers[10], allplayers[5]))
            print('{}\n{}'.format(allplayers[12], allplayers[24]))
            print('w.o.\nSeed #6: {}'.format(l_seeds[5]))
            #............................................................
            #  FIFTH 8
            print('Seed #8: {}\nw.o'.format(l_seeds[7]))
            print('Q {}\n{}'.format(qualyplayers[2], allplayers[2]))
            print('{}\n{}'.format(allplayers[4], allplayers[21]))
            print('w.o.\nSeed #9: {}'.format(l_seeds[8]))
            #............................................................
            #  SIXTH 8
            print('Seed #16: {}\nw.o'.format(l_seeds[15]))
            print('{}\n{}'.format(allplayers[0], allplayers[9]))
            print('{}\n{}'.format(allplayers[7], allplayers[22]))
            print('w.o.\nSeed #4: {}'.format(l_seeds[3]))
            #............................................................
            #  SEVENTH 8
            print('Seed #7: {}\nw.o'.format(l_seeds[6]))
            print('Q {}\n{}'.format(qualyplayers[1], allplayers[20]))
            print('{}\n{}'.format(allplayers[11], allplayers[19]))
            print('w.o.\nSeed #11: {}'.format(l_seeds[10]))
            #............................................................
            #  EIGTH 8
            print('Seed #13: {}\nw.o'.format(l_seeds[12]))
            print('{}\n{}'.format(allplayers[14], allplayers[18]))
            print('Q {}\n{}'.format(qualyplayers[0], allplayers[17]))
            print('w.o.\nSeed #2: {}'.format(l_seeds[1]))

elif draw == 'M1000':
    print("Draw of 128 players:")
    l_seeds = []
    while len(l_seeds) < 32:
        seeds = random.randint(1, 40)
        if seeds not in l_seeds:
            l_seeds.append(seeds)
    print(len(l_seeds), sorted(l_seeds))
    l_seeds = sorted(l_seeds)
    allplayers = []
    while len(allplayers) < 52:
        players = random.randint(41, 110)
        if players not in allplayers:
            allplayers.append(players)
    #print(len(allplayers), sorted(allplayers))
    allplayers = sorted(allplayers)
    qualyplayers = []
    while len(qualyplayers) < 12:
        qplayers = random.randint(111, 199)
        if qplayers not in qualyplayers:
            qualyplayers.append(qplayers)
    #print(len(qualyplayers), sorted(qualyplayers))
    qualyplayers = sorted(qualyplayers)

elif draw == 'GrandSlam':
    print("Draw of 128 players:")
    l_seeds = []
    while len(l_seeds) < 32:
        seeds = random.randint(1, 32)
        if seeds not in l_seeds:
            l_seeds.append(seeds)
    #print(len(l_seeds), sorted(l_seeds))
    l_seeds = sorted(l_seeds)

    allplayers = []
    while len(allplayers) < 72:
        players = random.randint(33, 105)
        if players not in allplayers:
            allplayers.append(players)

    #print(len(allplayers), sorted(allplayers))
    allplayers = sorted(allplayers)

    qualyplayers = []
    while len(qualyplayers) < 24:
        qplayers = random.randint(106, 250)
        if qplayers not in qualyplayers:
            qualyplayers.append(qplayers)
    #print(len(qualyplayers), sorted(qualyplayers))
    qualyplayers = sorted(qualyplayers)
    # FIRST 8
    print('Seed #1: {}\nQ {}'.format(l_seeds[0], qualyplayers[20]))
    print('{}\n{}'.format(allplayers[26], allplayers[13]))
    print('{}\n{}'.format(allplayers[66], allplayers[18]))
    print('{}\nSeed #27: {}'.format(allplayers[65],l_seeds[26]))
    #............................................................
    # SECOND 8    
    print('Seed #16: {}\n{}'.format(l_seeds[15], allplayers[40]))
    print('Q {}\n{}'.format(qualyplayers[2], allplayers[55]))
    print('{}\n{}'.format(allplayers[36], allplayers[63]))
    print('Q {}\nSeed #13: {}'.format(qualyplayers[19], l_seeds[12]))
    #............................................................
    # THIRD 8
    
elif draw == 'Personalized':
    print("What type of draw? Options:\nReversed ranking\tTop 8 players\tTop 20 players\tTop against bottom")
    type_of_draw = input()
    follow = False
    while follow == False:
        if type_of_draw == 'Reversed ranking' or type_of_draw == 'Top 8 players' or type_of_draw == 'Top 20 players' or type_of_draw == 'Top against bottom':
            follow = True
        else:
                print("***INPUT ERROR***\nOptions:\nReversed ranking\tTop 8 players\tTop 20 players\tTop against bottom")
                type_of_draw = input()
    if type_of_draw == 'Reversed ranking' and follow:
        l_seeds = []
        while len(l_seeds) < 8:
            seeds = random.randint(85, 100)
            if seeds not in l_seeds:
                l_seeds.append(seeds)
        #print(len(l_seeds), sorted(l_seeds))
        l_seeds = sorted(l_seeds,reverse = 1)
        allplayers = []
        while len(allplayers) < 16:
            players = random.randint(11, 84)
            if players not in allplayers:
                allplayers.append(players)
        #print(len(allplayers), sorted(allplayers))
        allplayers = sorted(allplayers, reverse= 1)
        qualyplayers = []
        while len(qualyplayers) < 4:
            qplayers = random.randint(1, 10)
            if qplayers not in qualyplayers:
                qualyplayers.append(qplayers)
        #print(len(qualyplayers), sorted(qualyplayers))
        qualyplayers = sorted(qualyplayers, reverse= 1)
        # FIRST 8
        print('Seed #1: {}\nw.o'.format(l_seeds[0]))
        print('Q {}\n{}'.format(qualyplayers[3], allplayers[15]))
        print('{}\n{}'.format(allplayers[7], allplayers[11]))
        print('{}\nSeed #8: {}'.format(allplayers[6], l_seeds[7]))
        #............................................................
        # SECOND 8
        print('Seed #5: {}\nQ {}'.format(l_seeds[4], qualyplayers[2] ))
        print('{}\n{}'.format(allplayers[10], allplayers[0]))
        print('{}\n{}'.format(allplayers[5], allplayers[2]))
        print('w.o.\nSeed #3: {}'.format(l_seeds[2]))
        #............................................................
        # THIRD 8
        print('Seed #4: {}\nw.o'.format(l_seeds[3]))
        print('{}\n{}'.format(allplayers[13], allplayers[4]))
        print('{}\n{}'.format(allplayers[9], allplayers[1]))
        print('Q {}\nSeed #6: {}'.format(qualyplayers[1], l_seeds[5]))
        #............................................................
        # FOURTH 8
        print('Seed #7: {}\n{}'.format(l_seeds[6], allplayers[3]))
        print('{}\n{}'.format(allplayers[8], allplayers[12]))
        print('Q {}\n{}'.format(qualyplayers[0], allplayers[14]))
        print('w.o.\nSeed #2: {}'.format(l_seeds[1]))
        print(l_seeds, qualyplayers)

    elif type_of_draw == 'Top 8 players' and follow:
        l_seeds = [1,2,3,4,5,6,7,8]
        while len(l_seeds) > 0:
            out = random.choice(l_seeds)
            print(out)
            l_seeds.remove(out)
    
    elif type_of_draw == 'Top 20 players' and follow:
        l_seeds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        while len(l_seeds) > 0:
            out = random.choice(l_seeds)
            print(out)
            l_seeds.remove(out)
    
    elif type_of_draw == 'Top against bottom' and follow:
        l_seeds = [1,2,3,4,5,6,7,8, 9, 10]
        l_bottom = [91,92,93,94,95,96,97,98,99,100]
        while len(l_seeds) > 0 and len(l_bottom) > 0:
            s_out = random.choice(l_seeds)
            b_out = random.choice(l_bottom)
            print("{} vs. {}\n".format(s_out, b_out))
            l_seeds.remove(s_out)
            l_bottom.remove(b_out)
import random
tyson_w = 8
tyson_p = 11.69
tyson = [tyson_w, tyson_p]

daniel_w = 6
daniel_p = 14.21
daniel = [daniel_w, daniel_p]

adam_w = 5
adam_p = 7.91
adam = [adam_w, adam_p]

nick_w = 5.5
nick_p = 12.14
nick = [nick_w, nick_p]

griffin_w = 4.5
griffin_p = 6.51
griffin = [griffin_w, griffin_p]

alex_w = 7
alex_p = 12.55
alex = [alex_w, alex_p]

gelliot_w = 6
gelliot_p = 13.56
gelliot = [gelliot_w, gelliot_p]

bodie_w = 4
bodie_p = 7.09
bodie = [bodie_w, bodie_p]

joey_w = 2
joey_p = 7.3
joey = [joey_w, joey_p]

jonah_w = 2
jonah_p = 7.08
jonah = [jonah_w, jonah_p]

for i in range(10):
    import random

    tyson_w = 8
    tyson_p = 11.69
    tyson = [tyson_w, tyson_p]

    daniel_w = 6
    daniel_p = 14.21
    daniel = [daniel_w, daniel_p]

    adam_w = 5
    adam_p = 7.91
    adam = [adam_w, adam_p]

    nick_w = 5.5
    nick_p = 12.14
    nick = [nick_w, nick_p]

    griffin_w = 4.5
    griffin_p = 6.51
    griffin = [griffin_w, griffin_p]

    alex_w = 7
    alex_p = 12.55
    alex = [alex_w, alex_p]

    gelliot_w = 6
    gelliot_p = 13.56
    gelliot = [gelliot_w, gelliot_p]

    bodie_w = 4
    bodie_p = 7.09
    bodie = [bodie_w, bodie_p]

    joey_w = 2
    joey_p = 7.3
    joey = [joey_w, joey_p]

    jonah_w = 2
    jonah_p = 7.08
    jonah = [jonah_w, jonah_p]

    # Week 11
    def prediction(f, u):
        winner_odds = (f[1]/(u[1] + f[1])) * 100
        winner = random.randrange(100000) / 1000
        if winner < winner_odds:
            f[0] += 1
        elif winner > winner_odds:
            u[0] += 1
        else:
            f[0] += .5
            u[0] += .5
    # Week 11
    f = daniel
    u = jonah
    prediction(f, u)

    f = alex
    u = nick
    prediction(f, u)

    f = tyson
    u = griffin
    prediction(f, u)

    f = joey
    u = bodie
    prediction(f, u)

    f = gelliot
    u = adam
    prediction(f, u)

    # Week 12
    f = tyson
    u = jonah
    prediction(f, u)

    f = nick
    u = joey
    prediction(f, u)

    f = alex
    u = adam
    prediction(f, u)

    f = daniel
    u = bodie
    prediction(f, u)

    f = gelliot
    u = griffin
    prediction(f, u)

    # Week 13
    f = bodie
    u = jonah
    prediction(f, u)

    f = adam
    u = joey
    prediction(f, u)

    f = gelliot
    u = tyson
    prediction(f, u)

    f = daniel
    u = nick
    prediction(f, u)

    f = alex
    u = griffin
    prediction(f, u)


    print(tyson[0])
    print(jonah[0])
    print(daniel[0])
    print(adam[0])
    print(nick[0])
    print(gelliot[0])
    print(griffin[0])
    print(joey[0])
    print(bodie[0])
    print(alex[0])
    print()

'''
    favorite = daniel
    underdog = jonah
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = alex
    underdog = nick
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = tyson
    underdog = griffin
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = joey
    underdog = bodie
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = gelliot
    underdog = adam
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

        # Week 12

    favorite = tyson
    underdog = jonah
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = nick
    underdog = joey
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = alex
    underdog = adam
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = daniel
    underdog = bodie
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = gelliot
    underdog = griffin
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    # Week 13

    favorite = bodie
    underdog = jonah
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = adam
    underdog = joey
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = gelliot
    underdog = tyson
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5

    favorite = daniel
    underdog = nick
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5
    print(favorite[0], underdog[0])

    favorite = alex
    underdog = griffin
    winner_odds = (favorite[1] / (underdog[1] + favorite[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        favorite[0] += 1
    elif winner > winner_odds:
        underdog[0] += 1
    else:
        favorite[0] += .5
        underdog[0] += .5
    print(favorite[0], underdog[0])

'''


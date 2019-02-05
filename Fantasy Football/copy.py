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

for i in range(1):

    # Week 11
    '''
    def prediction(f_0, u_0, f_1, u_1):
        winner_odds = (f_1/(u_1 + f_1)) * 100
        winner = random.randrange(100000) / 1000
        if winner < winner_odds:
            f_0 += 1
        elif winner > winner_odds:
            u_0 += 1
        else:
            f_0 += .5
            u_0 += .5
        return f_0, u_0
    print(prediction(daniel[0], jonah[0], daniel[1], jonah[1]))
    '''


    favorite = daniel
    underdog = jonah
    winner_odds = (daniel[1] / (jonah[1] + daniel[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        daniel[0] += 1
    elif winner > winner_odds:
        jonah[0] += 1
    else:
        daniel[0] += .5
        jonah[0] += .5

    favorite = alex
    underdog = nick
    winner_odds = (alex[1] / (nick[1] + alex[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        alex[0] += 1
    elif winner > winner_odds:
        nick[0] += 1
    else:
        alex[0] += .5
        nick[0] += .5

    favorite = tyson
    underdog = griffin
    winner_odds = (tyson[1] / (griffin[1] + tyson[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        tyson[0] += 1
    elif winner > winner_odds:
        griffin[0] += 1
    else:
        tyson[0] += .5
        griffin[0] += .5

    favorite = joey
    underdog = bodie
    winner_odds = (joey[1] / (bodie[1] + joey[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        joey[0] += 1
    elif winner > winner_odds:
        bodie[0] += 1
    else:
        joey[0] += .5
        bodie[0] += .5

    favorite = gelliot
    underdog = adam
    winner_odds = (gelliot[1] / (adam[1] + gelliot[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        gelliot[0] += 1
    elif winner > winner_odds:
        adam[0] += 1
    else:
        gelliot[0] += .5
        adam[0] += .5

        # Week 12

    favorite = tyson
    underdog = jonah
    winner_odds = (tyson[1] / (jonah[1] + tyson[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        tyson[0] += 1
    elif winner > winner_odds:
        jonah[0] += 1
    else:
        tyson[0] += .5
        jonah[0] += .5

    favorite = nick
    underdog = joey
    winner_odds = (nick[1] / (joey[1] + nick[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        nick[0] += 1
    elif winner > winner_odds:
        joey[0] += 1
    else:
        nick[0] += .5
        joey[0] += .5

    favorite = alex
    underdog = adam
    winner_odds = (alex[1] / (adam[1] + alex[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        alex[0] += 1
    elif winner > winner_odds:
        adam[0] += 1
    else:
        alex[0] += .5
        adam[0] += .5

    favorite = daniel
    underdog = bodie
    winner_odds = (daniel[1] / (bodie[1] + daniel[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        daniel[0] += 1
    elif winner > winner_odds:
        bodie[0] += 1
    else:
        daniel[0] += .5
        bodie[0] += .5

    favorite = gelliot
    underdog = griffin
    winner_odds = (gelliot[1] / (griffin[1] + gelliot[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        gelliot[0] += 1
    elif winner > winner_odds:
        griffin[0] += 1
    else:
        gelliot[0] += .5
        griffin[0] += .5

    # Week 13

    favorite = bodie
    underdog = jonah
    winner_odds = (bodie[1] / (jonah[1] + bodie[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        bodie[0] += 1
    elif winner > winner_odds:
        jonah[0] += 1
    else:
        bodie[0] += .5
        jonah[0] += .5

    favorite = adam
    underdog = joey
    winner_odds = (adam[1] / (joey[1] + adam[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        adam[0] += 1
    elif winner > winner_odds:
        joey[0] += 1
    else:
        adam[0] += .5
        joey[0] += .5

    favorite = gelliot
    underdog = tyson
    winner_odds = (gelliot[1] / (tyson[1] + gelliot[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        gelliot[0] += 1
    elif winner > winner_odds:
        tyson[0] += 1
    else:
        gelliot[0] += .5
        tyson[0] += .5

    favorite = daniel
    underdog = nick
    winner_odds = (daniel[1] / (nick[1] + daniel[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        daniel[0] += 1
    elif winner > winner_odds:
        nick[0] += 1
    else:
        daniel[0] += .5
        nick[0] += .5

    favorite = alex
    underdog = griffin
    winner_odds = (alex[1] / (griffin[1] + alex[1])) * 100
    winner = random.randrange(100000) / 1000
    if winner < winner_odds:
        alex[0] += 1
    elif winner > winner_odds:
        griffin[0] += 1
    else:
        alex[0] += .5
        griffin[0] += .5
    griffin[0].append()

    print('Tyson:', tyson_w)
    print('Jonah:', jonah_w)
    print('Daniel:', daniel_w)
    print('Adam:', adam_w)
    print('Nick:', nick_w)
    print('Gelliot:', gelliot_w)
    print('Griffin:', griffin_w)
    print('Joey:', joey_w)
    print('Bodie:', bodie_w)
    print('Alex:', alex_w)

import random

def wt():
    x = random.randint(0,4)
    y = random.randint(0,1)
    z = random.randint(0,1)
    nac = ['США', 'Германия', 'СССР', 'Великобритания', 'Япония']
    teh = ['Танки', 'Самолёты']
    tip = [' (Аркада)', ' (Реалистичные)']
    if a != 4:
        otvet = nac[x] + ' - ' + teh[y]
    else:
        otvet = nac[x] + ' - Самолёты'
    otvet += tip[z]
    return(otvet)

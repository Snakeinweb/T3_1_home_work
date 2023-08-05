

print('Çäğàâñòâóéòå')

prif = 'ëåò'

who_animal = input('Êòî âàø ïèòîìåö? ')

name = input('Èìÿ âàøåãî ïèòîìöà? ')

age = int(input('Âîçğàñò âàøåãî ïèòîìöà? '))

# â äàëüíåéøåì ìîæíî îáğàáîòàòü äî äğóãèõ "ëåò"

if age == 1:

    prif = 'ãîä'

else:

    if age >= 2 and age <= 4:

        prif = 'ãîäà'

print('İòî',who_animal,'ïî êëè÷êå "'+name+'". Âîçğàñò:',age,prif)

# ration en prtéine pour 100g
viande_rouge = 20
viande_blanche = 20
poisson = 18
poisson_gras = 18
oeuf = 8
lait = 20

avoine =  13.5
pates = 11
quinoa = 13.8

# ration en protéine pour 30g
whey = 24.6




prot = [whey, avoine, viande_rouge * 2 , pates, quinoa, viande_blanche, whey]

def sum(list):
    sum = 0
    for food in list:
        sum += food

    print('rapport de protéine journalier : ', sum)
    print('Voilà ce que tu dois manger : ')
    for food in list:
        print(f'{food}g de {food}')

    return sum
        

sum(prot)
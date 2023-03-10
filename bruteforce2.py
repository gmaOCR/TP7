# rendements_list = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]
liste = [1, 2, 3, 4, 5]
k = 2**len(liste)
combinaison = 0
# j = 0
result = [[]]
while combinaison < k:
    j = 0
    tmpList = []
    for item in liste: # si I =7
        positionDansBinaire = 2**j
        valeurEtLogic = combinaison &  positionDansBinaire
        # print("J= "  + str(j) + " Pos= "  + str(positionDansBinaire) +" val = "  + str(valeurEtLogic))
        #si somme + item.valeur > 500 alors continue
        if valeurEtLogic > 0 :
            tmpList.append(item)
        j = j + 1
    if len(tmpList)>0:
        result.append(tmpList)
        print(tmpList)
    combinaison = combinaison + 1
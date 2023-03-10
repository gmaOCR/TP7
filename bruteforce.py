actions_list = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
rendements_list = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]


class Action:
    """Constructeur obj action"""

    def __init__(self, k_id, valeur, rendement):
        self.id = k_id
        self.valeur = valeur
        self.gain = valeur * rendement / 100


def create_action_list_obj(liste_actions, liste_rendements):
    """Creer des objets actions en fonction d'une liste de valeurs de rendements"""
    actions_obj_list = []
    i = 0
    for _ in liste_actions:
        actions_obj_list.append(Action(i + 1, liste_actions[i], liste_rendements[i]))
        i = i + 1
    return actions_obj_list


"""Creation de la liste des objets Action"""
actions_list_obj = create_action_list_obj(actions_list, rendements_list)
n = len(actions_list_obj)
test_l = []
value_list = []


# def test(combo):
#     if not combo:
#         print(combo)
#     else:
#         print(combo)
#         i = 0
#         for c in combo:
#             print(c[i].valeur)
#             i = i + 1

def combinations(n, iterable):
    if not n:
        return [[]]
    if not iterable:
        return []
    head = [iterable[0]]
    tail = iterable[1:]
    new_comb = [head + list_ for list_ in combinations(n - 1, tail)]
    return new_comb + combinations(n, tail)


comb = []
for n in range(1, len(actions_list_obj) + 1):
    comb.append(combinations(n, actions_list_obj))

    print(comb)



# for l in range()


# l = 0

# for i in range(n):
#     test_l.append(actions_list_obj[i].valeur)
#     for l in range(i):
#         test_l.append(tuple((actions_list_obj[i].valeur, actions_list_obj[l].valeur)))
# print(test_l)


# i = 0
# while i < n:
#     for j in range(i, n):
#         test_l.append(actions_list_obj[j-n].valeur)
#     i = i + 1
# print(test_l)

# def combinations(iterable, r):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = list(range(r))
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i + 1, r):
#             indices[j] = indices[j - 1] + 1
#         yield tuple(pool[i] for i in indices)
#
#
# da = combinations(value_list, 20)
# print(da.__next__())

#
#
# class ArbreBinaire:
#     def __init__(self, valeur):
#         self.valeur = valeur
#         self.enfant_gauche = None
#         self.enfant_droit = None
#
#     def insert_gauche(self, valeur):
#         if self.enfant_gauche is None:
#             self.enfant_gauche = ArbreBinaire(valeur)
#         else:
#             new_node = ArbreBinaire(valeur)
#             new_node.enfant_gauche = self.enfant_gauche
#             self.enfant_gauche = new_node
#
#     def insert_droit(self, valeur):
#         if self.enfant_droit is None:
#             self.enfant_droit = ArbreBinaire(valeur)
#         else:
#             new_node = ArbreBinaire(valeur)
#             new_node.enfant_droit = self.enfant_droit
#             self.enfant_droit = new_node
#
#     def get_valeur(self):
#         return self.valeur
#
#     def get_gauche(self):
#         return self.enfant_gauche
#
#     def get_droit(self):
#         return self.enfant_droit
#
#

# def arrangements_v1(p, n):
#     if p > n:
#         return
#
#     indices = list(range(p))  # on initialise la liste des indices [0,1,2,..,p-1]
#     yield tuple(indices)  # ordre pour générer le tuple
#
#     i = p - 1  # on part de la fin de la liste des indices
#     k = p  # variable utilisé pour incrémenter ou initialiser les indices
#
#     while i != -1:  # on parcourt les indices de la droite vers la gauche : p-1 -> 0
#         if k < n:  # si la valeur d'indice maxi n'a pas été dépassée
#             if k not in indices[:i]:  # si l'indice k n'est pas présent parmi les indices précédant indices[i]
#                 indices[i] = k  # on incrémente indices[i] avec la valeur de k
#                 k = 0;
#                 j = i + 1  # on met k à 0 pour ensuite initialiser les prochains indices : nouveau cycle (ex. : 0,1,2,..).
#                 while (j < p):  # on parcourt les prochains indices
#                     if k not in indices[
#                                 :i + 1]:  # si l'indice k n'est pas présent parmi les indices précédant indices[i+1]
#                         indices[j] = k  # on initialise indices[j] avec la valeur de k
#                         j += 1  # prochain indice
#                     k += 1
#                 yield tuple(indices)  # ordre pour générer le tuple
#                 i = p - 1  # on revient sur le dernier indice à incrémenter
#                 k = indices[i]
#             k += 1  # on incrémente k
#         else:  # sinon
#             i -= 1  # on remonte les indices vers la gauche
#             k = indices[i] + 1  # on met à jour k pour le prochain indice
#
#     return
#
# ab = arrangements_v1(value_list,20)
# print(ab)
# print(sum((actions_list_obj[0].valeur, actions_list_obj[2].valeur)))

# def n_length_combo(lst, n):
#     if n == 0:
#         return [[]]
#
#     l = []
#     for i in range(0, len(lst)):
#
#         m = lst[i]
#         remLst = lst[i + 1:]
#
#         remainlst_combo = n_length_combo(remLst, n - 1)
#         for p in remainlst_combo:
#             l.append([m, *p])
#
#     return l


# Driver code
# if __name__ == "__main__":
#     arr = "abc"
#     print(n_length_combo([x for x in arr], 2))
#
# v = n_length_combo(actions_list_obj, 20)
# print(v)

# i = 0
# for action in range(0, n):
#     m = actions_list_obj[i]
#     remlst = actions_list_obj[i + 1:]


# Exo
#
# class Arbre:
#     def __init__(self, racine = None):
#         self.racine = racine # type : Noeud
# class Noeud:
#     def __init__(self, v, g = None, d = None):
#         self.g = g # type Noeud
#         self.d = d # type Noeud
#         self.v = v
#
# ng, nd = Noeud(9), Noeud(4)
# ng, nd = Noeud(1, ng, nd), Noeud(12)
# nd = Noeud(6, ng, nd)
# ngd = Noeud(3)
# ng = Noeud(10, d = ngd)
# arbre = Arbre(Noeud(5, ng, nd))
#
# def hauteur(noeud):
#     if noeud is None:
#         return -1
#     else:
#         return 1 + max(hauteur(noeud.g), hauteur(noeud.d))
#
# print(hauteur(ng))
# print(hauteur(nd))

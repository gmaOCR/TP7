import itertools

class Action:
    def __init__(self, id, valeur, rendement):
        self.id = id
        self.valeur = valeur
        self.gain = valeur * rendement / 100

def create_action_obj_list(liste_actions, liste_rendements):
    """Créé un objet Action en prenant la liste de leurs montants de leur rendements.
    Garder la correspondance des index pour les 2 listes. Les 2 listes doivent avoir la même longueur

    Args:
        liste_actions (int_list): montant unitaire de chaque action sous forme de liste
        liste_rendements (int_list): rendement unitaire de chaque action sous forme de liste

    Returns:
        _type_: Renvoie une liste d'objet Action de longueur égale aux listes initiales
    """
    actions_obj_list = []
    for i in range(len(liste_actions)):
        actions_obj_list.append(Action(i + 1, liste_actions[i], liste_rendements[i]))
    return actions_obj_list

def list_all_combinations(action_obj_list):
    """Liste toutes les possibilités de combinaisons sans remises d'une liste d'action
    de portée N. Utilise itertools

    Args:
        action_obj_list (object_list): Liste d'objets Actions

    Returns:
        _type_: Renvoie une liste d'objets Action de toutes les combinaisons possibles
    """
    combinations = []
    for i in range(1, len(action_obj_list) + 1):
        for c in itertools.combinations(action_obj_list, i):
            combinations.append(list(c))
    return combinations

def filter_combinations_by_value(combination_list, max_value):
    """Filtre une liste de combinaisons d'objets suivant une valeur maximale définie

    Args:
        combination_list (object_list): Liste d'objets Action
        max_value (int): _description_

    Returns:
        _type_: _description_
    """
    filtered_combinations = []
    for c in combination_list:
        if sum(action.valeur for action in c) <= max_value:
            filtered_combinations.append(c)
    return filtered_combinations

actions_list = [20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]
rendements_list = [5, 10, 15, 20, 17, 25, 7, 11, 13, 27, 17, 9, 23, 1, 3, 8, 12, 14, 21, 18]

# Création de la liste d'objets Action à partir des listes d'entiers
action_obj_list = create_action_obj_list(actions_list, rendements_list)

# Liste toutes les combinaisons possibles de 20 actions maximum sans remises
all_combinations = list_all_combinations(action_obj_list)[:1048576] # limite de combinaisons fixées à 2^20

# Filtrage des combinaisons en ne conservant que celles dont la somme des valeurs est inférieure ou égale à 500
filtered_combinations = filter_combinations_by_value(all_combinations, 500)

# Recherche de la combinaison la plus rentable
best_combination = None
best_profit = 0
for combination in filtered_combinations:
    current_profit = sum(action.gain for action in combination)
    if current_profit > best_profit:
        best_profit = current_profit
        best_combination = combination

# Affichage du nombre de combinaisons filtrées et de la combinaison la plus rentable
print("Nombre de combinaisons avec une somme des valeurs <= 500 :", len(filtered_combinations))
print("La combinaison la plus rentable est :", [(action.id, action.valeur) for action in best_combination], "avec un profit de", round(best_profit,2))

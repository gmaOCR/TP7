import csv

def read_csv(file_path):
    actions_id = []
    actions_values = []
    actions_returns = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader) # skip header row
        
        for row in reader:
            actions_id.append(row[0])
            actions_values.append(row[1])
            actions_returns.append(int(row[2].strip('%')))
    
    return actions_id, actions_values, actions_returns



class Action:
    def __init__(self, id, valeur, rendement):
        self.id = id
        self.valeur = int(valeur)
        self.gain = int(valeur) * rendement / 100


def create_action_obj_list(id_list,liste_actions, liste_rendements):
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
        actions_obj_list.append(Action(id_list[i], liste_actions[i], liste_rendements[i]))
    return actions_obj_list

def generate_combinations(action_list, r):
    """
    Génère toutes les combinaisons possibles de longueur r à partir de action_list.
    
    Args:
        action_list (list[Action]): Liste d'objets Action
        r (int): Longueur des combinaisons
        
    Returns:
        list[list[Action]]: Liste de toutes les combinaisons possibles de longueur r
    """
    if r == 0:
        return [[]]
        
    else:
        combinations = []
        for i in range(len(action_list)):
            current_action = action_list[i]
            remaining_actions = action_list[i+1:]
            for sub_combination in generate_combinations(remaining_actions, r-1):
                combinations.append([current_action] + sub_combination)
        return combinations

def list_all_combinations(action_obj_list):
    """Liste toutes les possibilités de combinaisons sans remises d'une liste d'action
    de portée N.

    Args:
        action_obj_list (object_list): Liste d'objets Actions

    Returns:
        _type_: Renvoie une liste d'objets Action de toutes les combinaisons possibles
    """
    all_combinations = []
    for r in range(1, len(action_obj_list) + 1):
        combinations = generate_combinations(action_obj_list, r)
        all_combinations.extend(combinations)
    return all_combinations

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

#Import depuis le CSV originel
actions_list = read_csv('actions.csv')

# Création de la liste d'objets Action à partir des listes d'entiers
action_obj_list = create_action_obj_list(actions_list[0],actions_list[1],actions_list[2])

# Liste toutes les combinaisons possibles de 20 actions maximum sans remises
all_combinations = list_all_combinations(action_obj_list)

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

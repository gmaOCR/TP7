import csv

class Action:
    def __init__(self, id, valeur, rendement):
        self.id = id
        self.valeur = float(valeur)
        self.gain = float(valeur) * rendement / 100 * 100 # Correction de facteur 100


def read_csv(file_path):
    """
    Lit un fichier CSV et retourne un tuple contenant une liste d'ID d'actions, de valeurs et
    de gains.
    
    Args:
        file_path (str): Chemin relatif du CSV.
        
    Returns:
        Tuple: Un tuple contenant 3 listes: actions_ids, actions_values, actions_returns.
    """

    actions_id = []
    actions_values = []
    actions_returns = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader) # skip header row

        for row in reader:
            value = float(row[1])
            if value > 0:
                actions_id.append(row[0])
                actions_values.append(row[1])
                actions_returns.append(float(row[2].strip('%')))
    
    result = (actions_id, actions_values, actions_returns)
    return result


def create_action_obj_list(id_list,liste_actions, liste_rendements):
    """Créé un objet Action en prenant la liste de leurs montants de leur rendements.
    Garder la correspondance des index pour les 2 listes. Les 2 listes doivent avoir la même longueur

    Args:
        id_list (str_list): Liste d'identifiants des actions
        liste_actions (int_list): Montant unitaire de chaque action sous forme de liste
        liste_rendements (float_list): Rendement unitaire de chaque action sous forme de liste

    Returns:
        _type_: Renvoie une liste d'objet Action de longueur égale aux listes initiales
    """
    actions_obj_list = []
    for i in range(len(liste_actions)):
        actions_obj_list.append(Action(id_list[i], liste_actions[i], liste_rendements[i]))
    return actions_obj_list

def find_best_combination(max_value, action_obj_list):
    """
    Trouve la meilleure combinaison d'actions qui maximise le gain total
    avec une contrainte en portefeuille max.

    Args:
        max_value (float): Budget max du portefeuille
        action_obj_list (list): Une liste d'objets Action.
    
    Returns:
        Tuple: Un tuple qui contient deux éléments: la liste d'objets Action optimale, 
        et le total des gains de la combinaison.
    """

    # Initialisation du tableau dynamique
    n = len(action_obj_list)
    gains_table = [[0]*(max_value*100+1) for _ in range(n+1)]

    # Remplissage de la table de programmation dynamique
    for i in range(1, n+1):
        for j in range(1, max_value*100+1):
            current_action = action_obj_list[i-1]
            if int(current_action.valeur * 100) > j:
                # L'achat de cette action est impossible car il n'y a plus assez d'argent pour ajouter une unité
                gains_table[i][j] = gains_table[i-1][j]
            else:
                # On compare le gain maximum obtenu en incluant l'action courante à celui obtenu sans elle
                previous_gains = gains_table[i-1][j-int(current_action.valeur * 100)]
                new_gains = previous_gains + current_action.gain
                gains_table[i][j] = max(new_gains, gains_table[i-1][j])

    # Reconstruction de la meilleure combinaison
    best_combination = []
    j = max_value * 100
    for i in range(n, 0, -1):
        if gains_table[i][j] > gains_table[i-1][j]:
            best_combination.append(action_obj_list[i-1])
            j -= int(action_obj_list[i-1].valeur * 100)

    best_combination = best_combination[::-1]
    total_gain = gains_table[-1][-1]
    result = (best_combination, total_gain)
    return result

def run(path_list):
    for path in path_list:
        #Import depuis le CSV originel
        actions_list = read_csv(path)
        # Création de la liste d'objets Action à partir des listes d'entiers
        action_obj_list = create_action_obj_list(actions_list[0],actions_list[1],actions_list[2])
        # Recherche de la meilleur combinaison possible, et son gain associé 
        best_combination, best_profit = find_best_combination(500, action_obj_list)
        best_combination_str = "".join([f'\n{a.id}({a.valeur})' for a in best_combination]) # Convertion textuelle
        #Valeur du porte-feuille d'actions
        total_value = sum(action.valeur for action in best_combination)
        print("\n""La valeur totale de la combinaison est :", total_value)
        print("La combinaison la plus rentable est :", best_combination_str,"\n""avec un profit de", round(best_profit/100, 2)) 


path_list = ["dataset1_Python+P7.csv","dataset2_Python+P7.csv"]

run(path_list)
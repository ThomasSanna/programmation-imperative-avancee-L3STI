reseau = [ 
  [0, 7, 3, 0, 0, 0],
  [0, 0, 0, 1, 1, 0],
  [4, 0, 0, 1, 0, 6],
  [0, 2, 0, 0, 4, 0],
  [0, 0, 0, 0, 0, 1],
  [0, 0, 0, 2, 3, 0]
]

sommets = ["S0", "S1", "S2", "S3", "S4", "S5"]
ptDepart = 0
ptArrive = 5
distPcc = float('inf')
lsPcc = []
distChemin = 0
lsChemin = []

def accepte(ei, e, LS, distPcc, distChemin):
  global reseau, sommets
  indE = sommets.index(e)
  indEi = sommets.index(ei)
  if reseau[indEi][indE] == 0:
    return False
  elif e in LS:
    return False
  elif distChemin + reseau[indEi][indE] > distPcc:
    return False
  return True
  































def plus_court_chemin(reseau, depart, destination, visites=None):
    if visites is None:
        visites = set()
    
    if depart == destination:
        return (0, [depart])
    
    visites.add(depart)
    min_distance = float('inf')
    min_chemin = []
    
    for voisin, poids in enumerate(reseau[depart]):
        if poids > 0 and voisin not in visites:
            distance, chemin = plus_court_chemin(reseau, voisin, destination, visites.copy())
            if distance != float('inf'):
                total_distance = poids + distance
                if total_distance < min_distance:
                    min_distance = total_distance
                    min_chemin = [depart] + chemin
    
    return (min_distance, min_chemin)

# Exemple d'utilisation
depart = 0
destination = 5
distance, chemin = plus_court_chemin(reseau, depart, destination)
print(f"Le plus court chemin de {depart} à {destination} est {chemin} avec une distance de {distance}")
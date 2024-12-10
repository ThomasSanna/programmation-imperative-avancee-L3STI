import random
from itertools import permutations
from copy import deepcopy

listeNombre = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10, 25,50,75,100]
nbAleatoire = []
for i in range(6):
  indexAleatoire = random.randint(0,len(listeNombre)-1)
  nbAleatoire.append(listeNombre[indexAleatoire])
  
nbTrouve = random.randint(100, 999)

listeOperateur = ['+', '-', '*', '/']

def operationsPossibles(num1, num2):
  ops = []
  if num1 > num2:
    ops.append((num1 + num2, f"{num1} + {num2}"))
    ops.append((num1 - num2, f"{num1} - {num2}"))
    if num1 % num2 == 0:
      ops.append((num1 // num2, f"{num1} / {num2}"))
    ops.append((num1 * num2, f"{num1} * {num2}"))
  return ops

def compteEstBon(nbAleatoire, nbTrouve, operations=[]):
  if nbTrouve in nbAleatoire:
    return True, operations

  if len(nbAleatoire) < 2:
    return False, operations

  for (num1, num2) in permutations(nbAleatoire, 2):
    for result, operation in operationsPossibles(num1, num2):
      new_nbAleatoire = deepcopy(nbAleatoire)
      new_nbAleatoire.remove(num1)
      new_nbAleatoire.remove(num2)
      new_nbAleatoire.append(result)
      new_operations = operations + [operation]
      found, final_operations = compteEstBon(new_nbAleatoire, nbTrouve, new_operations)
      if found:
        return True, final_operations

  return False, operations

found, operations = compteEstBon(nbAleatoire, nbTrouve)
if found:
  print("Le compte de " + str(nbTrouve) + " est bon")
  for op in operations:
    print(op)
else:
  print("Le compte n'est pas bon")
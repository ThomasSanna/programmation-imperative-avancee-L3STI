def getCard(n, tab, position):
  res = 1
  for i in range(position+1, len(tab)):
    if tab[i] == n:
      res += 1
  return res

def aUnMajoritaire(tab):
  ls = []
  for i, elt in enumerate(tab):
    if elt not in ls or i > len(tab) // 2:
      ls.append(elt)
      if getCard(elt, tab, i) > len(tab) // 2:
        return True
  return False

tab = [1, 2, 3, 4, 5, 1, 7, 1, 9, 1, 1, 1, 1, 10, 1, 1, 9]
print(aUnMajoritaire(tab))


def getCardRec(n, tab, position):
  if position >= len(tab):
    return 0
  if tab[position] == n:
    return 1 + getCardRec(n, tab, position + 1)
  return getCardRec(n, tab, position + 1)

def aUnMajoritaireRec(tab):
  def helper(tab, debut, fin):
    if debut == fin: # condition d'arrêt
      return tab[debut], 1
    
    milieu = (debut + fin) // 2
    gaucheMajoritaire, gaucheCompte = helper(tab, debut, milieu) # on cherche le majoritaire dans la partie gauche
    droiteMajoritaire, droiteCompte = helper(tab, milieu + 1, fin) # on cherche le majoritaire dans la partie droite
    
    if gaucheMajoritaire == droiteMajoritaire: # ie si le majoritaire est le même dans les deux parties
      return gaucheMajoritaire, gaucheCompte + droiteCompte # on retourne le majoritaire et son nombre d'occurences
    
    gaucheTotal = gaucheCompte + getCardRec(gaucheMajoritaire, tab, milieu + 1) # on compte le nombre d'occurences du majoritaire dans la partie gauche
    droiteTotal = droiteCompte + getCardRec(droiteMajoritaire, tab, debut) # on compte le nombre d'occurences du majoritaire dans la partie droite
    
    if gaucheTotal > (fin - debut + 1) // 2: # ie si le majoritaire est dans la partie gauche
      return gaucheMajoritaire, gaucheTotal # on retourne le majoritaire et son nombre d'occurences
    if droiteTotal > (fin - debut + 1) // 2:
      return droiteMajoritaire, droiteTotal
    
    return -1, 0
  
  majoritaire, compte = helper(tab, 0, len(tab) - 1)
  return majoritaire if compte > len(tab) // 2 else -1

tab = [1, 2, 3, 4, 5, 1, 7, 1, 9, 1, 1, 1, 1, 10, 1, 1, 9]
print(aUnMajoritaireRec(tab))
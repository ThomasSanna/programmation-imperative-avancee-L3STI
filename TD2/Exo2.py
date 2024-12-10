def notationPolonaiseLogique(chaine: str) -> bool:

    if not chaine:
      raise ValueError('La chaîne est vide!')
    
    tabBool = []
    tabElt = chaine.split(" ")
    # On inverse la liste pour pouvoir traiter les opérateurs de droite à gauche
    for elt in tabElt[::-1]: 
        if elt in ["True", "False"]:
            tabBool.append(elt == "True")
        elif elt in ['or', 'and']:
            if len(tabBool) < 2:
                raise ValueError('Il y a un problème sur la notation!')
            b1 = tabBool.pop()
            b2 = tabBool.pop()
            tabBool.append(b1 or b2 if elt == "or" else b1 and b2)
        elif elt == 'not':
            if not tabBool:
                raise ValueError('Il y a un problème sur la notation!')
            tabBool[-1] = not tabBool[-1]
        else:
            raise ValueError(f"Il y a un problème sur la notation! : {elt} est suspect")
    return tabBool[0]
  
print(notationPolonaiseLogique("and not False True"))  # Output: True

v = [True]*5

def actualiserTab(v):
  return [
    f"and {v[0]} not {v[4]}", 
    f"or {v[1]} and {v[2]} {v[3]}", 
    f"or not {v[0]} not {v[1]}", 
    f"or and {v[1]} {v[3]} and {v[2]} not {v[4]}", 
    f"or {v[2]} and {v[1]} {v[4]}"
    ]

def testInterrupteurs(tab):
  return all(notationPolonaiseLogique(elt) for elt in tab)

def prog(v, index=0):
  if index == len(v):
    tab = actualiserTab(v)
    if testInterrupteurs(tab):
      return (True, v)
    return (False, v)
  
  v[index] = True
  found, res = prog(v, index + 1)
  if found:
    return (found, res)
  
  v[index] = False
  found, res = prog(v, index + 1)
  if found:
    return (found, res)
  
  return (False, v)
  
  
print(prog(v))  # Output: (True, [True, False, True, False, True])
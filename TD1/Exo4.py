def operation(n1: float, n2: float, operateur: str) -> float:
    """
    Effectue une opération arithmétique entre deux nombres.

    Args:
        n1 (float): Le premier nombre.
        n2 (float): Le deuxième nombre.
        operateur (str): L'opérateur arithmétique sous forme de chaîne de caractères.
                         Les opérateurs valides sont '+', '-', '*', '/'.

    Returns:
        float: Le résultat de l'opération arithmétique.

    Raises:
        ValueError: Si l'opérateur est inconnu.
    """
    match operateur:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            return n1 / n2
        case _:
            raise ValueError(f"Opérateur inconnu: {operateur}")

def notationPolonaise(chaine: str) -> float:
    """
    Évalue une expression en notation polonaise inversée (RPN).

    Args:
        chaine (str): Une chaîne de caractères représentant l'expression en notation polonaise inversée.
                      Les opérandes doivent être des chiffres et les opérateurs peuvent être '+', '-', '*', '/'.

    Returns:
        float: Le résultat de l'évaluation de l'expression.

    Raises:
        ValueError: Si la notation est incorrecte ou si un caractère suspect est trouvé.
    """
    
    if not chaine:
      raise ValueError('La chaîne est vide!')
    
    tabInt = []
    for elt in chaine[::-1]:
        if elt in '0123456789':
            tabInt.append(int(elt))
        elif elt in "+-*/":
            if len(tabInt) < 2:
                raise ValueError('Il y a un problème sur la notation!')
            num1 = tabInt.pop()
            num2 = tabInt.pop()
            tabInt.append(operation(num1, num2, elt))
        else:
            raise ValueError(f"Il y a un problème sur la notation! : {elt} est suspect")
    return tabInt[0]

print(notationPolonaise("+*234"))  # Output: 14
print(notationPolonaise('*2+34'))  # Output: 14

def notationPolonaiseLogique(chaine: str) -> bool:
    """
    Évalue une expression logique en notation polonaise inversée (RPN).

    Args:
        chaine (str): Une chaîne de caractères représentant l'expression logique en notation polonaise inversée.
                      Les opérandes doivent être "True" ou "False" et les opérateurs peuvent être 'and', 'or', 'not'.

    Returns:
        bool: Le résultat de l'évaluation de l'expression logique.

    Raises:
        ValueError: Si la notation est incorrecte ou si un caractère suspect est trouvé.
    """
    
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
print(notationPolonaiseLogique("or True not True"))  # Output: True
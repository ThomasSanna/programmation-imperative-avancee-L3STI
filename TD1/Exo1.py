def factRec(n):
    if n == 0:
        return 1
    else:
        return n * factRec(n-1)
  
def carreRec(n):
    if n == 0:
        return 0
    else:
        return carreRec(n-1) + 2*n - 1
      
def pgcd(a,b):
    if b==0:
        return a
    else:
        return pgcd(b, a%b)
      
def somme(a, b):
    if b == 0:
        return a
    else:
        return somme(a, b-1) + 1
      
def produit(a, b):
    if b == 0:
        return 0
    else:
        return produit(a, b-1) + a

if __name__ == "__main__":
  assert factRec(5) == 120
  assert carreRec(4) == 16
  assert pgcd(48, 18) == 6
  assert somme(5, 3) == 8
  assert produit(6, 7) == 42
  print("All tests passed.")
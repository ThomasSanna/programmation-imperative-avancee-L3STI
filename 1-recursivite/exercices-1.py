#1 
def somme(n):
  if n<=0:
    raise ValueError('Le nombre doit être positif non nul')
  if n == 1:
    return 1
  return n + somme(n-1)

#2
def has10(n):
  if 0 <= n <= 9:
    return n == 0
  return n%10 == 0 or has10(n//10)

#3 
def calcPuissance(x, n):
  res = 1
  for i in range(n):
    res *= x
  return res


#4
def calcPuissanceRec(x, n):
  if n == 1:
    return x
  return x * calcPuissanceRec(x, n-1)

#5
def fibonacci(n):
  if n < 0:
    raise ValueError('Le nombre doit être positif')
  if n == 0 or n == 1:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

def main():
    try:
        print("somme(5):", somme(5))  
        print("somme(1):", somme(1))  
        print("somme(0):", somme(0)) 
    except ValueError as e:
        print("Erreur:", e)

    # Test pour la fonction has10
    print("has10(12345):", has10(12345))
    print("has10(102345):", has10(102345))
    print("has10(0):", has10(0)) 

    # Test pour la fonction calcPuissance
    print("calcPuissance(2, 3):", calcPuissance(2, 3))
    print("calcPuissance(5, 0):", calcPuissance(5, 0))

    # Test pour la fonction calcPuissanceRec
    print("calcPuissanceRec(2, 3):", calcPuissanceRec(2, 3)) 
    print("calcPuissanceRec(5, 1):", calcPuissanceRec(5, 1))  

    # Test pour la fonction fibonacci
    try:
        print("fibonacci(5):", fibonacci(5))  
        print("fibonacci(0):", fibonacci(0)) 
        print("fibonacci(-1):", fibonacci(-1))  
    except ValueError as e:
        print("Erreur:", e)

if __name__ == "__main__":
    main()
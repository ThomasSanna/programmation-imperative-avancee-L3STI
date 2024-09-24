def deplacer (tabA, tabB):
  tabB[1].append(tabA[1][-1])
  tabA[1].pop()
  print(tabA, tabB, tabC)

n = 3
tabA = ("A", [n-i for i in range(n)])
tabB = ("B", [])
tabC = ("C", [])

print(tabA, tabB, tabC)

def hanoi(n, tabA, tabB, tabC):
  if n == 0: 
    return None
  hanoi(n-1, tabA, tabC, tabB)
  deplacer(tabA, tabB)
  hanoi(n-1, tabC, tabB, tabA)
    
hanoi(n, tabA, tabB, tabC)
# print(tabA, tabB, tabC)


"""
('A', [3, 2, 1]) ('B', []) ('C', [])
('A', [3, 2]) ('B', [1]) ('C', [])
('A', [3]) ('C', [2]) ('B', [1])
('B', []) ('C', [2, 1]) ('A', [3])
('A', []) ('B', [3]) ('C', [2, 1])
('C', [2]) ('A', [1]) ('B', [3])
('C', []) ('B', [3, 2]) ('A', [1])
('A', []) ('B', [3, 2, 1]) ('C', [])
"""
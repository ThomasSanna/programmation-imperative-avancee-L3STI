def quickSort(tab):
  if len(tab) == 0:
    return tab
  pivot = tab[len(tab)//2]
  moins = [elt for elt in tab if elt < pivot]
  egal = [elt for elt in tab if elt == pivot]
  plus = [elt for elt in tab if elt > pivot]
  return quickSort(moins) + egal + quickSort(plus)

tab = [3, 6, 8, 10, 1, 2, 1, 4, 5, 7, 9]
print(quickSort(tab))


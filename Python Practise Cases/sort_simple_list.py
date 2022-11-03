# notice the difference between .sort() and sorted

lista = [1, 23, 4, 5, 67, 101]
lista.sort(reverse=True)  # change the original list
print(lista)
listb = sorted(lista, reverse=True)  # keep the original list intact
print(listb)

liste = ["BMW", "Mercedes", "Opel", "Mazda"]

print(liste)

print(len(liste))

print(liste[0])
print(liste[-1])

liste[-1] = "Toyota"
print(liste)

print(liste.index("Opel"))

print(liste[-2])

print(liste[0:3])

liste[-2:] = ["Toyota", "Renault"]
print(liste)

liste2 = ["Audi", "Nissan"]
liste.extend(liste2)
print(liste)

liste.pop()
print(liste)

liste.reverse()
print(liste)
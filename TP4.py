def multiplication():
    nombre = float(input("Vous cherchez la table de multiplication de quel nombre ? "))
    resultat = []

    for i in range(11):
        resultat.append(nombre * i)

    for i in range(11):
        print(nombre, "*", i, "=", round(resultat[i], 1))


#multiplication()

def moyenne():
    nombreEtudiants = int(input("Donnez le nombre d'étudiants : "))

    notes = []
    moyenne = 0.0

    for i in range(nombreEtudiants):
        note = -1
        while note < 0 or note > 20:
            note = float(input(f"Note étudiant {i} : "))
        notes.append(note)

    moyenne = sum(notes) / nombreEtudiants

    print(f"Moyenne de classe : {moyenne}")
    print("Numéro de l’étudiant | note | écart à la moyenne")

    for i in range(nombreEtudiants):
        ecart = notes[i] - moyenne
        print(f"{i} | {notes[i]} | {round(ecart, 1)}")


#moyenne()

def scalaire():
    nMax = 3
    v1 = []
    v2 = []

    n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
    while n < 1 or n > nMax:
        n = int(input(f"Erreur ! Entrez une valeur entre 1 et {nMax} : "))

    print("Saisie du premier vecteur :")
    for i in range(n):
        val = int(input(f"v1[{i}] = "))
        v1.append(val)

    print("Saisie du second vecteur :")
    for i in range(n):
        val = int(input(f"v2[{i}] = "))
        v2.append(val)

    produit_scalaire = 0
    for i in range(n):
        produit_scalaire += v1[i] * v2[i]

    print(f"Le produit scalaire de v1 par v2 vaut {float(produit_scalaire)}.")


#scalaire()

def frequent1(L):
    max_count = 0
    plus_frequent = L[0]

    for i in range(len(L)):
        current = L[i]
        compteur = 0
        for j in range(len(L)):
            if L[j] == current:
                compteur += 1
        if compteur > max_count:
            max_count = compteur
            plus_frequent = current

    print(f"Le nombre le plus fréquent dans la liste est : {plus_frequent} ({max_count} x)")


# frequent1([2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6])

def frequent2(L):
    most_frequent = L[0]
    max_count = L.count(L[0])

    for element in L:
        compteur = L.count(element)
        if compteur > max_count:
            max_count = compteur
            most_frequent = element

    print(f"Le nombre le plus fréquent dans la liste est : {most_frequent} ({max_count} x)")

def verificationDate():
    date = input("Entrez une date sous la forme jjmmaaaa : ")

    if len(date) != 8:
        print("Format incorrect, la date doit contenir exactement 8 chiffres (jjmmaaaa).")
        return

    jj = int(date[0:2])
    mm = int(date[2:4])
    aaaa = int(date[4:8])

    if mm < 1 or mm > 12:
        print("Date incorrecte : le mois est invalide.")
        return

    # Année bissextile
    bissextile = (aaaa % 4 == 0 and aaaa % 100 != 0) or (aaaa % 400 == 0)

    # Jours max selon le mois
    if mm in [1, 3, 5, 7, 8, 10, 12]:
        max_jour = 31
    elif mm in [4, 6, 9, 11]:
        max_jour = 30
    else:
        max_jour = 29 if bissextile else 28

    if jj < 1 or jj > max_jour:
        print("Date incorrecte : le jour est invalide pour ce mois.")
    else:
        print("Date correcte !")


#verificationDate()

# Exercice N°6

def tri_selection():
    tab = [5, 2, 4, 8, 1, 3]   # la liste donnée dans l'énoncé

    print("Phase 0 :", tab)

    n = len(tab)
    for i in range(n-1):
        min_index = i

        # Chercher le plus petit élément dans le reste du tableau
        for j in range(i+1, n):
            if tab[j] < tab[min_index]:
                min_index = j

        # On permute si un plus petit élément a été trouvé
        if min_index != i:
            tab[i], tab[min_index] = tab[min_index], tab[i]

        print(f"Phase {i+1} :", tab)


tri_selection()

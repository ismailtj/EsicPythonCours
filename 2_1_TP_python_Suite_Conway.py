# Ex 1
print("EX 1")

# 1a
chaine = "Il fait beau aujourd'hui. Je veux en profiter."

# 1b
chaine = chaine.replace('.', '!')
print("1b :", chaine)

# 1c
chaine_minuscule = chaine.lower()
print("1c :", chaine_minuscule)

# 1d
chaine_majuscule = chaine.upper()
print("1d :", chaine_majuscule)

# 1e
indice_b = chaine.find('b')
print("1e :", indice_b)

#EX 2
print("EX 2")

def premierMot(chaine):
    mots = chaine.split()
    return mots[0] if mots else ""

print(premierMot("samedi soir, je vais au cinéma"))


#EX 3
print("EX 3")

def majuscule_mot(chaine):
    return chaine.title()

chaine = "je mange du fromage"
res = majuscule_mot(chaine)
print("Résultat :", res)



#EX 4
print("EX 4")

def inverser_phrase(phrase):
    mots = phrase.split()
    mots_inverses = mots[::-1]
    phrase_inversee = " ".join(mots_inverses)
    return phrase_inversee

phrase = "J’en suis tout retourné"
print(inverser_phrase(phrase))


#EX 5
print("EX 5")

def image(mot):
    res = ""
    compt = 1 

    for i in range(1, len(mot)):
        if mot[i] == mot[i - 1]:
            compt += 1
        else:
            res += str(compt) + mot[i - 1]
            compt = 1

    res += str(compt) + mot[-1]
    return res


def generer_suite(n):
    terme = "1"
    print(f"u0 = {terme}")
    for i in range(1, n):
        terme = image(terme)
        print(f"u{i} = {terme}")

generer_suite(20)

import random
import csv


spanisch   =   ["el pelo", "rubio", "moreno", "castano", "pelirrojo", "el piel", "el ojo", "la barba", "bajo", "delgado", "gordo"]
deutsch    =   ["das Haar", "blond", "dunkelhaarig", "brünett", "rothaarig", "die Haut", "das Auge", "der Bart", "klein", "schlank", "dick"]

sprache = input("Auf welche Sprache möchtest du Übersetzen?: ").lower()

if sprache == "deutsch":

    while True:
        vokabel = random.randint(0, len(spanisch)-1)
        print(spanisch[vokabel])
        antwort = input("Deutsche Überstzung: ")
        if antwort == deutsch[vokabel]:
            print("Richtig! \n")
        else:
            print("Falsch!")
            print(deutsch[vokabel],"\n")
if sprache == "spanisch":
    while True:
        vokabel = random.randint(0, len(spanisch) - 1)
        print(deutsch[vokabel])
        antwort = input("Spanische Überstzung: ")
        if antwort == spanisch[vokabel]:
            print("Richtig! \n")
        else:
            print("Falsch!")
            print(spanisch[vokabel],"\n")

else:
    print("Bischt du dumm in deinem Kopf")

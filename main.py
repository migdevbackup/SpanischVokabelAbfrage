import csv
import random


sprache = input("In which language do you want to translate to?: ").lower()

with open("vocabs.csv", "r") as list:
    csv_reader = csv.reader(list, delimiter=";")
    next(csv_reader)

    length = 0
    spanish = []
    german = []

    for line in csv_reader:
        spanish.append(line[0])
        german.append(line[1])
        length += 1



    if sprache == "german":

        while True:
            i = random.randint(0, length - 1)
            print(spanish[i])
            antwort = input("German translation: ")
            if antwort == german[i]:
                print("Correct! \n")
            else:
                print("Wrong!")
                print(german[i], "\n")
    if sprache == "spanish":
        while True:
            i = random.randint(0, length - 1)
            print(german[i])
            antwort = input("Spanish Translation: ")
            if antwort == spanish[i]:
                print("Correct! \n")
            else:
                print("Wrong!")
                print(spanish[i], "\n")

    if sprache == "both":
        while True:
            i = random.randint(0, length - 1)
            language = random.randint(0, 1)

            if language == 0:
                quest = input("What is '" + spanish[i] + "' in german: ")

                if quest == german[i]:
                    print("Correct!")
                else:
                    print("That is not correct !")
            else:
                quest = input("What is '" + german[i] + "' in spanish: ")

                if quest == spanish[i]:
                    print("Correct!")
                else:
                    print("That is not correct !")

    else:
        print("You stupid?")

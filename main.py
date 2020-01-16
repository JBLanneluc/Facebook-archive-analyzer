#ASCII Intro :
import os
os.system("cls")
print("---------------------------------------------------")
ASCII = " ______      _____ ______ ____   ____   ____  _  __\n|  ____/\\   / ____|  ____|  _ \\ / __ \\ / __ \\| |/ /\n| |__ /  \\ | |    | |__  | |_) | |  | | |  | | ' /\n|  __/ /\\ \\| |    |  __| |  _ <| |  | | |  | |  <\n| | / ____ \\ |____| |____| |_) | |__| | |__| | . \\\n|_|/_/    \\_\\_____|______|____/ \\____/ \\____/|_|\\_\\\n\n\n __  __ ______  _____ _____ ______ _   _  _____ ______ _____\n|  \\/  |  ____|/ ____/ ____|  ____| \\ | |/ ____|  ____|  __ \\\n| \\  / | |__  | (___| (___ | |__  |  \\| | |  __| |__  | |__) |\n| |\\/| |  __|  \\___ \\\\___ \\|  __| | . ` | | |_ |  __| |  _  /\n| |  | | |____ ____) |___) | |____| |\\  | |__| | |____| | \\ \\\n|_|  |_|______|_____/_____/|______|_| \\_|\\_____|______|_|  \\_\\\n\n\n          _   _          _  __     ______________ _____\n    /\\   | \\ | |   /\\   | | \\ \\   / /___  /  ____|  __ \\\n   /  \\  |  \\| |  /  \\  | |  \\ \\_/ /   / /| |__  | |__) |\n  / /\\ \\ | . ` | / /\\ \\ | |   \\   /   / / |  __| |  _  /\n / ____ \\| |\\  |/ ____ \\| |____| |   / /__| |____| | \\ \\\n/_/    \\_\\_| \\_/_/    \\_\\______|_|  /_____|______|_|  \\_\\\n"

print(ASCII)
print("---------------------------------------------------\n")
print("Bienvenue sur notre programme d'analyse messenger. \nNous allons analyser votre archive facebook et en extraire des statistiques à titre informatif. \nSoyez rassuré, ces statistiques ne seront visibles que par vous-même, et en aucun cas elles ne seront envoyées ou stockées ailleurs.")
#print("\nEntrez le chemin vers votre archive décompressée :")
print("\nAppuyez sur Entrée pour continuer.")

from functions_main import *
from word_count import *
from functions_word_count import *
from functions_characterize import *

def display_dates_menu():
    os.system('cls')
    print("Indiquez les dates de début et de fin sous le format DD/MM/YYYY:")
    print("Date de début :")
    begin_date = input()
    print("Date de fin :")
    end_date = input()
    return select_data_between_dates(begin_date, end_date, df_sent)

def display_graph_menu():
    df_temp = df_sent.copy()
    local_quit = 0
    while local_quit == 0:
        os.system('cls')
        print("Quel graphique souhaitez-vous afficher ?")
        print("1. Messages par heure en fonction du jour de la semaine")
        print("2. Messages par mois en fonction de l'année")
        print("3. Messages par jour de la semaine en fonction de l'année")
        print("4. Jour de la semaine en fonction du mois")
        print("5. Changer la plage temporelle des données")
        print("6. Restaurer les données")
        print("7. Retour")
        selection = input()

        if selection == "1":
            display_graph_pyplot1(df_temp)
        elif selection == "2":
            display_graph_pyplot2(df_temp)
        elif selection == "3":
            display_graph_pyplot3(df_temp)
        elif selection == "4":
            display_graph_pyplot4(df_temp)
        elif selection == "5":
            df_temp = display_dates_menu()
            print(df_temp)
        elif selection == "6":
            df_temp = df_sent.copy()
        elif selection == "7":
            local_quit = 1
            os.system('cls')

        else :
            print("Sélection incorrecte")

def display_analyzer_menu():
    users_list = palmares(df_sent,df_received)
    os.system('cls')
    print("Entrez le nom d'une personne\nAttention à bien entrer le même nom que sur facebook :")
    ok = -1
    while ok == -1 :
        username = input()
        if username == 'Retour':
            return
        if username in users_list.index:
            print("Utilisateur identifié")
            ok = 0
        else:
            print("Utilisateur inconnu, veuillez réessayer, ou entrez 'Retour' si vous souhaitez revenir en arrière")
    conversation_analyser(username)
    print("Appuyez sur entrée pour revenir au menu précédent")
    input()





def display_palmares_menu():
    os.system('cls')
    print("Combien de personnes souhaitez-vous afficher ?")

    ok = -1
    while ok == -1:
        ok = 0
        try:
           n = int(input())
        except ValueError:
           print("Ce n'est pas un entier")
           ok = -1

    print('\n')
    top = palmares(df_sent, df_received, n)
    print("\nSouhaitez-vous estimer vos relations avec l'une des personnes ci-dessus ?\nRépondez par 'oui' ou par 'non':")
    ok = -1
    while ok == -1 :
        ok = 1
        choice = input()
        if choice == "non":
            return
        elif choice != "oui":
            ok = -1
            print("Entrée incorrecte, réessayez :")

    ok = -1
    print("Entrez le numéro ci-dessus correspondant à la personne:")
    while ok == -1:
        ok = 0
        try:
           choice = int(input())
           if choice >= n:
               print("numéro incorrect, réessayez :")
               ok = -1
        except ValueError:
           print("Ce n'est pas un entier, réessayez :")
           ok = -1
    conversation_analyser(top.iloc[choice]['Nom'])
    print("Appuyez sur entrée pour revenir au menu précédent")
    input()




def display_relations_menu():
    local_quit = 0
    while local_quit == 0:
        os.system('cls')
        print("Menu d'analyse relationnelle")
        print("----------------------------")
        print("Que souhaitez-vous faire ?")
        print("1. Afficher le palmares des personnes avec lesquelles vous avez le plus échangé")
        print("2. Afficher vos relations estimées avec une personne")
        print("3. Retour")
        selection = input()

        if selection == "1":
            display_palmares_menu()
        elif selection == "2":
            display_analyzer_menu()
        elif selection == "3":
            local_quit = 1
            os.system('cls')






print("\nDonnées chargées avec succès")
quit = 0
while quit == 0 :
    print("Quelle opération souhaitez-vous réaliser ?")
    print("1. Afficher des graphiques de votre utilisation de messenger")
    print("2. Afficher vos affinités avec une personne")
    print("3. Quitter l'application")
    selection = input()

    if selection == "1":
        display_graph_menu()
    elif selection == "2":
        display_relations_menu()
    elif selection == "3":
        print("À bientôt")
        quit = 1
    else :
        print("Sélection incorrecte")


#print(df_sent)
#print(df_received)
#palmares = palmares(df_sent, df_received, 20)

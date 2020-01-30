#import pandas as pd
import datetime
from path import Path
import os
import platform
import json
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

#dir_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\"
#dir_path = "/home/jean-baptiste/Travail/5A/Projet/facebook-loicgarnier104/messages/inbox/"

## Fonctions

def path_finder():
    dir_path = input()
    print("\nChargement des données en cours")
    slash = OS_value("\\", '/')
    local_path = OS_value('messages\\inbox\\','messages/inbox/')

    if dir_path[-1] == slash:
        dir_path = dir_path + local_path
    else:
        dir_path = dir_path + slash + local_path
    return(dir_path)


def OS_value(windows_value, linux_value):
    if platform.system() == 'Linux':
        return linux_value
    if platform.system() == 'Windows':
        return windows_value
    if platform.system() == 'Darwin':
        return linux_value
    else :
        return 'Erreur OS'


#Renvoit 2 listes pour une discussion precise : celle des messages recus et celle des messages envoyes avec l'expéditeur
def file_parser(file_path):
    with open(file_path) as json_data:
        data = json.load(json_data)
    user1 = "LoÃ¯c Garnier"
    user2 = ""
    for name in data['participants']:
        if name['name'] != user1:
            user2 = name['name']
    messages_received = []
    messages_sent = []
    for k in data["messages"]:
        if (k["sender_name"] != "LoÃ¯c Garnier" and 'content' in k):
            messages_received.append([k['timestamp_ms'],k['content'],k['sender_name'], user1])
        if (k["sender_name"] == "LoÃ¯c Garnier" and 'content' in k):
            messages_sent.append([k['timestamp_ms'],k['content'],k['sender_name'], user2])
    return [messages_sent, messages_received]

# convertit un timestamp en millisecondes depuis epoch en date lisible au format string
def convert_timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(float(timestamp)/1000).strftime("%d/%m/%Y %H:%M:%S")

# Renvoie la liste des fichiers de discussion à 2 et la liste des fichiers de discussions de groupe (chemin complet des fichiers)
def group_file_list(dir_path):
    dirs_list = []
    for path, dirs, files in os.walk(dir_path):
        dirs_list = dirs
        break
    dir_dictionary = {}
    duo_list = []
    group_list = []
    for dir in dirs_list:
        for file in message_files_list(dir_path + dir):
            with open(file) as json_data:
                data = json.load(json_data)
            participants_number = len(data["participants"])
            if participants_number > 2:
                group_list.append(file)
            elif participants_number == 2:
                duo_list.append(file)
                name = (data["participants"][0]["name"]).encode('latin1').decode('utf-8-sig')
                dir_dictionary[name] = dir
    return duo_list, group_list, dir_dictionary

def number_of_messages(name):
    number = 0

# renvoie la liste des fichiers de messages json dans le dossier en input
def message_files_list(dir_path):
    result = []
    for f in Path(dir_path).walkfiles():
        if (f.find('message_') != -1 and f.find('.json') != -1):
            result.append(f)
    return result


def extract_timestamp(messages_list):
    result = []
    for message in messages_list:
        result.append(message[0])
    return result


#Renvoie uniquement les discussions à 2, pas les discussions de groupes, sous la forme [[timestamp, content, sender, receiver],...]
def all_directories_timestamp_messages_parser(dir_path):
    sent_timestamp_list = []
    received_timestamp_list = []
    file_list, _, dir_dictionary = group_file_list(dir_path)
    for file in file_list:
        file_sent, file_received = file_parser(file)
        sent_timestamp_list = sent_timestamp_list + file_sent   #Juste une liste des timestamps des messages envoyés
        received_timestamp_list = received_timestamp_list + file_received #Liste des timestamps des messages reçus et de l'expéditeur : [[timestamp1, expéditeur1], [timestamp2, expéditeur2]]...
    return sent_timestamp_list, received_timestamp_list, dir_dictionary




# convertit une liste detimestamps depuis epoch en liste de dates au format string
def convert_timestamp_list_to_timestamp_date(timestamp_list):
    return [convert_timestamp_to_date(timestamp) for timestamp in timestamp_list]



#timestamp_list doit etre au format humain
def normalize_dataframe(messages_list):
    timestamps = extract_timestamp(messages_list)
    timestamps_date = convert_timestamp_list_to_timestamp_date(timestamps)
    day = []
    month = []
    year = []
    hour = []
    minute = []
    second = []
    weekday = []
    month_number = []
    Date = []
    sender = []
    receiver = []
    #content = []
    to_drop = []
    index = 0

    for message in messages_list:
        sender.append(message[2].encode('latin1').decode('utf-8-sig'))
        receiver.append(message[3].encode('latin1').decode('utf-8-sig'))
        if sender[-1] == "Utilisateur de Facebook" or receiver[-1] == "Utilisateur de Facebook":
            to_drop.append(index)
        index +=1
        #content.append(message[4]) #à ne mettre que si nécessaire, on verra si on en a besoin

    for timestamp in timestamps_date:
        date = timestamp.split(" ")[0]
        weekday_name = convert_weekday_number_to_name(convert_date_to_weekday_number(date))
        weekday.append(weekday_name)
        date = date.split("/")
        time = timestamp.split(" ")[1]
        time = time.split(":")

        Date.append(date[2] + "-" + date[1] + "-" + date[0] + " " + time[0] + ":" + time[1] + ":" + time[2])
        day.append(int(date[0]))
        month_number.append(int(date[1]))
        month.append(convert_month_number_to_name(int(date[1])))
        year.append(int(date[2]))
        hour.append(int(time[0]))
        minute.append(int(time[1]))
        second.append(int(time[2]))


    normalized_dataframe = pd.DataFrame({'day':day, 'month':month, 'year':year, 'hour':hour, 'minute':minute, 'second':second, 'month_number':month_number,'weekday':weekday, 'Date':pd.to_datetime(Date), 'sender':sender, 'receiver':receiver})
    to_drop.append(index)
    normalized_dataframe = normalized_dataframe.drop(to_drop[:-1])
    normalized_dataframe = normalized_dataframe.sort_values(by=['Date']).reset_index(drop=True)
    return normalized_dataframe



def test_dataframe():
    day = [1,1,2,4,4,4,4]
    month = ["Janvier","Janvier","Janvier","Janvier","Janvier","Janvier","Janvier"]
    year = [2019,2019,2019,2012,2012,2012,2012]
    hour = [12,12,12,0,0,0,0]
    minute = [15,30,40,0,0,0,0]
    second = [0,0,0,0,0,0,0]
    weekday = ["Lundi", "Lundi", "Lundi", "Lundi","Lundi","Lundi","Lundi"]
    month_number = [1,1,1,1,1,1,1]


    normalized_dataframe = pd.DataFrame({'day':day, 'month':month, 'year':year, 'hour':hour, 'minute':minute, 'second':second, 'month_number':month_number,'weekday':weekday})

    return normalized_dataframe





def convert_month_number_to_name(month_number):
    month_name = {1: "Janvier", 2: "Fevrier", 3: "Mars", 4: "Avril", 5: "Mai", 6: "Juin", 7: "Juillet", 8: "Aout", 9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Decembre"}
    return month_name[month_number]

def convert_date_to_weekday_number(date):
    weekday_number = datetime.datetime.strptime(date, '%d/%m/%Y').weekday()
    return weekday_number

def convert_weekday_number_to_name(weekday_number):
    weekday_calendar = {0: "Lundi", 1: "Mardi", 2: "Mercredi", 3: "Jeudi", 4: "Vendredi", 5: "Samedi", 6: "Dimanche"}
    if (weekday_number in weekday_calendar):
        return weekday_calendar[weekday_number]
    else:
        print("\nERROR: weekday_number = %s\n"%weekday_number)
        raise KeyError



#renvoie un dataframe contenant untiquement les donnees datees entre les 2 dates d'entrees (donnees au format "dd/MM/YYYY")
def select_data_between_dates(begin_date, end_date, data):
    begin_tuple = (int(begin_date[6:]),int(begin_date[3:5]),int(begin_date[0:2]))
    end_tuple = (int(end_date[6:]),int(end_date[3:5]),int(end_date[0:2]))
    index_to_keep = []
    print("Traitement en cours...")
    for index, row in data.iloc[::-1].iterrows():
        date_tuple = (row['year'],row['month_number'],row['day'])
        if (begin_tuple <= date_tuple  and date_tuple <= end_tuple):
            index_to_keep.append(index)
        elif (date_tuple < begin_tuple):
            break
    data_copy = data.copy()[index_to_keep[-1]:index_to_keep[0]]
    return data_copy




def get_years(normalized_dataframe):
    to_flatten = pd.DataFrame(normalized_dataframe.year.unique()).values.tolist()
    years = []
    for elem in to_flatten:
        years.append(elem[0])
    years.sort()
    return years

def get_months(normalized_dataframe):
    to_flatten = pd.DataFrame(normalized_dataframe.Date.dt.month.unique()).values.tolist()
    months = []
    for elem in to_flatten:
        months.append(elem[0])
    months.sort()
    return months

#Renvoie un dataframe des n utilisateurs qui nous ont envoyé le plus de messages et du nombre de messages reçus
#Si n n'est pas précisé, alors renvoie le nombre de messages échangés avec tous les utilisateurs
def palmares(df_sent, df_received, n=-1):
    palmares_sent = df_sent['receiver'].value_counts()
    palmares_received = df_received['sender'].value_counts()
    if n == -1:
        palmares = palmares_received.add(palmares_sent, fill_value=0).sort_values().astype('int32')
    elif n >= 0:
        palmares = palmares_received.add(palmares_sent, fill_value=0).sort_values().nlargest(n).astype('int32').reset_index()
        palmares.columns = ['Nom', 'Nombre de messages']
    else:
        print("Erreur, mauvaise valeur entrée")
        return
    print("Palmares des", n, "utilisateurs avec lesquels vous avez échangé le plus de messages :\n", palmares)
    return palmares


#Heures par jour de la semaine
def display_graph_pyplot1(df):
    fig, ax = plt.subplots(ncols=7, figsize=(30,10))
    plt.subplots_adjust(wspace=0.05)  #Remove some whitespace between subplots

    for idx, gp in df.groupby(df.Date.dt.dayofweek):
        ax[idx].set_title(gp.weekday.iloc[0])  #Set title to the weekday

        (gp.groupby(gp.Date.dt.hour).size().rename_axis('').to_frame('')
            .reindex(np.arange(0,24,1)).fillna(0)
            .plot(kind='bar', ax=ax[idx], rot=0, ec='k', legend=False))

        # Ticks and labels on leftmost only
        if idx == 0:
            _ = ax[idx].set_ylabel('Nombre de messages', fontsize=15)

        _ = ax[idx].tick_params(axis='x', which='major', labelsize=8,
                                labelleft=(idx == 0), left=(idx == 0))

        _ = ax[idx].tick_params(axis='y', which='major', labelsize=11,
                                labelleft=(idx == 0), left=(idx == 0))

        ax[idx].set_xticklabels([0,'',2,'',4,'',6,'',8,'',10,'',12,'',14,'',16,'',18,'',20,'',22,''])

    # Consistent bounds between subplots.
    lb, ub = list(zip(*[axis.get_ylim() for axis in ax]))
    for axis in ax:
        axis.set_ylim(min(lb), max(ub))
    fig.text(0.5, 0.02,  'Heure', ha='center', fontsize=15)
    plt.show()


#Mois par an
def display_graph_pyplot2(df):
    years=get_years(df)
    col_number = years[-1] - years[0] + 1
    fig, ax = plt.subplots(ncols=col_number, figsize=(30,10))
    if col_number == 1:
        ax = [ax]

    plt.subplots_adjust(wspace=0.05)  #Remove some whitespace between subplots

    for year, gp in df.groupby(df.year):
        idx = year - years[0]
        ax[idx].set_title(gp.year.iloc[0])  #Set title to the weekday

        (gp.groupby(gp.Date.dt.month).size().rename_axis('').to_frame('')
            .reindex(np.arange(1,13,1)).fillna(0)
            .plot(kind='bar', ax=ax[idx], rot=0, ec='k', legend=False))

        # Ticks and labels on leftmost only
        if idx == 0:
            _ = ax[idx].set_ylabel('Nombre de messages', fontsize=15)

        _ = ax[idx].tick_params(axis='x', which='major', labelsize=7,
                                labelleft=(idx == 0), left=(idx == 0))

        _ = ax[idx].tick_params(axis='y', which='major', labelsize=11,
                                labelleft=(idx == 0), left=(idx == 0))

    # Consistent bounds between subplots.
    lb, ub = list(zip(*[axis.get_ylim() for axis in ax]))
    for axis in ax:
        axis.set_ylim(min(lb), max(ub))

    fig.text(0.5, 0.02, 'Mois', ha='center', fontsize=15)
    plt.show()


#Jour de la semaine par an
def display_graph_pyplot3(df):
    years=get_years(df)
    col_number = years[-1] - years[0] + 1
    fig, ax = plt.subplots(ncols=col_number, figsize=(30,10))
    if col_number == 1:
        ax = [ax]
    plt.subplots_adjust(wspace=0.05)  #Remove some whitespace between subplots

    for year, gp in df.groupby(df.year):
        idx = year - years[0]
        ax[idx].set_title(gp.year.iloc[0])  #Set title to the weekday

        (gp.groupby(gp.Date.dt.dayofweek + 1).size().rename_axis('').to_frame('')
            .reindex(np.arange(1,8,1)).fillna(0)
            .plot(kind='bar', ax=ax[idx], rot=0, ec='k', legend=False))

        # Ticks and labels on leftmost only
        if idx == 0:
            _ = ax[idx].set_ylabel('Nombre de messages', fontsize=15)

        _ = ax[idx].tick_params(axis='both', which='major', labelsize=9,
                                labelleft=(idx == 0), left=(idx == 0))

    # Consistent bounds between subplots.
    lb, ub = list(zip(*[axis.get_ylim() for axis in ax]))
    for axis in ax:
        axis.set_ylim(min(lb), max(ub))

    fig.text(0.5, 0.02, 'Jour de la semaine', ha='center', fontsize=15)
    plt.show()

#Jour de la semaine par mois
def display_graph_pyplot4(df):
    months=get_months(df)
    col_number = months[-1] - months[0] + 1
    fig, ax = plt.subplots(ncols=col_number, figsize=(30,10))
    if col_number == 1:
        ax = [ax]
    plt.subplots_adjust(wspace=0.05)  #Remove some whitespace between subplots

    for idx, gp in df.groupby(df.Date.dt.month):
        idx = idx - months[0]
        ax[idx].set_title(gp.month.iloc[0])  #Set title to the month

        (gp.groupby(gp.Date.dt.dayofweek + 1).size().rename_axis('').to_frame('')
            .reindex(np.arange(1,8,1)).fillna(0)
            .plot(kind='bar', ax=ax[idx], rot=0, ec='k', legend=False))

        # Ticks and labels on leftmost only
        if idx == 0:
            _ = ax[idx].set_ylabel('Nombre de messages', fontsize=15)

        _ = ax[idx].tick_params(axis='both', which='major', labelsize=9,
                                labelleft=(idx == 0), left=(idx == 0))

    # Consistent bounds between subplots.
    lb, ub = list(zip(*[axis.get_ylim() for axis in ax]))
    for axis in ax:
        axis.set_ylim(min(lb), max(ub))

    fig.text(0.5, 0.02, 'Jour de la semaine', ha='center', fontsize=15)
    plt.show()

dir_path = path_finder()
messages_sent, messages_received, dir_dictionary = all_directories_timestamp_messages_parser(dir_path)
del dir_dictionary['Loïc Garnier']

df_sent = normalize_dataframe(messages_sent)
df_received = normalize_dataframe(messages_received)

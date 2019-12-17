#import pandas as pd
import datetime
from path import Path
import os
import json
import time
import pandas as pd
import matplotlib.pyplot as plt


## Fonctions

# renvoie la liste des timestamps de tous les messages envoyes par Loic Garnier dans le fichier en input
def sent_messages_timestamp_parser(file_path):
    with open(file_path) as json_data:
        data = json.load(json_data)

    timestamps_sender_loic = []
    for k in data["messages"]:
        if k["sender_name"] == "LoÃ¯c Garnier":
            timestamps_sender_loic.append(k["timestamp_ms"])

    return timestamps_sender_loic

# convertit un timestamp en millisecondes depuis epoch en date lisible au format string
def convert_timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(float(timestamp)/1000).strftime("%d/%m/%Y %H:%M:%S")


# renvoie la liste des fichiers de messages json dans le dossier en input
def message_files_list(dir_path):
    result = []
    for f in Path(dir_path).walkfiles():
        if (f.find('message_') != -1 and f.find('.json') != -1):
            result.append(f)
    return result

##



def all_directories_timestamp_messages_parser(dir_path):
    mega_timestamp_list = []
    for path, dirs, files in os.walk(dir_path):
        dirs_list = dirs
        break
    for dir in dirs_list:
        for file in message_files_list(dir_path + dir):
            mega_timestamp_list = mega_timestamp_list + sent_messages_timestamp_parser(file)
    return mega_timestamp_list





# convertit une liste detimestamps depuis epoch en liste de dates au format string
def convert_timestamp_list_to_timestamp_date(timestamp_list):
    return [convert_timestamp_to_date(timestamp) for timestamp in timestamp_list]



#timestamp_list doit etre au format humain
def normalize_dataframe(timestamp_list):
    day = []
    month = []
    year = []
    hour = []
    minute = []
    second = []
    weekday = []

    for timestamp in timestamp_list:
        date = timestamp.split(" ")[0]
        weekday_name = convert_weekday_number_to_name(convert_date_to_weekday_number(date))
        weekday.append(weekday_name)
        date = date.split("/")
        time = timestamp.split(" ")[1]
        time = time.split(":")



        day.append(int(date[0]))
        month.append(convert_month_number_to_name(int(date[1])))
        year.append(int(date[2]))
        hour.append(int(time[0]))
        minute.append(int(time[1]))
        second.append(int(time[2]))


    normalized_dataframe = pd.DataFrame({'day':day, 'month':month, 'year':year, 'hour':hour, 'minute':minute, 'second':second, 'weekday':weekday})

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











#dir_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\"
dir_path = "/home/jean-baptiste/Travail/5A/Projet/facebook-loicgarnier104/messages/inbox/"
result = all_directories_timestamp_messages_parser(dir_path)
result = sorted(result)
result = convert_timestamp_list_to_timestamp_date(result)
df = normalize_dataframe(result)
print(df)
df['hour'].plot.hist()
plt.show()









##

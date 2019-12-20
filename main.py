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

def received_messages_parser(file_path):
    with open(file_path) as json_data:
        data = json.load(json_data)

    messages_received = []
    for k in data["messages"]:
        if (k["sender_name"] != "LoÃ¯c Garnier" and 'content' in k):
            messages_received.append((k["sender_name"],k["content"]))

    return messages_received

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

def all_directories_received_messages_parser(dir_path):
    mega_messages_list = []
    for path, dirs, files in os.walk(dir_path):
        dirs_list = dirs
        break
    for dir in dirs_list:
        for file in message_files_list(dir_path + dir):
            mega_messages_list = mega_messages_list + received_messages_parser(file)
    return mega_messages_list



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
    month_number = []

    for timestamp in timestamp_list:
        date = timestamp.split(" ")[0]
        weekday_name = convert_weekday_number_to_name(convert_date_to_weekday_number(date))
        weekday.append(weekday_name)
        date = date.split("/")
        time = timestamp.split(" ")[1]
        time = time.split(":")



        day.append(int(date[0]))
        month_number.append(int(date[1]))
        month.append(convert_month_number_to_name(int(date[1])))
        year.append(int(date[2]))
        hour.append(int(time[0]))
        minute.append(int(time[1]))
        second.append(int(time[2]))


    normalized_dataframe = pd.DataFrame({'day':day, 'month':month, 'year':year, 'hour':hour, 'minute':minute, 'second':second, 'month_number':month_number,'weekday':weekday})

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

#renvoie un dataframe contenant untiquement les données datées entre les 2 dates d'entrées (données au format "dd/MM/YYYY")
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





def show_messages_per_interval(data, primary_interval, secondary_interval):

    bins_dictionnary = {"hour": 24, "weekday": 7, "month": 12, "second": 60, "minute": 60} # trouver le nombre d annees et le stocker pour le mettre dans le dico
    primary_interval = primary_interval.lower()
    primary_name = primary_interval #.capitalize()
    primary_number = bins_dictionnary[primary_interval]

    if (primary_interval == "weekday"):
        data[primary_interval].value_counts().hist(bins=24, edgecolor="black")
        #fig, ax = plt.subplots()
        weekday_names = "Lundi Mardi Mercredi Jeudi Vendredi Samedi Dimanche".split(' ')
        plt.xticks([0, 0.5 ,1,2,3,4,5], weekday_names)
        #ax.set_xticklabels(weekday_names)
        #ax.set_xticks(range(0, len(weekday_names)))
        #ax.plot()
    elif (primary_interval == "month"):
        data[primary_interval].value_counts().hist(bins=24, edgecolor="black")
        month_names = "Janvier Fevrier Mars Avril Mai Juin Juillet Aout Septembre Octobre Novembre Decembre".split(' ')
        #ax.set_xticklabels(month_names)
        #ax.set_xticks(range(0, len(month_names)))
    else:
        data[primary_interval].plot.hist(bins=24, edgecolor="black")

    plt.xlabel("Per " + primary_name)
    plt.ylabel("Average number of messages")
    plt.show()



def mega_function(data, primary_interval, secondary_interval, global_interval):
    percentage = False
    #primary_interval="weekday", secondary_interval="month"
    if percentage == True:
        summary = pd.DataFrame(data.groupby([secondary_interval])[primary_interval].value_counts()) # fonctionne mais pas la moyenne et legende a changer
        sum = data.groupby([secondary_interval])[primary_interval].count()
        summary = pd.DataFrame(data.groupby([secondary_interval])[primary_interval].value_counts() / sum * 100)
        #print(summary)
    else:
        summary = pd.DataFrame(data.groupby([secondary_interval])[primary_interval].value_counts()) # fonctionne mais pas la moyenne et legende a changer
        sum = data.groupby([secondary_interval])[primary_interval].count()
        summary = pd.DataFrame(data.groupby([secondary_interval])[primary_interval].value_counts() / sum * 100)
        #print(summary)

    """
    if percentage == True:
        summary = pd.DataFrame(data.groupby(["year"])["weekday"].value_counts()) # fonctionne mais pas la moyenne et legende a changer
        sum = data.groupby(["year"])["weekday"].count()
        summary = pd.DataFrame(data.groupby(["year"])["weekday"].value_counts() / sum * 100)
        print(summary)
    else:
        summary = pd.DataFrame(data.groupby(["year"])["weekday"].value_counts()) # fonctionne mais pas la moyenne et legende a changer
        sum = data.groupby(["year"])["weekday"].count()
        summary = pd.DataFrame(data.groupby(["year"])["weekday"].value_counts() / sum * 100)
        print(summary)
    """

    print("\n\n\n\n\n")
    print("avant unstack")
    print(summary)
    print("\n\n\n\n\n")
    summary = summary.unstack(level=0)
    print("apres unstack")
    print("\n\n\n\n\n")
    print(summary)
    print("\n\n\n\n\n")

    print(years)


    weekdays = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    months = ("Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre")
    hours = [5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4]
    dict = {"weekday": weekdays, "month": months, "hour": hours}
    if primary_interval == "weekday" or primary_interval == "month" or primary_interval == "hour":
        #print(dict[secondary_interval])
        #print(dict[primary_interval])

        summary = summary.reindex(index=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"])
        print("\n\n\n\n\n")
        print(summary)
        print("\n\n\n\n\n")
        print("\n\nerror ?\n\n\n")
        summary = summary.reindex(columns=("month", "Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"))
        print("\n\n\n\n\n")
        print(summary)
        print("\n\n\n\n\n")
        #summary = summary[dict["month"]]
        #summary = summary.unstack(level=0)

        #summary = summary.reindex(months, axis=(1))

        #summary = summary.reindex(dict[secondary_interval])

    #print(summary)
    #summary = summary.reindex(weekdays)
    #summary.plot(kind='line', subplots=False)
    summary.plot(kind='bar', subplots=False)
    plt.legend(loc="upper right")

    plt.xlabel("Jour de la semaine") #
    plt.ylabel("Pourcentage de messages envoyés")
    plt.title("Pourcentage de messages envoyés par jour de la semaine selon les années") #
    plt.tight_layout()
    plt.show()



def get_years(normalized_dataframe):
    to_flatten = pd.DataFrame(normalized_dataframe.year.unique()).values.tolist()
    years = []
    for elem in to_flatten:
        years.append(elem[0])
    return years


dir_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\"
#dir_path = "/home/jean-baptiste/Travail/5A/Projet/facebook-loicgarnier104/messages/inbox/"
result = all_directories_timestamp_messages_parser(dir_path)
result = sorted(result)
result = convert_timestamp_list_to_timestamp_date(result)
df = normalize_dataframe(result)

print(get_years(df))
#df = test_dataframe()
#print(df)
#print(df.dtypes)
#show_messages_per_interval(df, primary_interval="weekday", secondary_interval="")
#mega_function(data=df, primary_interval="weekday", secondary_interval="month", global_interval="")

#df['hour'].plot.hist(bins=24, edgecolor='black')
#data_between_dates = select_data_between_dates('01/01/2019', '01/02/2019', df)







##

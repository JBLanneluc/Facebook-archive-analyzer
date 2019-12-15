#import pandas as pd
import datetime
from path import Path
import os
import json
import time


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
def normalize_date(timestamp_list):
    normalized_list = []
    for timestamp in timestamp_list:
        date = timestamp.split(" ")[0]
        date = date.split("/")
        time = timestamp.split(" ")[1]
        time = time.split(":")

        """
        # si on fait un dico
        day = date[0]
        month = date[1]
        year = date[2]
        hour = time[0]
        minute = time[1]
        second = time[2]
        """

        normalized_list.append(date + time)

    return normalized_list




def sort_by_year(timestamp_list):
    years_dictionnary = {}
    current_year = int(timestamp_list[0][2])
    current_list = []

    for k in range(len(timestamp_list)):
        if (int(timestamp_list[k][2]) == current_year):
            current_list.append(timestamp_list[k])

        if (k+1 < len(timestamp_list)):
            if (int(timestamp_list[k+1][2]) == current_year + 1):
                if current_year in years_dictionnary:
                    years_dictionnary[current_year] = years_dictionnary[current_year] + current_list
                else:
                    years_dictionnary[current_year] = current_list

                current_list = []
                current_year = current_year + 1

    if current_year in years_dictionnary:
        years_dictionnary[current_year] = years_dictionnary[current_year] + current_list
    else:
        years_dictionnary[current_year] = current_list

    return years_dictionnary










def sort_by_month(timestamp_list):
    months_dictionnary = {}
    current_month = int(timestamp_list[0][1])
    current_list = []

    for k in range(len(timestamp_list)):
        if (int(timestamp_list[k][1]) == current_month):
            current_list.append(timestamp_list[k])

        if (k+1 < len(timestamp_list)):
            if (int(timestamp_list[k+1][1]) == current_month + 1):
                if current_month in months_dictionnary:
                    months_dictionnary[convert_month_number_to_name(current_month)] = months_dictionnary[convert_month_number_to_name(current_month)] + current_list
                else:
                    months_dictionnary[convert_month_number_to_name(current_month)] = current_list
                current_list = []
                current_month = current_month + 1

    if current_month in months_dictionnary:
        months_dictionnary[convert_month_number_to_name(current_month)] = months_dictionnary[convert_month_number_to_name(current_month)] + current_list
    else:
        months_dictionnary[convert_month_number_to_name(current_month)] = current_list

    return months_dictionnary

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


def sort_by_weekday(timestamp_list):
    weekdays_dictionnary = {}
    current_weekday = convert_date_to_weekday_number("%s/%s/%s"%(timestamp_list[0][0], timestamp_list[0][1], timestamp_list[0][2]))
    #weekday_number = convert_date_to_weekday_number(date)
    #date[0] = weekday_number
    current_list = []

    for k in range(len(timestamp_list)):
        if (convert_date_to_weekday_number("%s/%s/%s"%(timestamp_list[k][0], timestamp_list[k][1], timestamp_list[k][2])) == current_weekday):
            current_list.append(timestamp_list[k])

        if (k+1 < len(timestamp_list)):
            if (convert_date_to_weekday_number("%s/%s/%s"%(timestamp_list[k+1][0], timestamp_list[k+1][1], timestamp_list[k+1][2])) == current_weekday + 1):
                if current_weekday in weekdays_dictionnary:
                    weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] = weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] + current_list
                else:
                    weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] = current_list

                current_list = []
                current_weekday = (current_weekday + 1) % 7

    if current_weekday in weekdays_dictionnary:
        weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] = weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] + current_list
    else:
        weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] = current_list

    return weekdays_dictionnary


def sort_by_hour(timestamp_list):
    hours_dictionnary = {}
    if (timestamp_list == []):
        return hours_dictionnary

    current_hour = int(timestamp_list[0][3])
    current_list = []

    for k in range(len(timestamp_list)):
        if (int(timestamp_list[k][3]) == current_hour):
            current_list.append(timestamp_list[k])

        if (k+1 < len(timestamp_list)):
            if (int(timestamp_list[k+1][3]) == current_hour + 1):
                if current_hour in hours_dictionnary:
                    hours_dictionnary[current_hour] = hours_dictionnary[current_hour] + current_list
                else:
                    hours_dictionnary[current_hour] = current_list

                current_list = []
                current_hour = current_hour + 1

    if current_hour in hours_dictionnary:
        hours_dictionnary[current_hour] = hours_dictionnary[current_hour] + current_list
    else:
        hours_dictionnary[current_hour] = current_list

    return hours_dictionnary




"""
for key, value in result.items():
    print("\n\ncurrent year = %s\n\n"%key)
    print("\n\ntimestamps = %s\n\n"%value[0])
    result[key] = sort_by_month(value)

print("\n\n\n\n\n\n\n\n\n\nBIG CHANGE\n\n\n\n\n\n\n\n\n\n\n")

for key, value in result.items():
    print("\n\ncurrent year = %s\n\n"%key)
    for key2, value2 in value.items():
        print("\n\ncurrent month = %s\n\n"%key2)
        print("\n\ntimestamps = %s\n\n"%value2[0])

"""


def sort_by_everything_in_a_dictionary(normalized_timestamp_list):
    sorted_timestamp_dict = sort_by_year(normalized_timestamp_list)

    for year, year_timestamp_list in sorted_timestamp_dict.items():
        sorted_timestamp_dict[year] = sort_by_month(year_timestamp_list)

    """
    for year, year_timestamp_list in sorted_timestamp_dict.items():
        for month, month_timestamp_list in sorted_timestamp_dict[year].items():
            sorted_timestamp_dict[year][month] = sort_by_hour(month_timestamp_list)
    """
    for year, year_timestamp_list in sorted_timestamp_dict.items():
        for month, month_timestamp_list in sorted_timestamp_dict[year].items():
            sorted_timestamp_dict[year][month] = sort_by_weekday(month_timestamp_list)

    for year, year_timestamp_list in sorted_timestamp_dict.items():
        for month, month_timestamp_list in sorted_timestamp_dict[year].items():
            for weekday, weekday_timestamp_list in sorted_timestamp_dict[year][month].items():
                sorted_timestamp_dict[year][month][weekday] = sort_by_hour(weekday_timestamp_list)

    # just for printing
    print("\n\n\n\n\nHour parsing\n\n\n")
    for year, year_timestamp_list in sorted_timestamp_dict.items():
        print("\n\nYear = %s\n"%year)
        for month, month_timestamp_list in sorted_timestamp_dict[year].items():
            print("Month = %s"%month)
            for weekday, weekday_timestamp_list in sorted_timestamp_dict[year][month].items():
                print("Weekday = %s"%weekday)
                for hour, hour_timestamp_list in sorted_timestamp_dict[year][month][weekday].items():
                    print("Hour = %s"%hour)
                    for timestamp in hour_timestamp_list:
                        print(timestamp)
                    #time.sleep(1)



    return sorted_timestamp_dict







def count_number_of_messages_per_hour(sorted_timestamp_dict):
    count_timestamp_dict = {}

    for year, year_timestamp_list in sorted_timestamp_dict.items(): #timestamp dict plutot

        month_dict = {}
        for month, month_timestamp_list in sorted_timestamp_dict[year].items(): #timestamp dict plutot

            hour_dict = {}
            for hour, hour_timestamp_list in sorted_timestamp_dict[year][month].items():
                hour_dict[hour] = len(hour_timestamp_list)

            month_dict[month] = hour_dict

        count_timestamp_dict[year] = month_dict


    return count_timestamp_dict


def average_number_of_messages_per_hour_by_year(sorted_count_dict):
    sorted_average_dict = {}

    for year, year_count_dict in sorted_count_dict.items():

        hour_dict = {}
        #m = 0 #fonctionne pas parce que mois utilises differents selon les heures
        for month, month_count_dict in sorted_count_dict[year].items():
            for hour, hour_count in sorted_count_dict[year][month].items(): #hourly_count plutot
                if hour in hour_dict:
                    hour_dict[hour] = [hour_dict[hour][0] + hour_count, hour_dict[hour][1] + 1]
                else:
                    hour_dict[hour] = [hour_count, 1]

        for hour, hour_count in hour_dict.items():
            hour_dict[hour] = round(hour_dict[hour][0] / hour_dict[hour][1])

        sorted_average_dict[year] = hour_dict

    return sorted_average_dict

def total_number_of_messages_per_hour_by_year(sorted_count_dict):
    sorted_total_dict = {}

    for year, year_count_dict in sorted_count_dict.items():

        hour_dict = {}
        #m = 0 #fonctionne pas parce que mois utilises differents selon les heures
        for month, month_count_dict in sorted_count_dict[year].items():
            for hour, hour_count in sorted_count_dict[year][month].items(): #hourly_count plutot
                if hour in hour_dict:
                    hour_dict[hour] = hour_dict[hour] + hour_count
                else:
                    hour_dict[hour] = hour_count


        sorted_total_dict[year] = hour_dict

    return sorted_total_dict


def average_number_of_messages_per_day_by_year(sorted_average_dict): # celui de la fonction average_number_of_messages_per_hour_by_year => non du tout sinon j'ai jjuste des moyennes et pas de total, il faut le resultat de la fonction total_number_of_messages_per_hour_by_year
    sorted_average_per_year_dict = {}

    for year, year_count_dict in sorted_average_dict.items():
        for hour, hour_count in sorted_average_dict[year].items(): #hourly_count plutot
            if year in sorted_average_per_year_dict:
                sorted_average_per_year_dict[year] = [sorted_average_per_year_dict[year][0] + hour_count, sorted_average_per_year_dict[year][1] + 1]
            else:
                sorted_average_per_year_dict[year] = [hour_count, 1]

    for year, year_count in sorted_average_per_year_dict.items():
        sorted_average_per_year_dict[year] = round(sorted_average_per_year_dict[year][0] / sorted_average_per_year_dict[year][1])

    return sorted_average_per_year_dict





# a coder pour avoir lundi mardi mercredi jeudi vendredi samedi dimanche

#def convert_every_date_list_to_weekdays(timestamp_list):
#    pass












dir_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\"
result = all_directories_timestamp_messages_parser(dir_path)
result = sorted(result)
result = convert_timestamp_list_to_timestamp_date(result)
result = normalize_date(result)
result = sort_by_everything_in_a_dictionary(result)




"""
result = count_number_of_messages_per_hour(result)
result[2011]["Fevrier"][20] = 4
result[2011]["Mars"][8] = 40
result = total_number_of_messages_per_hour_by_year(result) # a checker
#result = average_number_of_messages_per_day_by_year(result) # a checker

# lister et ordonner les calculs necessaires et nommer corrrectement les fonctions associees

for year in result:
    if (year == 2011):
        print("\n\nyear = %s"%year)
        print(result[year])
    else:
        #print("\n\nyear = %s"%year)
        #print(result[year])
        pass
"""













##

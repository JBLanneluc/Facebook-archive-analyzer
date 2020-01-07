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

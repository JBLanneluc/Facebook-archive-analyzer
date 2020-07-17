from main import *


def show_messages_per_interval(data, primary_interval, secondary_interval):
    bins_dictionnary = {"hour": 24, "weekday": 7, "month": 12, "second": 60, "minute": 60}  # trouver le nombre d
    # annees et le stocker pour le mettre dans le dico
    primary_interval = primary_interval.lower()
    primary_name = primary_interval  # .capitalize()
    primary_number = bins_dictionnary[primary_interval]

    if primary_interval == "weekday":
        data[primary_interval].value_counts().hist(bins=24, edgecolor="black")
        # fig, ax = plt.subplots()
        weekday_names = "Lundi Mardi Mercredi Jeudi Vendredi Samedi Dimanche".split(' ')
        plt.xticks([0, 0.5, 1, 2, 3, 4, 5], weekday_names)
        # ax.set_xticklabels(weekday_names)
        # ax.set_xticks(range(0, len(weekday_names)))
        # ax.plot()
    elif primary_interval == "month":
        data[primary_interval].value_counts().hist(bins=24, edgecolor="black")
        month_names = "Janvier Fevrier Mars Avril Mai Juin Juillet Aout Septembre Octobre Novembre Decembre".split(' ')
        # ax.set_xticklabels(month_names)
        # ax.set_xticks(range(0, len(month_names)))
    else:
        data[primary_interval].plot.hist(bins=24, edgecolor="black")

    plt.xlabel("Per " + primary_name)
    plt.ylabel("Average number of messages")
    plt.show()


def mega_function(data, primary_interval, secondary_interval, global_interval):
    percentage = False
    # primary_interval="weekday", secondary_interval="month"
    if percentage == True:
        summary = pd.DataFrame(data.groupby([secondary_interval])[
                                   primary_interval].value_counts())  # fonctionne mais pas la moyenne et legende a
        # changer
        sum = data.groupby([secondary_interval])[primary_interval].count()
        summary = pd.DataFrame(data.groupby([secondary_interval])[primary_interval].value_counts() / sum * 100)
        # print(summary)
    else:
        summary = pd.DataFrame(data.groupby([secondary_interval])[
                                   primary_interval].value_counts())  # fonctionne mais pas la moyenne et legende a
        # changer
        sum = data.groupby([secondary_interval])[primary_interval].count()
        summary = pd.DataFrame(data.groupby([secondary_interval])[primary_interval].value_counts() / sum * 100)
        # print(summary)

    """
    if percentage == True:
        summary = pd.DataFrame(data.groupby(["year"])["weekday"].value_counts()) # fonctionne mais pas la moyenne et 
        # legende a changer
        sum = data.groupby(["year"])["weekday"].count()
        summary = pd.DataFrame(data.groupby(["year"])["weekday"].value_counts() / sum * 100)
        print(summary)
    else:
        summary = pd.DataFrame(data.groupby(["year"])["weekday"].value_counts()) # fonctionne mais pas la moyenne et 
        # legende a changer
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
    months = (
    "Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre",
    "Decembre")
    hours = [5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4]
    dict = {"weekday": weekdays, "month": months, "hour": hours}
    if primary_interval == "weekday" or primary_interval == "month" or primary_interval == "hour":
        # print(dict[secondary_interval])
        # print(dict[primary_interval])

        summary = summary.reindex(index=["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"])
        print("\n\n\n\n\n")
        print(summary)
        print("\n\n\n\n\n")
        print("\n\nerror ?\n\n\n")
        summary = summary.reindex(columns=(
        "month", "Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre",
        "Novembre", "Decembre"))
        print("\n\n\n\n\n")
        print(summary)
        print("\n\n\n\n\n")
        # summary = summary[dict["month"]]
        # summary = summary.unstack(level=0)

        # summary = summary.reindex(months, axis=(1))

        # summary = summary.reindex(dict[secondary_interval])

    # print(summary)
    # summary = summary.reindex(weekdays)
    # summary.plot(kind='line', subplots=False)
    summary.plot(kind='bar', subplots=False)
    plt.legend(loc="upper right")

    plt.xlabel("Jour de la semaine")  #
    plt.ylabel("Pourcentage de messages envoyes")
    plt.title("Pourcentage de messages envoyes par jour de la semaine selon les annees")  #
    plt.tight_layout()
    plt.show()


def sort_by_year(timestamp_list):
    years_dictionnary = {}
    current_year = int(timestamp_list[0][2])
    current_list = []

    for k in range(len(timestamp_list)):
        if (int(timestamp_list[k][2]) == current_year):
            current_list.append(timestamp_list[k])

        if (k + 1 < len(timestamp_list)):
            if (int(timestamp_list[k + 1][2]) == current_year + 1):
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
        if int(timestamp_list[k][1]) == current_month:
            current_list.append(timestamp_list[k])

        if k + 1 < len(timestamp_list):
            if int(timestamp_list[k + 1][1]) == current_month + 1:
                if current_month in months_dictionnary:
                    months_dictionnary[convert_month_number_to_name(current_month)] = months_dictionnary[
                                                                                          convert_month_number_to_name(
                                                                                              current_month)] + \
                                                                                      current_list
                else:
                    months_dictionnary[convert_month_number_to_name(current_month)] = current_list
                current_list = []
                current_month = current_month + 1

    if current_month in months_dictionnary:
        months_dictionnary[convert_month_number_to_name(current_month)] = \
            months_dictionnary[convert_month_number_to_name( current_month)] + current_list
    else:
        months_dictionnary[convert_month_number_to_name(current_month)] = current_list

    return months_dictionnary


def sort_by_weekday(timestamp_list):
    weekdays_dictionnary = {}
    current_weekday = convert_date_to_weekday_number(
        "%s/%s/%s" % (timestamp_list[0][0], timestamp_list[0][1], timestamp_list[0][2]))
    # weekday_number = convert_date_to_weekday_number(date)
    # date[0] = weekday_number
    current_list = []

    for k in range(len(timestamp_list)):
        if (convert_date_to_weekday_number(
                "%s/%s/%s" % (timestamp_list[k][0], timestamp_list[k][1], timestamp_list[k][2])) == current_weekday):
            current_list.append(timestamp_list[k])

        if (k + 1 < len(timestamp_list)):
            if (convert_date_to_weekday_number("%s/%s/%s" % (
            timestamp_list[k + 1][0], timestamp_list[k + 1][1], timestamp_list[k + 1][2])) == current_weekday + 1):
                if current_weekday in weekdays_dictionnary:
                    weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] = \
                        weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] + current_list
                else:
                    weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] = current_list

                current_list = []
                current_weekday = (current_weekday + 1) % 7

    if current_weekday in weekdays_dictionnary:
        weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] = weekdays_dictionnary[
                                                                                    convert_weekday_number_to_name(
                                                                                        current_weekday)] + current_list
    else:
        weekdays_dictionnary[convert_weekday_number_to_name(current_weekday)] = current_list

    return weekdays_dictionnary


def sort_by_hour(timestamp_list):
    hours_dictionnary = {}
    if not timestamp_list:
        return hours_dictionnary

    current_hour = int(timestamp_list[0][3])
    current_list = []

    for k in range(len(timestamp_list)):
        if int(timestamp_list[k][3]) == current_hour:
            current_list.append(timestamp_list[k])

        if k + 1 < len(timestamp_list):
            if int(timestamp_list[k + 1][3]) == current_hour + 1:
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
        print("\n\nYear = %s\n" % year)
        for month, month_timestamp_list in sorted_timestamp_dict[year].items():
            print("Month = %s" % month)
            for weekday, weekday_timestamp_list in sorted_timestamp_dict[year][month].items():
                print("Weekday = %s" % weekday)
                for hour, hour_timestamp_list in sorted_timestamp_dict[year][month][weekday].items():
                    print("Hour = %s" % hour)
                    for timestamp in hour_timestamp_list:
                        print(timestamp)
                    # time.sleep(1)

    return sorted_timestamp_dict


def count_number_of_messages_per_hour(sorted_timestamp_dict):
    count_timestamp_dict = {}

    for year, year_timestamp_list in sorted_timestamp_dict.items():  # timestamp dict plutot

        month_dict = {}
        for month, month_timestamp_list in sorted_timestamp_dict[year].items():  # timestamp dict plutot

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
        # m = 0 #fonctionne pas parce que mois utilises differents selon les heures
        for month, month_count_dict in sorted_count_dict[year].items():
            for hour, hour_count in sorted_count_dict[year][month].items():  # hourly_count plutot
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
        # m = 0 #fonctionne pas parce que mois utilises differents selon les heures
        for month, month_count_dict in sorted_count_dict[year].items():
            for hour, hour_count in sorted_count_dict[year][month].items():  # hourly_count plutot
                if hour in hour_dict:
                    hour_dict[hour] = hour_dict[hour] + hour_count
                else:
                    hour_dict[hour] = hour_count

        sorted_total_dict[year] = hour_dict

    return sorted_total_dict


def average_number_of_messages_per_day_by_year(
        sorted_average_dict):  # celui de la fonction average_number_of_messages_per_hour_by_year => non du tout
    # sinon j'ai jjuste des moyennes et pas de total, il faut le resultat de la fonction
    # total_number_of_messages_per_hour_by_year
    sorted_average_per_year_dict = {}

    for year, year_count_dict in sorted_average_dict.items():
        for hour, hour_count in sorted_average_dict[year].items():  # hourly_count plutot
            if year in sorted_average_per_year_dict:
                sorted_average_per_year_dict[year] = [sorted_average_per_year_dict[year][0] + hour_count,
                                                      sorted_average_per_year_dict[year][1] + 1]
            else:
                sorted_average_per_year_dict[year] = [hour_count, 1]

    for year, year_count in sorted_average_per_year_dict.items():
        sorted_average_per_year_dict[year] = round(
            sorted_average_per_year_dict[year][0] / sorted_average_per_year_dict[year][1])

    return sorted_average_per_year_dict

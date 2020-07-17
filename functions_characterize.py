import json
from functions_main import *


def extract_characterizing_categories(clean_text):
    dict_lists = {
        "use_of_tutoiement_list": use_of_tutoiement_list,
        "informal_speech_list": informal_speech_list,
        "smiley_faces_list": smiley_faces_list,
        "sms_language_list": sms_language_list,
        "friends_list": friends_list,
        "vulgar_speech_list": vulgar_speech_list,

        "calls_together_list": calls_together_list,
        "plans_together_list": plans_together_list,

        "empathy_words_list": empathy_words_list,
        "deep_stuff_list": deep_stuff_list,
        "talking_late_list": talking_late_list,
        "love_and_affection_list": love_and_affection_list,

        "flatmates_list": flatmates_list,
        "vegan_list": vegan_list,
        "in_class_together_list": in_class_together_list,
        "family_member_list": family_member_list,
        "student_list": student_list
    }
    dict_opposite_lists = {
        "family_member_list_opposite": family_member_list_opposite,
        "flatmates_list_opposite": flatmates_list_opposite
    }
    dict_results = {}
    modifiable_text = clean_text
    for key in dict_lists:
        # print("family_member_list_opposite")
        # print("\n\n\n\n")
        # print(key)
        # print("\n")

        key_opposite = key + "_opposite"
        modifiable_text_after_opposite = modifiable_text
        modifiable_text_after_tutoiement = modifiable_text
        if key_opposite in dict_opposite_lists:
            dict_results[key_opposite] = 0
            for word in dict_opposite_lists[key_opposite]:
                while word in modifiable_text:
                    modifiable_text = modifiable_text.replace(word, " ", 1)  # si je les enleve ca fait de la merde
                    if word in family_member_list:
                        index = modifiable_text.find(word)
                        # print(modifiable_text[index-10:index+10]) #### important
                    if word in dict_opposite_lists[key_opposite]:
                        dict_results[key_opposite] += 1
                        # print("+1")
        modifiable_text = modifiable_text_after_opposite

        dict_results[key] = 0
        for word in dict_lists[key]:
            while word in modifiable_text:
                modifiable_text = modifiable_text.replace(word, " ", 1)  # si je les enleve ca fait de la merde
                if word in family_member_list:
                    # print("\n")
                    # print(key)
                    index = modifiable_text.find(word)
                    # print(modifiable_text[index-10:index+10])
                if word in dict_lists[key]:
                    dict_results[key] += 1
                    # print("+1")

        if key == "use_of_tutoiement_list":
            modifiable_text = modifiable_text_after_tutoiement

    for key in dict_lists:
        key_opposite = key + "_opposite"
        if key_opposite in dict_opposite_lists:
            # print(key_opposite)
            # print(dict_results[key])
            # print(dict_results[key_opposite])
            dict_results[key] -= dict_results[key_opposite]
            dict_results[key] = 0 if dict_results[key] < 0 else dict_results[key]
            # print(dict_results[key])
            del dict_results[key + "_opposite"]

    return dict_results


def characterize_with_weights(dict_results):
    coefs = {
        "use_of_tutoiement_list": 0.5,
        "informal_speech_list": 0.6,

        "smiley_faces_list": 1,
        "sms_language_list": 1,
        "vulgar_speech_list": 1,

        "friends_list": 0.7,
        "calls_together_list": 1,
        "plans_together_list": 2,
        "empathy_words_list": 2,
        "deep_stuff_list": 2,
        "talking_late_list": 2,
        "love_and_affection_list": 10
    }

    # degree_of_friendship = 100
    total_count = 0
    for key in coefs:
        total_count += dict_results[key]
    print("total_count = %s" % total_count)

    dict_percentages = {}
    for key in coefs:
        percentage = float("%.2f" % (dict_results[key] * 100 / total_count))
        dict_percentages[key] = percentage
        print("%s = %s" % (key, percentage))

    """if dict_results["use_of_tutoiement_list"] <= 100 and dict_results["informal_speech_list"] <= 50: # 
    caracteriser avec le nb total de messages envoyés / recus degree_of_friendship = degree_of_friendship * 0.5 

    if dict_results["smiley_faces_list"] <= 100 and dict_results["informal_speech_list"] <= 50: # caracteriser avec 
    le nb total de messages envoyés / recus degree_of_friendship = degree_of_friendship * 0.5 """

    degree_of_friendship = 0

    for key in coefs:
        degree_of_friendship += dict_results[key] * coefs[key] * 100 / total_count

    if dict_percentages["love_and_affection_list"] >= 1.2:  # caracteriser avec le nb total de messages envoyés / recus
        degree_of_friendship = degree_of_friendship * 1.2
    elif dict_percentages["love_and_affection_list"] >= 0.8:  # caracteriser avec le nb total de messages envoyés /
        # recus
        degree_of_friendship = degree_of_friendship * 1.1

    if dict_percentages["love_and_affection_list"] <= 0.2:  # caracteriser avec le nb total de messages envoyés / recus
        degree_of_friendship = degree_of_friendship * 0.6
    elif dict_percentages["love_and_affection_list"] <= 0.4:  # caracteriser avec le nb total de messages envoyés /
        # recus
        degree_of_friendship = degree_of_friendship * 0.7
    elif dict_percentages["love_and_affection_list"] <= 0.6:  # caracteriser avec le nb total de messages envoyés /
        # recus
        degree_of_friendship = degree_of_friendship * 0.8

    """
    number_of_messages = 100 # mettre la fonction qui le recupere
    if number_of_messages <= 200:
        degree_of_friendship = degree_of_friendship * 0.5
    """

    # en attendant le nb total de messages
    if total_count <= 200:
        degree_of_friendship = degree_of_friendship * 0.5
    if total_count <= 300:
        degree_of_friendship = degree_of_friendship * 0.6
    if total_count <= 400:
        degree_of_friendship = degree_of_friendship * 0.7
    if total_count <= 500:
        degree_of_friendship = degree_of_friendship * 0.8
    if total_count <= 600:
        degree_of_friendship = degree_of_friendship * 0.9

    # regarder la date du dernier message aussi !
    # regarder le nb de gens dans les mêmes groupes

    # degree_of_friendship = degree_of_friendship * 0.95
    degree_of_friendship = 99 if degree_of_friendship >= 99 else degree_of_friendship
    degree_of_friendship = round(degree_of_friendship)

    """
    use_of_tutoiement_list
    informal_speech_list

    smiley_faces_list
    sms_language_list

    friends_list
    vulgar_speech_list
    calls_together_list
    plans_together_list
    empathy_words_list
    deep_stuff_list
    talking_late_list
    love_and_affection_list
    """

    print("\n\nEstimated probability of friendship = %s%%" % degree_of_friendship)
    return degree_of_friendship


def palmares_of_people_in_groups_with_you(inbox_path):
    group_conversations_file_list = group_file_list(inbox_path)[1]
    # print(group_conversations_file_list)
    people_in_groups_with_you = {}
    # participants = []
    nb_of_groups = len(group_conversations_file_list)
    for group_conversation in group_conversations_file_list:
        with open(group_conversation) as json_data:
            participants = []
            data = json.load(json_data)
            # print(data["participants"])

            for key in data["participants"]:
                person_name = key["name"].encode('latin1').decode('utf-8-sig')

                if person_name in people_in_groups_with_you:
                    people_in_groups_with_you[person_name] += 1
                else:
                    people_in_groups_with_you[person_name] = 1

                # participants.append(key["name"].encode('latin1').decode('utf-8-sig'))

    if "Utilisateur de Facebook" in people_in_groups_with_you:
        del people_in_groups_with_you["Utilisateur de Facebook"]
    if "Loïc Garnier" in people_in_groups_with_you:
        del people_in_groups_with_you["Loïc Garnier"]

    for key, value in sorted(people_in_groups_with_you.items(), key=lambda x: x[1], reverse=True):
        # print(key)
        # if key[0] == "C":# and key[-1] == "y":
        #    print(key)
        if value >= 0:
            # print("%s\t%s" % (value, key))
            pass

    return [people_in_groups_with_you, nb_of_groups]


def get_total_number_of_messages(df_sent, df_received, n=-1):
    palmares_sent = df_sent['receiver'].value_counts()
    palmares_received = df_received['sender'].value_counts()
    if n == -1:
        palmares = palmares_received.add(palmares_sent, fill_value=0).sort_values().astype('int32')
        # print([name.encode('latin1').decode('utf-8-sig') for name in palmares.index.values.tolist()])

        # palmares = palmares.reindex([name.encode('latin1').decode('utf-8-sig') for name in
        # palmares.index.values.tolist()])

    elif n >= 0:
        palmares = palmares_received.add(palmares_sent, fill_value=0).sort_values().nlargest(n).astype(
            'int32').reset_index()
        palmares.columns = ['Nom', 'Nombre de messages']
        # palmares["Nom"] = palmares["Nom"].tolist().encode('latin1').decode('utf-8-sig')
        print("Palmares des", n, "utilisateurs avec lesquels vous avez échangé le plus de messages :\n", palmares)
    else:
        print("Erreur, mauvaise valeur entrée")
        return
    return palmares


def characterize_with_percentages_for_each_category(dict_results, person_name):
    # person_name = "Téo Frossard" ###
    # person_name_dir_version = ""
    # total_nb_of_messages = get_total_number_of_messages(df_sent, df_received)[person_name]
    total_nb_of_messages = get_total_number_of_messages(df_sent, df_received)[person_name]
    # print(df_sent)
    # print(df_received)

    inbox_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\"
    groups = palmares_of_people_in_groups_with_you(inbox_path)
    if person_name in groups[0]:
        dict_results["groups_together"] = groups[0][person_name] / groups[
            1] * 100  # gerer qq chose avec le pourcentage de groupes ds lequel t'es et le nb de la personne
    else:
        dict_results["groups_together"] = 0
    # print(dict_results["groups_together"])
    result_percentages = {}
    coefs = {
        "talking_late_list": 1,
        "student_list": 1,

        # informal
        "use_of_tutoiement_list": 1 / 15,
        "informal_speech_list": 1 / 8,
        "smiley_faces_list": 1 / 2,
        "sms_language_list": 1 / 2,
        "vulgar_speech_list": 1 / 3,
        "friends_list": 1 / 1.5,

        # in_class_together
        "in_class_together_list": 120,

        # flatmates
        "flatmates_list": 15,

        # activities_together
        "groups_together": 2,
        "plans_together_list": 3,
        "calls_together_list": 1,

        # love_and_affection
        "love_and_affection_list": 3.5,
        "deep_stuff_list": 1.8,
        "empathy_words_list": 1.2,

        # vegan
        "vegan_list": 12,

        # family_member
        "family_member_list": 6,

    }
    categories = {
        "activities_together": {"plans_together_list": coefs["plans_together_list"],
                                "calls_together_list": coefs["calls_together_list"],
                                "groups_together": coefs["groups_together"]},
        "love_and_affection": {"love_and_affection_list": coefs["love_and_affection_list"],
                               "empathy_words_list": coefs["empathy_words_list"],
                               "deep_stuff_list": coefs["deep_stuff_list"]},
        "vegan": {"vegan_list": coefs["vegan_list"]},
        "flatmates": {"flatmates_list": coefs["flatmates_list"]},
        "in_class_together": {"in_class_together_list": coefs["in_class_together_list"]},
        "informal": {"use_of_tutoiement_list": coefs["use_of_tutoiement_list"],
                     "informal_speech_list": coefs["informal_speech_list"],
                     "smiley_faces_list": coefs["smiley_faces_list"], "sms_language_list": coefs["sms_language_list"],
                     "vulgar_speech_list": coefs["vulgar_speech_list"], "friends_list": coefs["friends_list"]},
        "family_member": {"family_member_list": coefs["family_member_list"]}
    }

    for category in categories:
        proportion = 0
        small_dict_of_lists = categories[category]
        for listing in small_dict_of_lists:
            coef = small_dict_of_lists[listing]
            if listing == "groups_together":
                proportion += coef * dict_results[listing]
            else:
                proportion += coef * dict_results[listing] / total_nb_of_messages * 1000
        # result_percentages[category] = float("%.2f"%proportion)
        result_percentages[category] = int(proportion)

    for key in result_percentages:
        result_percentages[key] = 95 if result_percentages[key] >= 95 else result_percentages[key]
        result_percentages[key] = 5 if result_percentages[key] <= 5 else result_percentages[key]

    # float("%.2f"%(dict_results[key] * 100 / total_count))
    dict_to_print = {
        "activities_together": "de chances que vous ayez fait des activités ensemble.\n",
        "love_and_affection": "de chances que vous exprimiez de l'affection dans vos conversation.\n",
        "vegan": "de chances qu'au moins l'un des participants de la conversation soi végétarien ou végan.\n",
        "flatmates": "de chances que vous ayez vécu en colocation.\n",
        "in_class_together": "de chances que vous soyez ou ayez été en cours ensemble.\n",
        "informal": "de chances que vous ayez une relation informelle.\n",
        "family_member": "de chances que vous fassiez partie de la même famille.\n"
    }

    for key, value in sorted(result_percentages.items(), key=lambda x: x[1], reverse=True):
        print("%s %%\t\t%s" % (value, dict_to_print[key]))

    return result_percentages


# inbox_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\"
# palmares_of_people_in_groups_with_you(inbox_path)


global flatmates_list
flatmates_list = [
    "coloc",
    "le loyer",
    "payer",
    "proprio",
    "proprio",
    "propriétaire",
    "caf",
    "les charges",
    "électricité",
    # "eau",
    # "gaz",
    "facture"
]

global flatmates_list_opposite
flatmates_list_opposite = [
    "bien la coloc",
    "la coloc de",

    "es en coloc",
    "suis en coloc",

    "mon coloc",
    "ma coloc",
    "mes coloc",
    "ton coloc",
    "ta coloc",
    "tes coloc",

    "ton proprio",
    "ta proprio",

    "mon proprio",
    "ma proprio"
]

global vegan_list
vegan_list = [
    'végan',
    "vegan",
    "végan",
    "végé",
    "végétarien",
    "vegan",
    "viande",
    "tofu",
    "seitan",
    "soja",
    "levure maltée"
]

global in_class_together_list
in_class_together_list = [
    "on a cours de quoi",
    "tu viens en cours",
    "le prof",
    "la prof",
    "t'as révisé"
]

global family_member_list
family_member_list = [
    "papi",
    "mamie",
    "maman",
    "papa"
]

global family_member_list_opposite
family_member_list_opposite = [
    "papie",
    "papil"
    "ma maman",
    "mon papa",
    "ta maman",
    "ton papa",
    "sa maman",
    "son papa",

    "ma mamie",
    "mon papi",
    "ta mamie",
    "ton papi",
    "sa mamie",
    "son papi",

    "un papi",
    "une mamie",
    "des papis",
    "des mamies",
    # "papillons"
]

global student_list
student_list = [
    "je suis en erasmus",
    "je pars en erasmus",
    "je vais en erasmus",
    "je vais en échange",
    "je suis en échange",
    "au partiel",
    "aux partiels",
    "exam"
]

# 1
global use_of_tutoiement_list
use_of_tutoiement_list = [
    "t'",
    "toi",
    "tu",
    "ton"
]

# 2
global informal_speech_list
informal_speech_list = [
    "hey",
    "j'suis",
    "jsuis",
    "j'sais",
    "j'me",
    "j'vais",
    'd’acc',
    "d'acc",
    "hmm",
    "hein",
    "ouaip",
    "pk",
    "pck",
    "bah",
    "ouais",
    "okay",
    "cool",
    "nice",
    "oh",
    "tkt",
    "mec",
    "meuf",
    "dsl",
    "genre",
    "grave",
    "ya",
    "euh",
    "ben",
    'perso',
    'qqun',
    "super",
    "hyper",
    "truc",
    "trucs"
]

# 3
global smiley_faces_list
smiley_faces_list = [
    ":)",
    ";)",
    ":(",
    ":D",
    "x)",
    "xd",
    "xD",
    ":p",
    ":3",
    "=)",
    "=D",
    "<3",
    ":*"
]

# 4
global sms_language_list
sms_language_list = [
    'mdr',
    'ptdr',
    'lol',
    "lmfao",
    "lmao",
    "wtf",
    "dsl"
]

# 5
global friends_list
friends_list = [
    "dodo",
    "marrant",
    "drôle",
    'rire',
    "t'inquiète",
    "wesh",
    "yo",
    "pote",
    "bro",  #
    "ahah",
    "haha",
    "damn",
    "putain",
    "merde",
    "fuck",
    'content',
    'ohhh',
    'sorry',
    'promis'
]

# 6
global vulgar_speech_list
vulgar_speech_list = [
    "un enculé",
    "une enculé",
    "un connard",
    "une pute",
    "une sale pute",
    "une connasse",
    "une salope"
    "quelle connasse",
    "quel connard",
    "quelle pute",
    "quelle salope"
]

# 7
global calls_together_list
calls_together_list = [
    "on s'appelle",
    "tu m'as appelé",
    "appelle moi",
    "skype",
    "appel vidéo",
    "discord",
    "whatsapp"
]

# 8
global plans_together_list
plans_together_list = [
    "tiens au jus",
    "tiens moi au jus",
    "tiens au courant",
    "tiens moi au courant",

    "la semaine prochaine",
    "soirée chez moi"
    "soiree chez moi"
    "soirée",
    "soiree",
    "es chaud",
    "suis chaud",
    "inté",
    "wei",
    "ce soir",

    "tu fais quoi ce",
    "tu fais quoi demain",
    "tu fais quoi pendant",
    "tu fais quoi samedi",
    "tu fais quoi dimanche",
    "tu fais quoi lundi",
    "tu fais quoi mardi",
    "tu fais quoi mercredi",
    "tu fais quoi jeudi",
    "tu fais quoi vendredi",
    "tu fais quoi l",

    "t'es là lundi",
    "t'es là mardi",
    "t'es là mercredi",
    "t'es là jeudi",
    "t'es là vendredi",
    "t'es là samedi",
    "t'es là dimanche",
    "t'es là pendant",
    "t'es là ce",
    "t'es là demain",
    "t'es là l",

    "tu es là lundi",
    "tu es là mardi",
    "tu es là mercredi",
    "tu es là jeudi",
    "tu es là vendredi",
    "tu es là samedi",
    "tu es là dimanche",
    "tu es là pendant",
    "tu es là ce",
    "tu es là demain",
    "tu es là l",

    "ce week-end",
    "ce week end",
    'ce weekend',
    # 'weekend',
    # "week-end",
    # "week end",
    "demain soir",
    "vendredi soir",
    "ce soir",
    "samedi soir",
    "jeudi soir",
    "demain",
    "ça serait sympa",
    "habites où",
    "habites ou",
    "où chez toi",
    "ou chez toi",
    "quoi ton adresse",
    "je suis là",
    "je suis en bas",
    "je suis devant",
    "tu peux m'ouvrir",
    "viens chez moi"
]

# 9
global empathy_words_list
empathy_words_list = [
    "je comprends",
    "je suis désolée",
    "je suis désolé",
    "j'espère pour toi",
    "profite bien",
    'courage'
]

# 9
global deep_stuff_list
deep_stuff_list = [
    "j'ai peur",
    "tu as peur",
    "t'as peur",
    "relation",
    "couple",
    "copain",
    "copine",
    "problème",
    "confiance en soi",
    "confiance en moi",
    "confiance en toi"
    'triste',
    "me sens seul"
]

# 10
global talking_late_list
talking_late_list = [
    'bonne nuit',
    "je vais dormir",
    "je vais dodo"
]

# 11
global love_and_affection_list
love_and_affection_list = [
    "je t'aime",
    "je t'adore",
    "tu m'as manqué",
    "tu me manques",
    "te voir",
    "se voir",
    "t'es beau",
    "t'es belle",
    "t'es parfaite",
    "t'es parfait",
    "tu es parfaite",
    "tu es parfait",
    "t'es drôle",
    "tu me faire rire"
    "toi et moi",
    "bébé"
]

global shallow_hello_words_list
shallow_hello_words_list = [
    "salut",
    "ça va",
    "tu vas bien",
    "ça va et toi",
    "super et toi",
    "très bien et toi"
]

global not_very_relevant_list
not_very_relevant_list = [
    "désolée",
    "désolé",
    "merci",
    "viens",
    "mode",
    "jouer",
    'gentil',
    "gros",
    'je vais manger',
    'vivre',
    "parents",
    'mère',
    "père",
    "ami",
    'amis',
    "vacances",
    "photo",
    'projets',
    'projet',
]

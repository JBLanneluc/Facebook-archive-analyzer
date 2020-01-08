
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
        #print("family_member_list_opposite")
        #print("\n\n\n\n")
        #print(key)
        #print("\n")

        key_opposite = key + "_opposite"
        modifiable_text_after_opposite = modifiable_text
        if key_opposite in dict_opposite_lists:
            dict_results[key_opposite] = 0
            for word in dict_opposite_lists[key_opposite]:
                while word in modifiable_text:
                    modifiable_text = modifiable_text.replace(word, " ", 1) #si je les enleve ca fait de la merde
                    if word in family_member_list:
                        index = modifiable_text.find(word)
                        #print(modifiable_text[index-10:index+10]) #### important
                    if word in dict_opposite_lists[key_opposite]:
                        dict_results[key_opposite] += 1
                        #print("+1")
        modifiable_text = modifiable_text_after_opposite

        dict_results[key] = 0
        for word in dict_lists[key]:
            while word in modifiable_text:
                modifiable_text = modifiable_text.replace(word, " ", 1) #si je les enleve ca fait de la merde
                if word in family_member_list:
                    #print("\n")
                    #print(key)
                    index = modifiable_text.find(word)
                    #print(modifiable_text[index-10:index+10])
                if word in dict_lists[key]:
                    dict_results[key] += 1
                    #print("+1")




    """
    voir si on peut pas compter en mode enlever les occurrences des mots qui correspondraient pas, genre ici family_member :
    une liste papi mamie
    et on enlève les occurrences de la liste family_member_list_opposite
    """
    for key in dict_lists:
        key_opposite = key + "_opposite"
        if key_opposite in dict_opposite_lists:
            #print(key_opposite)
            #print(dict_results[key])
            #print(dict_results[key_opposite])
            dict_results[key] -= dict_results[key_opposite]
            dict_results[key] = 0 if dict_results[key] < 0 else dict_results[key]
            #print(dict_results[key])
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

    #degree_of_friendship = 100
    total_count = 0
    for key in coefs:
        total_count += dict_results[key]
    print ("total_count = %s"%total_count)

    dict_percentages = {}
    for key in coefs:
        percentage = float("%.2f"%(dict_results[key] * 100 / total_count))
        dict_percentages[key] = percentage
        print ("%s = %s"%(key, percentage))



    """
    if dict_results["use_of_tutoiement_list"] <= 100 and dict_results["informal_speech_list"] <= 50: # caracteriser avec le nb total de messages envoyés / recus
        degree_of_friendship = degree_of_friendship * 0.5

    if dict_results["smiley_faces_list"] <= 100 and dict_results["informal_speech_list"] <= 50: # caracteriser avec le nb total de messages envoyés / recus
        degree_of_friendship = degree_of_friendship * 0.5
    """



    degree_of_friendship = 0

    for key in coefs:
        degree_of_friendship += dict_results[key] * coefs[key] * 100 / total_count



    if dict_percentages["love_and_affection_list"] >= 1.2: # caracteriser avec le nb total de messages envoyés / recus
        degree_of_friendship = degree_of_friendship * 1.2
    elif dict_percentages["love_and_affection_list"] >= 0.8: # caracteriser avec le nb total de messages envoyés / recus
        degree_of_friendship = degree_of_friendship * 1.1

    if dict_percentages["love_and_affection_list"] <= 0.2: # caracteriser avec le nb total de messages envoyés / recus
        degree_of_friendship = degree_of_friendship * 0.6
    elif dict_percentages["love_and_affection_list"] <= 0.4: # caracteriser avec le nb total de messages envoyés / recus
        degree_of_friendship = degree_of_friendship * 0.7
    elif dict_percentages["love_and_affection_list"] <= 0.6: # caracteriser avec le nb total de messages envoyés / recus
        degree_of_friendship = degree_of_friendship * 0.8

    """
    number_of_messages = 100 # mettre la fonction qui le recupere
    if number_of_messages <= 200:
        degree_of_friendship = degree_of_friendship * 0.5
    """

    #en attendant le nb total de messages
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

    #degree_of_friendship = degree_of_friendship * 0.95
    degree_of_friendship = 98 if degree_of_friendship >= 98 else degree_of_friendship
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

    print("\n\nEstimated probability of friendship = %s%%"%degree_of_friendship)
    return degree_of_friendship




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
#"eau",
#"gaz",
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
"viande",
"tofu",
"vegan",
"seitan"
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
#"papillons"
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






#1
global use_of_tutoiement_list
use_of_tutoiement_list = [
"t'es",
"toi",
"tu",
"ton"
]

#2
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

#3
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
"=D"
]

#4
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


#5
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
"bro", #
"ahah",
"haha",
"damn",
"putain",
"merde",
"fuck",
'contente',
'ohhh',
'sorry',
'promis'
]

#6
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

#7
global calls_together_list
calls_together_list = [
"on s'appelle",
"tu m'as appelé",
"appelle moi",
"skype",
"appel vidéo",
"discord",
"sms",
"whatsapp"
]

#8
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
#'weekend',
#"week-end",
#"week end",
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

#9
global empathy_words_list
empathy_words_list = [
"je comprends",
"je suis désolée",
"je suis désolé",
"j'espère pour toi",
"profite bien",
'courage'
]

#9
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

#10
global talking_late_list
talking_late_list = [
'bonne nuit',
"je vais dormir",
"je vais dodo"
]

#11
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
"bébé",
"<3",
":*"
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

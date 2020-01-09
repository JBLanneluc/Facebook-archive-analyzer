from collections import Counter
from path import Path
import json
import codecs
import io #
import string

#Lien de word_cloud :
# http://www.sthda.com/french/wiki/text-mining-et-nuage-de-mots-avec-le-logiciel-r-5-etapes-simples-a-savoir

def internet_address_extractor(message):
    https = []
    #clean_message = message
    for k in range(len(message)):
        if message[k] == "h" and message[k+1] == "t" and message[k+2] == "t" and message[k+3] == "p":
            c = 0
            while message[k+c] != " ":
                c += 1
            https.append(message[k:k+c])
        if k+3 < len(message):
            break
            #clean_message.replace(message[k:k+c], " ")

            #print("\n%s\n"%message[k:k+c])

    clean_https = []

    for address in https:
        address = address.replace("http://www.", "")
        address = address.replace("https://www.", "")
        address = address.replace("http://m.", "")
        address = address.replace("https://m.", "")
        address = address.replace("http://fr.", "")
        address = address.replace("https://fr.", "")
        address = address.replace("http://ec.", "")
        address = address.replace("https://ec.", "")
        address = address.replace("http://", "")
        address = address.replace("https://", "")
        address = address.replace(".fr", "#")
        address = address.replace(".com", "#")
        address = address.replace("/", "#")
        address = list(filter(None, address.split("#")))
        clean_https.append(address[0])

    return [https, Counter(clean_https).most_common()]

def phone_number_extractor(message, https):

    for address in https:
        message = message.replace(address, " ", 1)

    numbers = []
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    k = 0
    while k+2 < len(message):

        if (message[k] == "+" and message[k+1] in digits and message[k+2] in digits) or (message[k] in digits and message[k+1] in digits):
            #print(message[k:k+20])
            c = 0
            n = 0
            nb = ""
            while n < 13 and c < 19 and k+c < len(message):
                if message[k+c] in ([" ", "-", ".", "+"] + digits):
                    if message[k+c] == "+":
                        if c==0:
                            nb += message[k+c]
                            n += 1
                        elif len(nb) >= 13:
                            numbers.append(nb)
                            break
                        else:
                            break
                    elif message[k+c] in digits:
                        nb += message[k+c]
                        n += 1
                    c += 1
                else:
                    break

                if nb == '+33627848766':
                    print("k = %s"%k)
                    print("c = %s"%c)
                    print("len = %s"%len(message))


                if len(nb) == 10 and nb[0] == "0" and nb[1] != "0":
                    numbers.append(nb)
                    break
                elif len(nb) == 12 and nb[0] == "+" and nb[1] != "0":
                    numbers.append(nb)
                    break
                elif len(nb) == 13 and nb[0] == "0" and nb[1] == "0":
                    numbers.append(nb)
                    break




            k += c-1
        else:
            k += 1

    return numbers






def text_cleaner1(message):
    #message = message.encode('latin1').decode('utf-8-sig')


    for char in ["\"", "-", "_", ".", ",", "!", "?", "[", "]", "{", "}", "\t", "\n"]: #"'", "(", ")", "/", ":", ";",
        message = message.replace(char, " ")
    message = message.lower()
    return message

def word_count(words_list):
    #words_list = clean_message.split()
    words_list = Counter(words_list).most_common()
    return words_list

global interessant_words
interessant_words = [
"je t'aime",
"je t'adore",
"tiens au jus",
"ça va",
"tu vas bien",
"tiens au courant",
"je comprends",
"appelle",
"t'inquiète",
"la semaine prochaine",
"je suis désolée",
"je suis désolé",
"désolée",
"désolé",
"merci",
"viens",
"mode",
"jouer",
"yo",
"soirées",
"soirée",
"soiree",
"gros",
"hmm",
"ouaip",
"con",
"connard",
"hein",
"pk",
"pck",
"t'es",
"coloc",
"colocation",
"loyer",
"payer",
"proprio",
"propriétaire",
"caf",
"charges",
"électricité",
"eau",
"gaz",
"facture",
"bah",
"ouais",
"te",
"toi",
"okay",
"cool",
"truc",
"trucs",
"nice",
"oh",
"tkt",
"mec",
"meuf",
"es chaud",
"suis chaud",
"photo",
"putain",
"merde",
"dsl",
"pote",
"genre",
"grave",
"ya",
"wesh",
"tu",
"ton",
#"ta",
"bro",
"youtube",
"euh",
"bah",
"ben",
"papi",
"mamie",
"hey",
":)",
";)",
":(",
":D",
"x)",
"xd",
"xD",
":p",
"<3",
":3",
"=)",
"=D",
"ahah",
"haha",
"peur",
"relation",
"couple",
"inté",
"wei",
"copain",
"copine",
"erasmus",
"problème",
"ce soir",
"tu fais quoi",
"ce week-end",
"ce week end",
"week-end",
"week end",
"tu m'as manqué",
"tu me manques",
"te voir",
"se voir",
"super",
"hyper",
"profite bien",
"t'es beau",
"t'es belle",
"t'es parfaite",
"t'es parfait",
"tu es parfaite",
"tu es parfait",
"toi et moi",
"ensemble",
"vegan",
"végan",
"végé",
"viande",
"maman",
"papa",
"père",
"mère",
"ça serait sympa",
"cours de quoi",
"tu viens en cours",
"demain soir",
"vendredi soir",
"ce soir",
"samedi soir",
"jeudi soir",
"demain",
"j'espère",
"appel",
"skype",
"vidéo",
"bébé",
"j'suis",
"jsuis",
"j'sais",
"j'me",
"j'vais",
"ami",
'amis',
'perso',
"t'es drôle",
'd’acc',
"d'acc",
"drôle",
'rire',
'mdr',
'ptdr',
'lol',
'projets',
'végan',
'projet',
'je vais manger',
"je vais dormir",
"je vais dodo",
"dodo",
'mère',
'bonne nuit',
'qqun',
'vivre',
'courage',
"vacances",
"parents",
'weekend',
'ohhh',
'contente',
'sorry',
'gentil',
'promis',
'triste',
"ill"
]

def extract_and_count_interessant_words(clean_text):

    modifiable_text = clean_text
    dict = {}
    for word in interessant_words:
        while word in modifiable_text:
            modifiable_text = modifiable_text.replace(word, " ", 1)
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    return dict #does not return clean_textanymore because it did not change !!!!!!!!!!!!!!!!!!!!




def print_wrong_words_to_copy():
    print("\n\naqui\n\n\n")
    text = "('c’était', 97)('mdrrr', 70)('infj', 59)('schéma', 57)('j’étais', 55)('toute', 55)('comprends', 49)('zèbre', 49)('tête', 48)('tellement' 47)('mdrr', 34)('reste', 31)('toutes', 30)('potes', 29)('justement', 26)('j’espère', 26)('totalement', 24)('vite', 22)('mdrrrr', 22)('réflexion', 22)('doute', 21)('autant', 21)('confiance', 20)('réfléchir', 20)"
    text = text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace(",", " ")
    text = text.replace("\t", " ")
    text = text.replace("\n", " ")
    text = text.replace("1", " ")
    text = text.replace("2", " ")
    text = text.replace("3", " ")
    text = text.replace("4", " ")
    text = text.replace("5", " ")
    text = text.replace("6", " ")
    text = text.replace("7", " ")
    text = text.replace("8", " ")
    text = text.replace("9", " ")
    text = text.replace("0", " ")
    text = text.replace("'", " ")
    text = text.split(" ")
    text = list(filter(None, text))
    print(text)
    #print(text)

#print_wrong_words_to_copy()

"""
"""


#ouais mais attends ya genre
def split_words(clean_text):
    clean_text = clean_text.replace("  ", " ")
    clean_text = clean_text.split(" ")
    clean_text = list(filter(None, clean_text))
    return clean_text


def clean_irrelevant_words(words_list): # marche pas bien parce que nettoie dans la string => à refaire
    irrelevant_words = ['je', 'est', "c'est", "c’est", "j’ai", "j'ai", "comme", 'tu', 'de', 'pas', 'c', 'et', 'que', 'en', 'le', 'la', 'ça', 'à', 'j', 'les', 'un', 'mais', 'pour', 'l', 'ai', 'du', 'des', 'il', 'on', 'bien', 'd', 'une', 'a', 'ce', 'me', 'qu', 'fait', 'elle', 'oui', 'plus', 'as', 'si', 'moi', 'au', 'avec', 'sur', 't', 'ou', 'qui', 'dans', 'ah', 'quand', 'faire', 'non', 'm', 'tout', 'mon', 'coup', 'suis', 'quoi', 'bon', 'trop', 'était', 'y', 'x', 'se', 'va', 'sais', 'là', 'es', 'même',
    'veux',
    'aussi',
    'être',
    'ta',
    'lui',
    'peux',
    'vais',
    'par',
    'peu',
    'dire',
    'très', 'fais', 'the', 'ils', 'faut', 'juste', 'comment', 'ma', 'son', 'après', 'vrai', 'donc', 'ne', 'tous', 'mieux', 'dit', 'voir', 'pense', 'peut', 'avais', 'mes', 'tes', 'fois', 'n', '=', 'vous', 'parce', 'sa', '', 'déjà', 'chez', 'cette', 'dis', 'marche', 'avait', 'sinon', 'bcp', 'of', 'to', 'alors', 'avant', 'puis', 'vas', 'temps', 'crois', 'vraiment', 'votre', 'ahh', 'nous', 'avoir', 'cas', 'sont',
    'rien',
    'vu',
    '+',
    "-",
    'fin',
    'vois',
    'encore',
    'mal', 'demain', 'où', "qu'il", "qu'elle", "qu'on", 'ont', 'moins', 'pourquoi', 'depuis', "d'ailleurs", 'bonne', 'vient', 'autre', 'enfin', 'aller', 'dois', 'sûr', 'petit', 'quel', 'maintenant', 'soit', 'eu', 'surtout', 'gens', 'nan', 'sans', 'tant', 'autres', 'ok', 'ces', 'besoin', 'connais', 'sens', 'jamais', 'passe', 'haha', 'vie', 'imagine', 'cet', 'aux', 'au', "j'avais", "qu'est", "j'aime", "ment", "nais", "côté", "coté", "cote", "parle",
    "mettre",
    "met",
    "mett",
    'j’aime',
    "garde",
    "demande",
    "moment",
    "quel",
    "partie",
    "soir",
    "com/watch", "entre", "s'est", "l'impression", "effet", "parler", "plein", "penses", "assez" "serait", "l'ai", "long", "longtemps", "pris", "question", "manqué", "part", "normal", "nant", "hier", "nais", "main", "bref", "message", "plutôt", "donne", "tiens", "trouve", "trouves", "heure", "encore", "souvent", "sera", "enco", "j'espè", "t'en", "t'as", "vers", "leur", "leurs", "voila", "voilà", "choses", "chose",
    "m'en",
    "beaucoup",
    "d'un",
    "d'une",
    "celle",
    "voit",
    "vois",
    "d'être",
    "l'air",
    "semaine",
    "tard",
    "exactement",
    "petite",
    "passant",
    "euros",
    "euro",
    "mois",
    "chaque",
    "niveau",
    "deja",
    "apres",
    "envoyé",
    "personne",
    "quelqu'un",
    "d'accord",
    'qu’il',
    'qu’on',
    'j’en',
    't’as',
    'j’avais',
    'l’impression',
    'd’être',
    'm’en',
    'quelqu’un',
    'qu’ils',
    't’es',
    'j’avoue',
    'd’un',
    'j’essaye',
    'j’aimerais',
    'd’accord',
    's’est',
    'sûrement',
    'n’est',
    'j’es',
    'doit',
    'quelques',
    'sait',
    'paris',
    'lement',
    'l’autre',
    'j’arrive',
    'travail',
    'premier',
    'qu’elle',
    'l’école',
    'année',
    'clair',
    'd’ailleurs',
    'disais',
    'quelque',
    'l’ai',
    'l’air',
    'qu’à',
    'week',
    'manière',
    'pensé',
    'place',
    'meme',
    "deux",
    "trois",
    'etre',
    'prendre',
    "assez",
    "envie",
    "notre",
    "drôle",
    "rapport",
    "passer",
    "loin",
    "cours",
    "ensui",
    "fille",
    "filles",
    "loin",
    "sympa",
    "serait",
    "seul",
    "seule",
    "question",
    "profi",
    "manqué",
    "monde",
    "peti",
    "toujours",
    "sous",
    "quel",
    "quelle",
    "cher",
    "pris",
    "façon",
    "beau",
    "belle",
    "dont",
    'fort',
    "nuit",
    'passé',
    'pareil',
    'exemple',
    'facile',
    "l'autre",
    "manger",
    "dormir",
    'trouver',
    'arrê',
    'forcément',
    "qu'ils",
    'fond',
    'jours',
    'meilleur',
    'gars',
    'fiance',
    'pendant',
    'début',
    "d'autres",
    'compris',
    'exac',
    'font',
    'général',
    'nexion',
    'pouvoir',
    'comprendre',
    'veut',
    "jusqu'à",
    'type',
    'llement',
    'changer',
    'sortir',
    "d'avoir",
    'tion',
    'clairement',
    'point',
    'discu',
    'public',
    'dessus',
    'faisait',
    'parlé',
    'trer',
    "s'il",
    "s'en",
    'récemment',
    'compliqué',
    'première',
    'jour',
    'partir',
    'possible',
    'voulais',
    'devant',
    'impor',
    'allez',
    'mots',
    'ient',
    'laisser',

    "c'était",
    "j'étais",
    'sûre',
    'compte',
    'essayer',
    'parfois',
    'avez',
    'regarder',
    'venir',
    'contre',
    "m'as",
    'madrid',
    'prends',


    'versation',
    'c’était',
    'mdrrrr',
    'mdrrr',
    'mdrr',
    'j’étais',
    'toute',
    'comprends',
    'tête',
    'tellement',
    'reste',
    'toutes',
    'potes',
    'justement',
    'j’espère',
    'totalement',
    'vite',
    'réflexion',
    'doute',
    'autant',
    'confiance',
    'réfléchir',
    'ation',
    'vont',
    'savoir',
    'celui',
    'médi',
    'ntiel',
    'difficile',
    'présent',
    'proche',
    'donner',
    'grand',
    'tres',
    'copine',
    'complè',
    'sauf',
    'raison',
    'bleu',
    'ition',
    "http://www",
    "https://www",
    "comp",
    "j'en",
    'pu',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    '(',
    ')',
    '',
    '*']
    irrelevant_words = irrelevant_words + interessant_words ###
    clean_list = []
    for word in words_list:
        if word not in irrelevant_words:
            clean_list.append(word)


    return clean_list


# recuperer les noms de gens
# recuperer les adresses web yes
# recuperer le tutoiement à part
# recuperer les smileys
# recuperer les noms de villes


# renvoie la liste des fichiers de messages json dans le dossier en input
def message_files_list(dir_path):
    result = []
    for f in Path(dir_path).walkfiles():
        if (f.find('message_') != -1 and f.find('.json') != -1):
            result.append(f)
    return result

#Renvoit 2 listes pour une discussion precise : celle des messages recus et celle des messages envoyes
def received_messages_parser(file_path):
    #with open(file_path) as json_data:
        #json.load(io.open('sample.json', 'r', encoding='utf-8-sig'))

    with io.open(file_path, "r", encoding='utf-8-sig') as json_data:
        data = json.load(json_data) #, encoding='utf8'

    #data = json.loads(open(file_path).read().decode('utf-8-sig'))

    #with io.open(file_path, 'r', encoding='utf-8-sig') as json_file:
    #    data = json.load(json_file)

    #data = json.load(codecs.open(file_path, 'r', 'utf-8-sig'))

    messages_received = ""
    messages_sent = ""
    for k in data["messages"]:
        if (k["sender_name"] != "LoÃ¯c Garnier" and 'content' in k):
            messages_received = messages_received + " " + k["content"]
        if (k["sender_name"] == "LoÃ¯c Garnier" and 'content' in k):
            messages_sent = messages_sent + " " + k["content"]

    return [messages_sent.encode('latin1').decode('utf-8-sig'), messages_received.encode('latin1').decode('utf-8-sig')]

#Parse les messages envoyes et recus d'une discussion precise (chemin donne dans dir_path)
def discussion_parser(dir_path):
    messages_sent = ""
    messages_received = ""
    for file_path in message_files_list(dir_path):
        #print(file_path)
        parsed = received_messages_parser(file_path)
        messages_sent = messages_sent + " " + parsed[0]
        messages_received = messages_received + " " + parsed[1]


    return [messages_sent, messages_received]

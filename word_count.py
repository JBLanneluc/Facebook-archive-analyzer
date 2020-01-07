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
    for k in range(len(message)):
        if message[k] == "h" and message[k+1] == "t" and message[k+2] == "t" and message[k+3] == "p":
            c = 0
            while message[k+c] != " ":
                c += 1
            https.append(message[k:k+c])
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

    return Counter(clean_https).most_common()

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


def replace_accents(words_list):
    clean = words_list.replace("(","")
    clean = clean.replace(")","")
    clean = clean.replace("'","")
    clean = clean.replace("'","")
    clean = clean.replace(",","")

    """
    clean = clean.replace("0","")
    clean = clean.replace("1","")
    clean = clean.replace("2","")
    clean = clean.replace("3","")
    clean = clean.replace("4","")
    clean = clean.replace("5","")
    clean = clean.replace("6","")
    clean = clean.replace("7","")
    clean = clean.replace("8","")
    clean = clean.replace("9","")
    """

    clean = clean.replace("ã©","é")
    clean = clean.replace("Ã©","é")

    clean = clean.replace("ã¨","è")
    clean = clean.replace("Ã¨","è")

    clean = clean.replace("ãª","ê")
    clean = clean.replace("Ãª","ê")

    clean = clean.replace("ã§","ç")
    clean = clean.replace("Ã§","ç")


    clean = clean.replace("ã»","û")
    clean = clean.replace("ã¹","ù")
    clean = clean.replace("ã¯","ï")

    clean = clean.replace("ã´","ô")
    clean = clean.replace("Ã´","ô")



    clean = clean.replace("ã","à")
    clean = clean.replace("Ã","à")




    return clean


def parse_terminal_list_for_research_purposes():
    #irrelevant_words = ["le", "la", "je", "j", "tu", "on"]
    irrelevant_words = "('je', 1216)('est', 1110)('tu', 1073)('de', 1064)('pas', 913)('c', 910)('et', 870)('que', 713)('en', 712)('le', 687)('la', 682)('ã§a', 660)('ã', 657)('j', 598)('les', 508)('un', 505)('mais', 484)('pour', 465)('l', 390)('ai', 372)('du', 325)('des', 321)('il', 307)('on', 305)('bien', 303)('d', 282)('une', 282)('a', 266)('ce', 266)('me', 261)('te', 253)('qu', 252)('ouais', 249)('fait', 248)('elle', 246)('oui', 234)('plus', 232)('as', 230)('si', 229)('moi', 221)('toi', 209)('au', 209)('avec', 209)('sur', 208)('t', 207)('ou', 206)('qui', 204)('dans', 199)('ah', 192)('quand', 185)('faire', 174)('non', 171)('m', 171)('tout', 169)('mon', 164)('coup', 159)('suis', 159)('quoi', 158)('bon', 149)('trop', 149)('ã©tait', 146)('y', 141)('x', 141)('se', 135)('va', 134)('sais', 131)('ton', 129)('lã', 124)('es', 118)('mãªme', 118)('veux', 117)('ã\x87a', 110)('aussi', 109)('1', 107)('ãªtre', 105)('ta', 105)('lui', 100)('peux', 99)('s', 97)('vais', 96)('2', 96)('par', 95)('peu', 95)('dire', 91)('trã¨s', 88)('fais', 87)('the', 87)('ils', 85)('faut', 84)('0', 84)('juste', 83)('ð\x9f\x98\x82', 83)('comment', 78)('rã©da', 77)('okay', 76)('ma', 76)('cool', 75)('genre', 75)('son', 75)('truc', 72)('ouaip', 72)('aprã¨s', 72)('gros', 70)('vrai', 70)('merci', 69)('donc', 69)('ne', 65)('tous', 63)(',', 63)('mieux', 62)('dit', 62)('oh', 62)('voir', 62)('int', 62)('https', 61)('pense', 61)('peut', 61)('avais', 60)('com', 59)('mes', 59)('grave', 58)('tes', 58)('fois', 58)('n', 58)('=', 58)('vous', 57)('parce', 57)('putain', 57)('sa', 57)('3', 57)('dã©jã', 55)('chez', 55)('cette', 55)('dis', 54)('marche', 53)('trucs', 51)('avait', 51)('sinon', 51)('bcp', 51)('of', 50)('to', 50)('alors', 49)('avant', 48)('puis', 48)('vas', 48)('aime', 48)('temps', 48)('aurã©lie', 47)('crois', 47)('vraiment', 47)('votre', 45)('pk', 45)('ahh', 45)('nous', 44)('avoir', 44)('cas', 43)('sont', 42)('rien', 42)('vu', 41)('i', 41)('+', 41)('fin', 41)('vois', 40)('encore', 40)('mal', 40)('demain', 39)('oã¹', 39)('comprends', 39)('www', 39)('mec', 39)('ont', 38)('moins', 38)('bonne', 37)('ya', 37)('vient', 37)('autre', 36)('enfin', 36)('clara', 36)('aller', 36)('tkt', 35)('dois', 35)('*', 34)('sã»r', 34)('petit', 32)('quel', 31)('chaud', 31)('maintenant', 31)('soit', 31)('eu', 30)('surtout', 30)('gens', 30)('merde', 30)('loã¯c', 30)('pauline', 29)('4', 29)('nan', 29)('sans', 28)('pote', 28)('tant', 28)('autres', 28)('photo', 28)('ok', 27)('ces', 27)('besoin', 27)('connais', 27)('sens', 27)('jamais', 27)('passe', 27)('haha', 27)('vie', 27)('imagine', 27)('mode', 27)('if', 27)"

    clean = irrelevant_words.replace("(","")
    clean = clean.replace(")","")
    clean = clean.replace("'","")
    clean = clean.replace("'","")
    clean = clean.replace(",","")

    clean = clean.replace("0","")
    clean = clean.replace("1","")
    clean = clean.replace("2","")
    clean = clean.replace("3","")
    clean = clean.replace("4","")
    clean = clean.replace("5","")
    clean = clean.replace("6","")
    clean = clean.replace("7","")
    clean = clean.replace("8","")
    clean = clean.replace("9","")

    clean = clean.replace("ã©","é")
    clean = clean.replace("ã¨","è")
    clean = clean.replace("ã»","û")
    clean = clean.replace("ã¹","ù")
    clean = clean.replace("ãª","ê")
    clean = clean.replace("ã¯","ï")
    clean = clean.replace("à","ç")
    clean = clean.replace("ã","à")
    clean = clean.replace("ã´","ô")
    clean = clean.replace("ã®","î")



    clean = clean.split(" ")
    print(clean)


weird_ones = ["ð", "ð\x9f\x98\x82"]

#a garder

def extract_and_count_interessant_words(clean_text):
    interessant_words = ["je t'aime", "je t'adore", "tiens au jus", "ça va", "tu vas bien", "tiens au courant", "je comprends", "appelle", "t'inquiète", "la semaine prochaine", "je suis désolée", "je suis désolé", "désolée", "désolé", "merci", "viens", "mode", "jouer", "yo", "soirées", "soirée", "soiree", "gros", "hmm", "ouaip", "con", "connard", "hein", "pk", "pck", "t'es", "coloc", "colocation", "bah", "ouais", "te", "toi", "okay", "cool", "truc", "trucs", "nice", "oh", "tkt", "mec", "meuf", "chaud", "photo", "putain", "merde", "dsl", "pote", "genre", "grave", "ya", "wesh", "tu", "ton", "ta", "bro", "youtube", "euh", "bah", "ben", ":)", ";)", ":(", ":D", "x)", "xd", "xD", ":p", "<3", ":3", "=)", "=D", "ahah", "haha", "peur", "relation", "couple", "inté", "erasmus", "problème", "ce soir", "tu fais quoi", "ce week-end", "week-end", "tu m'as manqué", "tu me manques", "te voir", "se voir", "super", "hyper", "profite bien", "t'es beau", "t'es belle", "t'es parfaite", "t'es parfait", "tu es parfaite", "tu es parfait", "toi et moi", "ensemble", "vegan", "végé", "viande", "maman", "père", "ça serait sympa", "cours de quoi", "tu viens en cours", "demain soir", "vendredi soir", "ce soir", "samedi soir", "jeudi soir", "demain", "j'espère", "appel", "skype", "vidéo", "bébé", "j'suis", "jsuis", "j'sais", "j'me", "j'vais",
    "ami",
    'amis',
    'perso',
    "t'es drôle",
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
    'courage'
    ]
    dict = {}
    for word in interessant_words:
        while word in clean_text:
            clean_text = clean_text.replace(word, " ", 1)
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
    return [clean_text, dict]

# a checker : tutoiement, photo, nom de personnes, soiree, genre, cool, ouaip, ton, truc, gros, oh, https, com (.com), ya, tkt, www, mec, okay, chaud, grave, putain, merde, nan, pote, mode, aime, comprends, photo, pote
# extraire les smileys, les je t'aime, mal, soirée, etc !!!
#maman papa famille


"""
('qu’il', 174)
('qu’on', 76)
('j’en', 65)
('t’as', 64)
('j’avais', 61)
('infj', 59)
('schéma', 57)
('zèbre', 49)
('l’impression', 48)
('d’être', 48)
('j’aime', 48)
('m’en', 47)
('quelqu’un', 42)
('parents', 39)
('qu’ils', 39)
('t’es', 37)
('d’acc', 36)
('j’avoue', 33)
('d’un', 33)
('j’essaye', 30)
('j’aimerais', 30)
('d’accord', 28)
('s’est', 28)
('sûrement', 27)
('n’est', 26)
('j’es', 26)
('doit', 26)
('quelques', 25)
('sait', 25)
('paris', 25)
('lement', 25)
('l’autre', 25)
('j’arrive', 25)
('travail', 24)
('premier', 23)
('qu’elle', 23)
('l’école', 23)
('année', 22)
('clair', 22)
('d’ailleurs', 22)
('disais', 22)
('réflexion', 22)
('quelque', 21)
('l’ai', 21)
('l’air', 21)
('qu’à', 21)
('week', 21)
('manière', 20)
('pensé', 20)
('place', 20)
('réfléchir', 20)
"""


#ouais mais attends ya genre
def split_words(clean_text):
    clean_text = clean_text.replace("  ", " ")
    clean_text = clean_text.split(" ")
    clean_text = list(filter(None, clean_text))
    return clean_text


def clean_irrelevant_words(words_list): # marche pas bien parce que nettoie dans la string => à refaire
    irrelevant_words = ['je', 'est', "c'est", "c’est", "j’ai", "j'ai", "comme", 'tu', 'de', 'pas', 'c', 'et', 'que', 'en', 'le', 'la', 'ça', 'à', 'j', 'les', 'un', 'mais', 'pour', 'l', 'ai', 'du', 'des', 'il', 'on', 'bien', 'd', 'une', 'a', 'ce', 'me', 'qu', 'fait', 'elle', 'oui', 'plus', 'as', 'si', 'moi', 'au', 'avec', 'sur', 't', 'ou', 'qui', 'dans', 'ah', 'quand', 'faire', 'non', 'm', 'tout', 'mon', 'coup', 'suis', 'quoi', 'bon', 'trop', 'était', 'y', 'x', 'se', 'va', 'sais', 'là', 'es', 'même', 'veux', 'aussi', '', 'être', 'ta', 'lui', 'peux', 's', 'vais', 'par', 'peu', 'dire', 'très', 'fais', 'the', 'ils', 'faut', 'juste', 'comment', 'ma', 'son', 'après', 'vrai', 'donc', 'ne', 'tous', 'mieux', 'dit', 'voir', 'pense', 'peut', 'avais', 'mes', 'tes', 'fois', 'n', '=', 'vous', 'parce', 'sa', '', 'déjà', 'chez', 'cette', 'dis', 'marche', 'avait', 'sinon', 'bcp', 'of', 'to', 'alors', 'avant', 'puis', 'vas', 'temps', 'crois', 'vraiment', 'votre', 'ahh', 'nous', 'avoir', 'cas', 'sont', 'rien', 'vu', 'i', '+', 'fin', 'vois', 'encore', 'mal', 'demain', 'où', "qu'il", "qu'elle", "qu'on", 'ont', 'moins', 'pourquoi', 'depuis', "d'ailleurs", 'bonne', 'vient', 'autre', 'enfin', 'aller', 'dois', 'sûr', 'petit', 'quel', 'maintenant', 'soit', 'eu', 'surtout', 'gens', 'nan', 'sans', 'tant', 'autres', 'ok', 'ces', 'besoin', 'connais', 'sens', 'jamais', 'passe', 'haha', 'vie', 'imagine', 'cet', 'aux', 'au', "j'avais", "qu'est", "j'aime", "ment", "nais", "côté", "coté", "cote", "parle", "mettre", "met", "mett", "garde", "demande", "moment", "quel", "partie", "soir", "com/watch", "entre", "s'est", "l'impression", "effet", "parler", "plein", "penses", "assez" "serait", "l'ai", "long", "longtemps", "pris", "question", "manqué", "part", "normal", "nant", "hier", "nais", "main", "bref", "message", "plutôt", "donne", "tiens", "trouve", "trouves", "heure", "encore", "souvent", "sera", "enco", "j'espè", "t'en", "t'as", "vers", "leur", "leurs", "voila", "voilà", "choses", "chose", "m'en",  "beaucoup", "d'un", "d'une", "celle", "voit", "vois", "d'être", "l'air", "semaine", "passant", "euros", "euro", "mois", "chaque", "niveau", "deja", "apres", "envoyé", "personne", "quelqu'un", "d'accord", 'meme', "deux", "trois", 'etre', 'prendre', "assez", "envie", "notre", "drôle", "rapport", "passer", "loin", "cours", "ensui", "fille", "filles", "loin", "sympa", "serait", "seul", "seule", "question", "profi", "manqué", "monde", "peti", "toujours", "sous", "quel", "quelle", "cher", "pris", "façon", "beau", "belle", "dont",
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
    'versation',
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
    "http://www", "https://www", "comp", "j'en", 'pu', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '(', ')', '*']
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

    data = json.load(codecs.open(file_path, 'r', 'utf-8-sig'))

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

#AurelieGalea_bE7hp1v_Dg
#RedaDiouri_mhrkjg0Ipg
#PaulineSch_jGhV8u0dVA
#MarjolaineVrs_EHqk8KdqeA
#CedricBay_XjPXsuUgjA
#JeanBaptisteLanneluc_NnhjkMmx-A
dir_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\JeanBaptisteLanneluc_NnhjkMmx-A"

k=1
#print("\n\n\n\n\n\n%s\n\n\n\n\n\n"%k)
parsed = discussion_parser(dir_path)
#print(parsed)

k+=1
#print("\n\n\n\n\n\n%s\n\n\n\n\n\n"%k)
https = internet_address_extractor(parsed[1])
#print(https)
print("\n\n\n\n\n\nMost shared internet addresses\n\n\n")
for address in https:
    if address[1] >= 2 and len(address[0]) >= 0:
        print(address)


k+=1
#print("\n\n\n\n\n\n%s\n\n\n\n\n\n"%k)
clean_text = text_cleaner1(parsed[1])
#print(clean_text)

k+=1
#print("\n\n\n\n\n\n%s\n\n\n\n\n\n"%k)
interessant_words_count = {}
[clean_text, interessant_words_count] = extract_and_count_interessant_words(clean_text)
#print(interessant_words_count)
print("\n\n\n\n\n\nMost shared interessant words\n\n\n")
for key, value in sorted(interessant_words_count.items(), key=lambda x: x[1], reverse=True):
    if value >= 5:
        print("%s\t\t%s" % (value, key))


#clean_irrelevant_words(clean_text)

k+=1
#print("\n\n\n\n\n\n%s\n\n\n\n\n\n"%k)
words_list = split_words(clean_text)
#print(words_list)

#print(words_list)
k+=1
#print("\n\n\n\n\n\n%s\n\n\n\n\n\n"%k)
words_list = clean_irrelevant_words(words_list)
#print(words_list)



k+=1
#print("\n\n\n\n\n\n%s\n\n\n\n\n\n"%k)
words_list = word_count(words_list)

print("\n\n\n\n\n\nMost shared other words\n\n\n")
for word in words_list:
    if word[1] >= 5 and len(word[0]) >= 4:
        print(word)






"""

k+=1
print("\n\n\n\n\n\n%s\n\n\n\n\n\n"%k)
clean_text = clean_irrelevant_words(clean_text) # marche pas bien
print(clean_text)

k+=1
print("\n\n\n\n\n\n%s\n\n\n\n\n\n"%k)
words_list = word_count(clean_text)
print(words_list)
"""


#clean_irrelevant_words()



#print(words)

#print("é ç à ï ô û")












##

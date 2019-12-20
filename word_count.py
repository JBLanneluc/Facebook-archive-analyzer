from collections import Counter
from path import Path
import json

#Lien de word_cloud :
# http://www.sthda.com/french/wiki/text-mining-et-nuage-de-mots-avec-le-logiciel-r-5-etapes-simples-a-savoir


def text_cleaner(message):
    for char in ["'", "\"", "-", "_", "/", ".", ",", ":", ";", "!", "?", "(", ")", "[", "]", "{", "}", "\t", "\n"]:
        message = message.replace(char, " ")
    message = message.lower()
    return message

def word_count(clean_message):
    words_list = clean_message.split()
    words_list = Counter(words_list).most_common()
    return words_list





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
    clean = clean.replace("ã§","ç")
    clean = clean.replace("ã","à")

    clean = clean.split(" ")
    print(clean)


weird_ones = ["ð", "ð\x9f\x98\x82"]

#a garder



def clean_irrelevant_words(words_list): # marche pas bien parce que nettoie dans la string => à refaire
    irrelevant_words = ['je', 'est', 'tu', 'de', 'pas', 'c', 'et', 'que', 'en', 'le', 'la', 'ça', 'à', 'j', 'les', 'un', 'mais', 'pour', 'l', 'ai', 'du', 'des', 'il', 'on', 'bien', 'd', 'une', 'a', 'ce', 'me', 'qu', 'fait', 'elle', 'oui', 'plus', 'as', 'si', 'moi', 'au', 'avec', 'sur', 't', 'ou', 'qui', 'dans', 'ah', 'quand', 'faire', 'non', 'm', 'tout', 'mon', 'coup', 'suis', 'quoi', 'bon', 'trop', 'était', 'y', 'x', 'se', 'va', 'sais', 'là', 'es', 'même', 'veux', 'aussi', '', 'être', 'ta', 'lui', 'peux', 's', 'vais', 'par', 'peu', 'dire', 'très', 'fais', 'the', 'ils', 'faut', 'juste', 'comment', 'ma', 'son', 'après', 'vrai', 'donc', 'ne', 'tous', 'mieux', 'dit', 'voir', 'pense', 'peut', 'avais', 'mes', 'tes', 'fois', 'n', '=', 'vous', 'parce', 'sa', '', 'déjà', 'chez', 'cette', 'dis', 'marche', 'avait', 'sinon', 'bcp', 'of', 'to', 'alors', 'avant', 'puis', 'vas', 'temps', 'crois', 'vraiment', 'votre', 'ahh', 'nous', 'avoir', 'cas', 'sont', 'rien', 'vu', 'i', '+', 'fin', 'vois', 'encore', 'mal', 'demain', 'où', 'ont', 'moins', 'bonne', 'vient', 'autre', 'enfin', 'aller', 'dois', 'sûr', 'petit', 'quel', 'maintenant', 'soit', 'eu', 'surtout', 'gens', 'nan', 'sans', 'tant', 'autres', 'ok', 'ces', 'besoin', 'connais', 'sens', 'jamais', 'passe', 'haha', 'vie', 'imagine']

    for word in irrelevant_words:
        if word in words_list:
            words_list = words_list.replace("%s"%word, "")

    return words_list

# a checker : tutoiement, photo, nom de personnes, soiree, genre, cool, ouaip, ton, truc, gros, oh, https, com (.com), ya, tkt, www, mec, okay, chaud, grave, putain, merde, nan, pote, mode, aime, comprends, photo, pote
# extraire les smileys, les je t'aime, mal, soirée, etc !!!

# renvoie la liste des fichiers de messages json dans le dossier en input
def message_files_list(dir_path):
    result = []
    for f in Path(dir_path).walkfiles():
        if (f.find('message_') != -1 and f.find('.json') != -1):
            result.append(f)
    return result

#Renvoit 2 listes pour une discussion precise : celle des messages recus et celle des messages envoyes
def received_messages_parser(file_path):
    with open(file_path) as json_data:
        data = json.load(json_data)
    messages_received = ""
    messages_sent = ""
    for k in data["messages"]:
        if (k["sender_name"] != "LoÃ¯c Garnier" and 'content' in k):
            messages_received = messages_received + " " + k["content"]
        if (k["sender_name"] == "LoÃ¯c Garnier" and 'content' in k):
            messages_sent = messages_sent + " " + k["content"]
    return [messages_sent, messages_received]

#Parse les messages envoyes et recus d'une discussion precise (chemin donne dans dir_path)
def discussion_parser(dir_path):
    messages_sent = ""
    messages_received = ""
    for file_path in message_files_list(dir_path):
        print(file_path)
        parsed = received_messages_parser(file_path)
        messages_sent = messages_sent + " " + parsed[0]
        messages_received = messages_received + " " + parsed[0]


    return [messages_sent, messages_received]

dir_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\RedaDiouri_mhrkjg0Ipg"



parsed = discussion_parser(dir_path)
#print(parsed)
clean_text = text_cleaner(parsed[0])
clean_text = clean_irrelevant_words(clean_text) # marche pas bien
words_list = word_count(clean_text)


#clean_irrelevant_words()
#words = word_count(parsed[0])


#print(words)
for word in words_list:
    if word[1] >= 10:
        print(word)





#print("é ç à ï ô û")












##

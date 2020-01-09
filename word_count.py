from functions_word_count import *
from functions_characterize import *
from functions_main import *

#AurelieGalea_bE7hp1v_Dg
#RedaDiouri_mhrkjg0Ipg
#PaulineSch_jGhV8u0dVA
#MarjolaineVrs_EHqk8KdqeA
#CedricBay_XjPXsuUgjAs
#JeanBaptisteLanneluc_NnhjkMmx-A
#NoemieHennequin_bNjUhVHR0A
#MeghanedeAraujo_Ajq-7uQmQA
#ClaraBookflyer_sd3e4EFpdQ
#SophieDokBodart_bLzC3g-_zg



"""
Gens a tester :
Reda
Cedric
Charlotte
Pauline
Aurelie
JB
Corentin


"""
person_to_analyse = "Aurélie Galea"

def conversation_analyser(person_name):

    #inbox_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\"
    inbox_path = "/home/jean-baptiste/Travail/5A/Projet/facebook-loicgarnier104/messages/inbox/"
    name_matching_dict = group_file_list(inbox_path)[2]
    #dir_path = inbox_path + name_matching_dict[person_name]
    dir_path = "/home/jean-baptiste/Travail/5A/Projet/facebook-loicgarnier104/messages/inbox/aureliegalea_be7hp1v_dg"
    parsed = discussion_parser(dir_path)
    sent = parsed[0] # 1 = lui, 0 = toi
    received = parsed[1] # 1 = lui, 0 = toi
    total_nb_of_messages = get_total_number_of_messages(df_sent, df_received)[person_name]
    #print(total_nb_of_messages)
    #conversation_dict = {"sent": sent, "received": received}



    #person_name = dir_path.split("\\").pop().split("_")[0]

    text_to_analyse = sent + received

    print("\n")
    print("____________________________________________________________________________________________________________________________")
    print(person_name)
    print("____________________________________________________________________________________________________________________________\n")

    #text_to_analyse = conversation_dict[key]


    """
    """
    [https, https_counter] = internet_address_extractor(text_to_analyse)

    print("____________________________________________________________________________________________________________________________")
    print("Most shared internet addresses")
    print("____________________________________________________________________________________________________________________________\n")
    for address in https_counter:
        print(address)
        #if address[1] >= 1:# and len(address[0]) >= 0:


    numbers = phone_number_extractor(text_to_analyse, https)
    print("____________________________________________________________________________________________________________________________")
    print("Shared phone numbers")
    print("____________________________________________________________________________________________________________________________\n")
    for number in numbers:
        print(number)


    ### separate sent and received or not
    clean_text = text_cleaner1(text_to_analyse)
    #clean_text = text_cleaner1(text_to_analyse) ### separate sent and received


    """
    interessant_words_count = extract_and_count_interessant_words(clean_text)
    print("\n\n\n\n\n\nMost shared interessant words\n\n\n")
    for key, value in sorted(interessant_words_count.items(), key=lambda x: x[1], reverse=True):
        if value >= 50:
            print("%s\t\t%s" % (value, key))
    """

    characterize = extract_characterizing_categories(clean_text)
    """
    print("\n\n\nCharacterizing categories\n")
    for key, value in sorted(characterize.items(), key=lambda x: x[1], reverse=True):
        if value >= 0:
            #print("%s\t%s" % (value, key))
            pass
    """

    #estimated_degree_of_friendship = characterize_with_weights(characterize)
    print("____________________________________________________________________________________________________________________________")
    print("Characterizing percentages")
    print("____________________________________________________________________________________________________________________________\n")
    percentages_characterizing = characterize_with_percentages_for_each_category(characterize, person_name)
    #print(percentages_characterizing)

    words_list = split_words(clean_text)

    words_list = clean_irrelevant_words(words_list)


    words_list = word_count(words_list)

    print("____________________________________________________________________________________________________________________________")
    print("Most shared other words")
    print("____________________________________________________________________________________________________________________________\n")
    for word in words_list:
        if word[1] >= total_nb_of_messages/200 and len(word[0]) >= 4:
            print(word)

    """
    """

#conversation_analyser(person_to_analyse)



##

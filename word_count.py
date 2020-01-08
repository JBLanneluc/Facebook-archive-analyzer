from functions_word_count import *
from functions_characterize import *

#AurelieGalea_bE7hp1v_Dg
#RedaDiouri_mhrkjg0Ipg
#PaulineSch_jGhV8u0dVA
#MarjolaineVrs_EHqk8KdqeA
#CedricBay_XjPXsuUgjA
#JeanBaptisteLanneluc_NnhjkMmx-A



dir_path = "C:\\Users\\loicg\\Desktop\\facebook-loicgarnier104\\messages\\inbox\\AurelieGalea_bE7hp1v_Dg"
parsed = discussion_parser(dir_path)
text_to_analyse = parsed[1] # 1 = lui, 0 = toi


[https, https_counter] = internet_address_extractor(text_to_analyse)

print("\n\n\n\n\n\nMost shared internet addresses\n\n\n")
for address in https_counter:
    if address[1] >= 2 and len(address[0]) >= 0:
        print(address)


numbers = phone_number_extractor(text_to_analyse, https)
print("\n\n\n\n\n\nShared phone numbers\n\n\n")
for number in numbers:
    print(number)




clean_text = text_cleaner1(text_to_analyse)


"""
interessant_words_count = extract_and_count_interessant_words(clean_text)
print("\n\n\n\n\n\nMost shared interessant words\n\n\n")
for key, value in sorted(interessant_words_count.items(), key=lambda x: x[1], reverse=True):
    if value >= 50:
        print("%s\t\t%s" % (value, key))
"""

characterize = extract_and_characterize(clean_text)
print("\n\n\n\n\n\nCharacterizing categories\n\n\n")
for key, value in sorted(characterize.items(), key=lambda x: x[1], reverse=True):
    if value >= 0:
        print("%s\t\t%s" % (value, key))



words_list = split_words(clean_text)

words_list = clean_irrelevant_words(words_list)


words_list = word_count(words_list)

print("\n\n\n\n\n\nMost shared other words\n\n\n")
for word in words_list:
    if word[1] >= 20 and len(word[0]) >= 4:
        print(word)









##

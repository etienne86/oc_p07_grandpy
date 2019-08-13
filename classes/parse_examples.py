import re

import classes.stop_words as stop_words


string_list = [
    "Hey GrandPy, salut ! Comment vas-tu ? J'aimerais savoir où se trouve la Tour Montparnasse s'il te plaît ?",
    "Je veux aller faire un tour au zoo de Beauval. Il paraît que cet endroit est merveilleux.",
    "Coucou mon vieux, peux-tu me dire où se trouve la poste de Poitiers STP ?",
    "salut grand py bot, est ce que tu connais la basilique de saint maximin",
    "ou est la tour eiffel",
    "ou trouver la cathedrale notre dame"
]

result_list = [
    ["Tour", "Montparnasse"],
    ["Zoo", "Beauval"],
    ["Poste", "Poitiers"],
    ["Basilique", "Saint", "Maximin"],
    ["Tour", "Eiffel"]
]

# sub function
def exclude_expressions(words):
    result = words # type is list
    consec = stop_words.consecutive_fr
    for i in range(len(words) - 1):
        for j in range(len(consec)):
            if words[i] == consec[j][0] and words[i+1] == consec[j][1]:
                # remove the two consecutive words
                if i == 0 and i+1 == len(words) - 1: # if list is only two words
                    result = []
                elif i == 0: # if words are at the beginning
                    result = words[i+2:] # keep only the end
                elif i+1 == len(words) - 1: # if words are at the end
                    result = result[:i]
                else:
                    result = result[:i] + words[i+2:]
    return result


# remove punctuation
sub_string_list = [re.sub("([,\?;\.\:!/\\\*\(\)\[\]])*", "", string)\
    for string in string_list]

# remove redundant spaces
sub_string_list = [re.sub("( ){2,}", " ", sub_string)\
    for sub_string in sub_string_list]

# transform to lowercase
sub_string_list = [sub_string.lower() for sub_string in sub_string_list]

# split
words_list = [sub_string.split() for sub_string in sub_string_list]

# exclude stop words
limited_list = [
    [word for word in elt if word not in stop_words.all_fr] \
        for elt in words_list
]

# exclude stop expressions (two consecutive words)
lower_result = [exclude_expressions([sub_item for sub_item in item]) \
    for item in limited_list]

# capitalize for Google Maps and Wikipedia search
capitalize_result = [[sub_item.capitalize() for sub_item in item] \
    for item in lower_result]

# check the results
print(capitalize_result)
# print(capitalize_result == result_list)
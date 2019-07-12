from utils.clustering_utils import get_letters_appearances, get_levenshteins_avr, \
    get_special_symbols_appearances, get_number_appearances, get_levenshteins_minmax,  \
    get_levenshteins_min,get_levenshteins_max


def minmaxlev(companies_names_list):
    cn_with_features_list = []
    for cname in companies_names_list:
        letters_appearance_vector = get_letters_appearances(cname)
        numbers_appearance_vector = get_number_appearances(cname)
        levenshtain_dist_vector = get_levenshteins_minmax(cname)
        symbols_appearance_vector = get_special_symbols_appearances(cname)

        features = letters_appearance_vector + \
                   numbers_appearance_vector + \
                   levenshtain_dist_vector + \
                   symbols_appearance_vector

        cn_with_features_list.append(
            [cname] + features
        )
    return cn_with_features_list


def avrlev(companies_names_list):
    cn_with_features_list = []
    for cname in companies_names_list:
        letters_appearance_vector = get_letters_appearances(cname)
        numbers_appearance_vector = get_number_appearances(cname)
        levenshtain_dist_vector = get_levenshteins_avr(cname)
        symbols_appearance_vector = get_special_symbols_appearances(cname)

        features = letters_appearance_vector + \
                   numbers_appearance_vector + \
                   levenshtain_dist_vector + \
                   symbols_appearance_vector

        cn_with_features_list.append(
            [cname] + features
        )
    return cn_with_features_list


def minlev(companies_names_list):
    cn_with_features_list = []
    for cname in companies_names_list:
        letters_appearance_vector = get_letters_appearances(cname)
        numbers_appearance_vector = get_number_appearances(cname)
        levenshtain_dist_vector = get_levenshteins_min(cname)
        symbols_appearance_vector = get_special_symbols_appearances(cname)

        features = letters_appearance_vector + \
                   numbers_appearance_vector + \
                   levenshtain_dist_vector + \
                   symbols_appearance_vector

        cn_with_features_list.append(
            [cname] + features
        )
    return cn_with_features_list


def maxlev(companies_names_list):
    cn_with_features_list = []
    for cname in companies_names_list:
        letters_appearance_vector = get_letters_appearances(cname)
        numbers_appearance_vector = get_number_appearances(cname)
        levenshtain_dist_vector = get_levenshteins_max(cname)
        symbols_appearance_vector = get_special_symbols_appearances(cname)

        features = letters_appearance_vector + \
                   numbers_appearance_vector + \
                   levenshtain_dist_vector + \
                   symbols_appearance_vector

        cn_with_features_list.append(
            [cname] + features
        )
    return cn_with_features_list
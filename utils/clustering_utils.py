import re
import Levenshtein as levd

from configs.word_lists import LETTERS_EN, LEVENSHTEIN_WORDS, DROP_WORDS, SYMBOLS, NUMBERS



def get_letters_appearances(cn):
    letters_vector = [0] * len(LETTERS_EN)
    cn_lower = cn.lower()
    for i in range(len(LETTERS_EN)):
        l = LETTERS_EN[i]
        count_l = cn_lower.count(l)
        letters_vector[i] = count_l
    return letters_vector



def get_special_symbols_appearances(cn):
    symb_vector = [0] * len(SYMBOLS)
    cn_lower = cn.lower()
    for i in range(len(SYMBOLS)):
        s = SYMBOLS[i]
        count_s = cn_lower.count(s)
        symb_vector[i] = count_s
    return symb_vector



def get_number_appearances(cn):
    numb_vector = [0] * len(NUMBERS)
    cn_lower = cn.lower()
    for i in range(len(NUMBERS)):
        n = NUMBERS[i]
        count_n = cn_lower.count(str(n))
        numb_vector[i] = count_n
    return numb_vector



def get_lev_dists_for_word(w):
    lev_dist_list = []
    for lw in LEVENSHTEIN_WORDS:
        d = levd.distance(w, lw)
        lev_dist_list.append(d)
    return lev_dist_list

def func(list):
    return sum(list)/len(list)
def get_levenshteins_avr(cn):
    cn_lower = cn.lower()

    all_words = list(set(re.findall(r'[a-z]+', cn_lower)))
    # cn_lower_letters_all_words = "".join(all_words)

    for drop_word in DROP_WORDS:
        if drop_word in all_words:
            all_words.remove(drop_word)

    if len(all_words)==0:
        all_words = list(set(re.findall(r'[a-z]+', cn_lower)))

    # lev_dist_list_all_words = get_lev_dists_for_word(cn_lower_letters_all_words)

    list_of_lev_dist_for_every_words = list(map(get_lev_dists_for_word, all_words))
    avr_lev_dist = list(map(func, zip(*list_of_lev_dist_for_every_words)))

    return avr_lev_dist

def get_levenshteins_minmax(cn):
    cn_lower = cn.lower()

    all_words = list(set(re.findall(r'[a-z]+', cn_lower)))
    # cn_lower_letters_all_words = "".join(all_words)

    for drop_word in DROP_WORDS:
        if drop_word in all_words:
            all_words.remove(drop_word)

    if len(all_words)==0:
        all_words = list(set(re.findall(r'[a-z]+', cn_lower)))

    # lev_dist_list_all_words = get_lev_dists_for_word(cn_lower_letters_all_words)

    list_of_lev_dist_for_every_words = list(map(get_lev_dists_for_word, all_words))
    min_lev_dist = list(map(min, zip(*list_of_lev_dist_for_every_words)))
    max_lev_dist = list(map(max, zip(*list_of_lev_dist_for_every_words)))

    return min_lev_dist + max_lev_dist

def get_levenshteins_min(cn):
    cn_lower = cn.lower()

    all_words = list(set(re.findall(r'[a-z]+', cn_lower)))
    # cn_lower_letters_all_words = "".join(all_words)

    for drop_word in DROP_WORDS:
        if drop_word in all_words:
            all_words.remove(drop_word)

    if len(all_words)==0:
        all_words = list(set(re.findall(r'[a-z]+', cn_lower)))

    # lev_dist_list_all_words = get_lev_dists_for_word(cn_lower_letters_all_words)

    list_of_lev_dist_for_every_words = list(map(get_lev_dists_for_word, all_words))
    min_lev_dist = list(map(min, zip(*list_of_lev_dist_for_every_words)))


    return min_lev_dist

def get_levenshteins_max(cn):
    cn_lower = cn.lower()

    all_words = list(set(re.findall(r'[a-z]+', cn_lower)))
    # cn_lower_letters_all_words = "".join(all_words)

    for drop_word in DROP_WORDS:
        if drop_word in all_words:
            all_words.remove(drop_word)

    if len(all_words)==0:
        all_words = list(set(re.findall(r'[a-z]+', cn_lower)))

    # lev_dist_list_all_words = get_lev_dists_for_word(cn_lower_letters_all_words)

    list_of_lev_dist_for_every_words = list(map(get_lev_dists_for_word, all_words))
    max_lev_dist = list(map(max, zip(*list_of_lev_dist_for_every_words)))

    return max_lev_dist




















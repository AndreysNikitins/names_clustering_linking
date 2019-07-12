import pandas as pd
import random

do_a_new_sample = True

def sample_data(more_than,less_than,samp_big,samp_small):
    df_companies_names = pd.read_excel("./data/analysts_companies_dict.xlsx")
    df_companies_names = df_companies_names[["cn", "correct_name", "error"]].copy()
    df_companies_names = df_companies_names.loc[df_companies_names["error"].isna(), ["cn", "correct_name"]].copy()

    correct_name_list = pd.unique(df_companies_names["correct_name"]).tolist()
    numbers = [i for i in range(len(correct_name_list))]
    correct_name_dict = dict(zip(correct_name_list, numbers))
    df_companies_names["company_number"] = df_companies_names["correct_name"].map(correct_name_dict)
    df = df_companies_names.reset_index()

    df_big = df[df.groupby("company_number")["company_number"].transform('size') > more_than].reset_index(drop=True)
    uniq_big = pd.unique(df_big["company_number"]).tolist()
    uniq_big_new = random.sample(uniq_big, samp_big)
    df_big = df_big[df_big["company_number"].isin(uniq_big_new)].reset_index(drop=True)
    if do_a_new_sample == True:
        print('data_taken_from_big_clusters =', len(df_big))


    df_small = df[df.groupby("company_number")["company_number"].transform('size') <= less_than].reset_index(drop=True)
    uniq_small = pd.unique(df_small["company_number"]).tolist()
    uniq_small_new = random.sample(uniq_small, samp_small)
    df_small = df_small[df_small["company_number"].isin(uniq_small_new)].reset_index(drop=True)
    if do_a_new_sample == True:
        print('data_taken_from_small_clusters =', len(df_small))

    df_used = pd.concat([df_big, df_small], ignore_index=True)
    return df_used


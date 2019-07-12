import pandas as pd
from scipy.stats import entropy


def calc_max_clust(gdf):

     max_count = gdf["clusters"].value_counts().max()
     return max_count / len(gdf)

def max_value_metric_recall(df):

    df_metric_mr_per_company = df.groupby("correct_name").apply(calc_max_clust).reset_index()
    df_metric_mr_per_company.columns = ["correct_name", "metric_mr"]

    df_company_weights = df.groupby("correct_name")[["company_number"]].count()
    df_company_weights.columns = ["n_obs"]
    df_company_weights = df_company_weights.reset_index()
    df_company_weights["weights"] = df_company_weights["n_obs"] / len(df)

    df_metrics_info = pd.merge(left=df_company_weights, right=df_metric_mr_per_company, on="correct_name", how="outer")

    df_metrics_info["metric_mr_weighted"] = df_metrics_info["metric_mr"] * df_metrics_info["weights"]

    unvalue_big_clusters = df_metrics_info["metric_mr"].mean()
    value_big_clusters = df_metrics_info["metric_mr_weighted"].sum()


    return df_metrics_info, unvalue_big_clusters, value_big_clusters



def calc_entropy_clust(gdf):
    entropy1 = entropy(list(gdf["clusters"].value_counts()/len(gdf)), base=2)
    return entropy1

def entropy_metric_recall(df):

    df_metric_er_per_company = df.groupby("correct_name").apply(calc_entropy_clust).reset_index()
    df_metric_er_per_company.columns = ["correct_name", "metric_er"]

    df_company_weights = df.groupby("correct_name")[["company_number"]].count()
    df_company_weights.columns = ["n_obs"]
    df_company_weights = df_company_weights.reset_index()
    df_company_weights["weights"] = df_company_weights["n_obs"] / len(df)

    df_metrics_info = pd.merge(left=df_company_weights, right=df_metric_er_per_company, on="correct_name", how="outer")

    df_metrics_info["metric_er_weighted"] = df_metrics_info["metric_er"] * df_metrics_info["weights"]

    unvalue_big_clusters = df_metrics_info["metric_er"].mean()
    value_big_clusters = df_metrics_info["metric_er_weighted"].sum()


    return df_metrics_info, unvalue_big_clusters, value_big_clusters



def calc_max_comp(gdf):
    max_count = gdf["company_number"].value_counts().max()
    return max_count / len(gdf)

def max_value_metric_precision(df):
    df_metric_mp_per_company = df.groupby("clusters").apply(calc_max_comp).reset_index()
    df_metric_mp_per_company.columns = ["clusters", "metric_mp"]

    df_company_weights = df.groupby("clusters")[["clusters"]].count()
    df_company_weights.columns = ["n_obs"]
    df_company_weights = df_company_weights.reset_index()
    df_company_weights["weights"] = df_company_weights["n_obs"] / len(df)

    df_metrics_info = pd.merge(left=df_company_weights, right=df_metric_mp_per_company, on="clusters", how="outer")

    df_metrics_info["metric_mp_weighted"] = df_metrics_info["metric_mp"] * df_metrics_info["weights"]

    unvalue_big_clusters = df_metrics_info["metric_mp"].mean()
    value_big_clusters = df_metrics_info["metric_mp_weighted"].sum()

    return df_metrics_info, unvalue_big_clusters, value_big_clusters



def calc_entropy_comp(gdf):
    entropy2 = entropy(list(gdf["company_number"].value_counts()/len(gdf)), base=2)
    return entropy2

def entropy_metric_precision(df):
    df_metric_ep_per_company = df.groupby("clusters").apply(calc_entropy_comp).reset_index()
    df_metric_ep_per_company.columns = ["clusters", "metric_ep"]

    df_company_weights = df.groupby("clusters")[["clusters"]].count()
    df_company_weights.columns = ["n_obs"]
    df_company_weights = df_company_weights.reset_index()
    df_company_weights["weights"] = df_company_weights["n_obs"] / len(df)

    df_metrics_info = pd.merge(left=df_company_weights, right=df_metric_ep_per_company, on="clusters", how="outer")

    df_metrics_info["metric_ep_weighted"] = df_metrics_info["metric_ep"] * df_metrics_info["weights"]

    unvalue_big_clusters = df_metrics_info["metric_ep"].mean()
    value_big_clusters = df_metrics_info["metric_ep_weighted"].sum()


    return df_metrics_info, unvalue_big_clusters, value_big_clusters


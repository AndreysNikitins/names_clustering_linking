import pandas as pd

from configs.configuration import config_list
from utils.features_composition import minmaxlev, avrlev, minlev, maxlev
from utils.metrics_calculation import max_value_metric_recall, \
            max_value_metric_precision, entropy_metric_precision
from utils.hist_and_datasave import metrics
from utils.sample_data import sample_data, do_a_new_sample

from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.cluster import MeanShift,estimate_bandwidth

from sklearn.manifold import TSNE
import plotly.graph_objs as go
from plotly import offline
from utils.plotting_utils import create_color_dict

col_name = ('Clast_conf_name, met_rec1, met_rec2, met_pre1, met_pre2, ent_pre1, ent_pre2 ' + '\n')
f = open("C:/Users/Владелец/Diplom_results/testing.csv", "w")
f.write(col_name)
f = open("C:/Users/Владелец/Diplom_results/testing.csv", "a")
f.write(','+'\n')


if do_a_new_sample == True:
    sample_data_done = sample_data(5, 5, 500, 1000)
    sample_data_done = sample_data_done.dropna()
    sample_data_done.to_csv("C:/Users/Владелец/Diplom_results/new_sampled_data.csv")
    df_companies_names = sample_data_done
else:
    df_companies_names = pd.read_csv("C:/Users/Владелец/Diplom_results/new_sampled_data.csv", engine='python')


counter = 0
print(counter)
print(' -----------------------------------')

for conf in config_list:
    if conf['alg_name'] == "MShift_minmaxlev_noscal_1comp":
        print(conf)
        companies_names_list = df_companies_names["cn"].tolist()
        companies_correct_name_list = df_companies_names["correct_name"].tolist()
        # if "AfPropagation" in conf["alg_name"]:
        #     companies_names_list = companies_names_list
        #     companies_correct_name_list = companies_correct_name_list
        # if "KMeans" in conf["alg_name"]:
        #     companies_names_list = companies_names_list
        #     companies_correct_name_list = companies_correct_name_list
        feature_list = []
        if conf["minmaxlevenstein"] == True:
            feature_list = minmaxlev(companies_names_list)
            df_with_features = pd.DataFrame(feature_list)
        if conf["minlevenstein"] == True:
            feature_list = minlev(companies_names_list)
            df_with_features = pd.DataFrame(feature_list)
        if conf["maxlevenstein"] == True:
            feature_list = maxlev(companies_names_list)
            df_with_features = pd.DataFrame(feature_list)
        if conf["avrxlevenstein"] == True:
            feature_list = avrlev(companies_names_list)
            df_with_features = pd.DataFrame(feature_list)


        for_norm = df_with_features.iloc[:,1:].values
        if conf["StandardScaler"] == True:
            scaler = StandardScaler()
            norm_done = scaler.fit_transform(for_norm)
        if conf["MinMaxScaler"] == True:
            scaler = MinMaxScaler()
            norm_done = scaler.fit_transform(for_norm)
        else:
            norm_done = for_norm
        if "MShift" in conf["alg_name"]:
            bandwidth = estimate_bandwidth(norm_done, n_samples=500)
            print(bandwidth)
            clustering_done = MeanShift(bandwidth = bandwidth, cluster_all = False)
            clustering_done.fit(norm_done)
        else:
            clustering_done = conf["algoritm_conf"]
            clustering_done.fit(norm_done)

        df_for_metrics = pd.DataFrame()
        df_for_metrics["cn"] = companies_names_list
        df_for_metrics["correct_name"] = companies_correct_name_list

        correct_name_list = pd.unique(df_for_metrics["correct_name"]).tolist()
        amount_of_comp = len(df_for_metrics)
        numbers = [i for i in range(len(correct_name_list))]
        correct_name_dict = dict(zip(correct_name_list, numbers))
        df_for_metrics["company_number"] = df_for_metrics["correct_name"].map(correct_name_dict)

        df_for_metrics["clusters"] = clustering_done.labels_


        if "DBscan" or "MShift" in conf["alg_name"]:

            if conf["without_1comp_cluster"] == False:
                amount_of_clusters = df_for_metrics['clusters'].max()
                df_for_metrics['clusters_with_minus1'] = clustering_done.labels_

                metrics_list = df_for_metrics["clusters"].tolist()
                metrics_list_final = []
                replacing_minus = amount_of_clusters + 1
                for l in metrics_list:
                    if l > -1:
                        metrics_list_final.append(l)
                    else:
                        metrics_list_final.append(replacing_minus)
                        replacing_minus += 1

                df_for_metrics["clusters"] = metrics_list_final
            else:
                amount_of_minus1 = len(df_for_metrics[df_for_metrics['clusters'] == -1])
                df_for_metrics = df_for_metrics.drop(df_for_metrics[df_for_metrics["clusters"] == -1].index).reset_index(drop=True)
        else:
            if conf["without_1comp_cluster"] == True:
                df_for_metrics = df_for_metrics[df_for_metrics.groupby('clusters')['clusters'].transform('size') > 1]



        df_for_metrics_final = df_for_metrics[["correct_name", "company_number", "clusters"]]
        print(df_for_metrics_final.head())

        mvmr = max_value_metric_recall(df_for_metrics_final)
        mvmp = max_value_metric_precision(df_for_metrics_final)
        emp = entropy_metric_precision(df_for_metrics_final)

        metrics(mvmr,mvmp,emp,conf["alg_name"])
        print(counter)
        print(' -----------------------------------')
        counter += 1


        x_embedded = TSNE(n_components=2, verbose=2).fit_transform(norm_done)

        df_tnse_features = pd.DataFrame(x_embedded, columns=["tsnec1", "tsnec2"])
        df_tnse_features["cn"] = companies_names_list
        df_tnse_features["clusters"] = clustering_done.labels_

        colors_num = sorted(pd.unique(df_tnse_features["clusters"]))
        color_dict = create_color_dict(colors_num)
        df_tnse_features["cluster_color"] = df_tnse_features["clusters"].map(color_dict)

        # map(func, list)
        # filter(func, list)
        # df.apply(func)

        trace = go.Scatter(
            x=df_tnse_features["tsnec1"].tolist(),
            y=df_tnse_features["tsnec2"].tolist(),
            mode='markers + text',
            name='Analysts Companies representation',
            # text=df_tnse_features["cn"].tolist(),
            # textposition='bottom center',
            # textfont=dict(
            #     family='sans serif',
            #     size=6
            # ),
            marker=dict(color=df_tnse_features["cluster_color"].tolist())
        )

        fig = go.Figure(data=[trace])

        offline.plot(fig, filename='analysts_companies_clustered_before_tsne_with_scaling.html')

        print()
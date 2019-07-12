import os
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def metrics(data1,data2,data3,conf_name):
    print(' unvalue_big_clusters = ', data1[1])
    print(' value_big_clusters = ', data1[2])
    print(' -----------------------------------')
    print(' unvalue_big_clusters = ', data2[1])
    print(' value_big_clusters = ', data2[2])
    print(' -----------------------------------')
    print(' unvalue_big_clusters = ', data3[1])
    print(' value_big_clusters = ', data3[2])
    print(' -----------------------------------')

    folder = os.path.join('C:/Users/Владелец/Diplom_results', conf_name)
    if not os.path.exists(folder):
        os.makedirs(folder)

    data1[0]["metric_mr"].plot.hist()
    z = os.path.join('C:/Users/Владелец/Diplom_results', conf_name, 'max_value_metric_recall.png')
    if os.path.isfile(z):
        os.remove(z)
    plt.savefig(z)
    plt.close()

    def df_graph1(df):
        df["count_equal_n_obs"] = [len(df)] * len(df)
        return df
    data1[0]["count_equal_n_obs"] = [0] * len(data1[0])
    data1_new = data1[0].groupby("n_obs").apply(df_graph1)

    sns.lmplot(x="n_obs", y="metric_mr", hue="count_equal_n_obs", palette="cubehelix",
               data=data1_new, fit_reg=False, legend=True, legend_out=False, size=10)
    z = os.path.join('C:/Users/Владелец/Diplom_results', conf_name, 'max_value_metric_recall_graph.png')
    if os.path.isfile(z):
        os.remove(z)
    plt.savefig(z)
    plt.close()

    data2[0]["metric_mp"].plot.hist()
    z = os.path.join('C:/Users/Владелец/Diplom_results', conf_name, 'max_value_metric_precision.png')
    if os.path.isfile(z):
        os.remove(z)
    plt.savefig(z)
    plt.close()

    def df_graph2(df):
        df["count_equal_n_obs"] = [len(df)] * len(df)
        return df
    data2[0]["count_equal_n_obs"] = [0] * len(data2[0])
    data2_new = data2[0].groupby("n_obs").apply(df_graph2)

    sns.lmplot(x="n_obs", y="metric_mp", hue="count_equal_n_obs", palette="cubehelix",
               data=data2_new, fit_reg=False, legend=True, legend_out=False, size=10)
    z = os.path.join('C:/Users/Владелец/Diplom_results', conf_name, 'max_value_metric_precision_graph.png')
    if os.path.isfile(z):
        os.remove(z)
    plt.savefig(z)
    plt.close()


    data3[0]["metric_ep"].plot.hist()
    z = os.path.join('C:/Users/Владелец/Diplom_results', conf_name, 'entropy_metric_precision.png')
    if os.path.isfile(z):
        os.remove(z)
    plt.savefig(z)
    plt.close()

    def df_graph3(df):
        df["count_equal_n_obs"] = [len(df)] * len(df)
        return df
    data3[0]["count_equal_n_obs"] = [0] * len(data3[0])
    data3_new = data3[0].groupby("n_obs").apply(df_graph3)

    sns.lmplot(x="n_obs", y="metric_ep", hue="count_equal_n_obs", palette="cubehelix",
               data=data3_new, fit_reg=False, legend=True, legend_out=False, size=10)
    z = os.path.join('C:/Users/Владелец/Diplom_results', conf_name, 'entropy_metric_precision_graph.png')
    if os.path.isfile(z):
        os.remove(z)
    plt.savefig(z)
    plt.close()

    data = (conf_name + ',' + str(data1[1])+ ',' + str(data1[2]) + ',' +str(data2[1]) + ',' + str(data2[2])
           +','+ str(data3[1])+','+str(data3[2])+ ',' + '\n')
    f = open("C:/Users/Владелец/Diplom_results/testing.csv", "a")
    f.write(data)
    f.close()
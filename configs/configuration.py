from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import AffinityPropagation


KMeans1 = KMeans(n_clusters=1600, max_iter = 750)
KMeans2 = KMeans(n_clusters=1700, max_iter = 750)
KMeans3 = KMeans(n_clusters=1100, max_iter = 1000)
KMeans4 = KMeans(n_clusters=1300, max_iter = 500)
DBscan1 = DBSCAN(eps=3.5, min_samples=2)
DBscan2 = DBSCAN(eps=7.5, min_samples=2)
DBscan3 = DBSCAN(eps=6.5, min_samples=2)
DBscan4 = DBSCAN(eps=5.5, min_samples=2)
DBscan01 = DBSCAN(eps=0.05, min_samples=2)
DBscan02 = DBSCAN(eps=0.3, min_samples=2)
DBscan03 = DBSCAN(eps=0.5, min_samples=2)
DBscan04 = DBSCAN(eps=0.7, min_samples=2)
AfPropagation1 = AffinityPropagation(damping=0.5,max_iter=200)
AfPropagation2 = AffinityPropagation(damping=0.6,max_iter=250)
AfPropagation3 = AffinityPropagation(damping=0.8,max_iter=350)


configs_DBscan1 = [{"alg_name":"DBscan_eps_3.5","algoritm_conf": DBscan1},{"alg_name":"DBscan_eps_7.5","algoritm_conf": DBscan2},
                  {"alg_name":"DBscan_eps_6.5","algoritm_conf": DBscan3},{"alg_name":"DBscan_eps_5.5","algoritm_conf": DBscan4}]

configs_DBscan01 = [{"alg_name":"DBscan_eps0.05","algoritm_conf": DBscan01},{"alg_name":"DBscan_eps0.3","algoritm_conf": DBscan02},
                    {"alg_name":"DBscan_eps0.5","algoritm_conf": DBscan03},{"alg_name":"DBscan_eps0.7","algoritm_conf": DBscan04}]

configs_KMeans = [{"alg_name":"KMeans_iter500","algoritm_conf": KMeans1},{"alg_name":"KMeans_iter750","algoritm_conf": KMeans2},
                  {"alg_name":"KMeans_iter1000","algoritm_conf": KMeans3},{"alg_name":"KMeans_nc1100_iter1000","algoritm_conf": KMeans4}]

configs_AfPropagation = [{"alg_name":"AfPropagation_damp0.5","algoritm_conf": AfPropagation1},{"alg_name":"AfPropagation_damp0.6","algoritm_conf": AfPropagation2},
                  {"alg_name":"AfPropagation_damp0.8","algoritm_conf": AfPropagation3}]

# configs_MShift =[{"alg_name":"MShift","minmaxlevenstein":False,"minlevenstein":True, "maxlevenstein":False,"avrxlevenstein":False,
#                      "StandardScaler": False,"MinMaxScaler": False,"without_1comp_cluster": False,},
#                  {"alg_name":"MShift","minmaxlevenstein":False,"minlevenstein":True, "maxlevenstein":False,"avrxlevenstein":False
#                      ,"StandardScaler": False,"MinMaxScaler": True,"without_1comp_cluster": False},
#                  {"alg_name":"MShift","minmaxlevenstein":False,"minlevenstein":True, "maxlevenstein":False,"avrxlevenstein":False,
#                      "StandardScaler": False,"MinMaxScaler": False,"without_1comp_cluster": True},
#                  {"alg_name":"MShift","minmaxlevenstein":False,"minlevenstein":True, "maxlevenstein":False,"avrxlevenstein":False,
#                      "StandardScaler": False,"MinMaxScaler": True,"without_1comp_cluster": True}]

configs_MShift =[{"alg_name":"MShift"}]

configs_final = configs_DBscan1 + configs_DBscan01 + configs_AfPropagation + configs_KMeans + configs_MShift
#configs_final = configs_DBscan1[1:2]

config_lev = [ {"minmaxlevenstein":True,"minlevenstein":False, "maxlevenstein":False,"avrxlevenstein":False,"name":"_minmaxlev"},
               {"minmaxlevenstein":False,"minlevenstein":True, "maxlevenstein":False,"avrxlevenstein":False,"name":"_minlev"},
               {"minmaxlevenstein":False,"minlevenstein":False, "maxlevenstein":True,"avrxlevenstein":False,"name":"_maxlev"},
               {"minmaxlevenstein":False,"minlevenstein":False, "maxlevenstein":False,"avrxlevenstein":True,"name":"_avrlev"}]

config_Scal = [{"StandardScaler": False,"MinMaxScaler": False,"name":"_noscal"},
               {"StandardScaler": True,"MinMaxScaler": False,"name":"_Stscal"},
               {"StandardScaler": False,"MinMaxScaler": True,"name":"_MinMaxscal"}]

config_1comp_cluster = [{"without_1comp_cluster": False,"name":"_1comp"},
                        {"without_1comp_cluster": True,"name":"_no1comp"}]

def asseble_conf(configs):
    assembled_config_list = []
    for set_start in configs:
        set = set_start.copy()
        for lev in config_lev:
            set1 = set.copy()
            set1.update(lev)
            del set1["name"]
            set1["alg_name"] += lev["name"]
            if "DBscan_eps0" in set1["alg_name"]:
                config_Scal_final = config_Scal[1:]
            elif "DBscan_eps_" in set1["alg_name"]:
                config_Scal_final = [config_Scal[0]]
            else:
                config_Scal_final = config_Scal
            for scal in config_Scal_final:
                set2 = set1.copy()
                set2.update(scal)
                del set2["name"]
                set2["alg_name"] += scal["name"]
                for comp in config_1comp_cluster:
                    set3 = set2.copy()
                    set3.update(comp)
                    del set3["name"]
                    set3["alg_name"] += comp["name"]
                    assembled_config_list.append(set3)
    return assembled_config_list

config_list = asseble_conf(configs_final)



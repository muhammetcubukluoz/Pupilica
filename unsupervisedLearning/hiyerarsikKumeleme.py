import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

X, _ = make_blobs(n_sample = 300, centers = 4, cluster_std= 0.5, random_state=0)


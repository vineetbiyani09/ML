
def cluster_selection(dataset, method, metric):
  
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import scipy.cluster.hierarchy as sch
  from sklearn.cluster import KMeans

  #i = 0
  print('in function')

  wcss = []     # within cluster sum of squares
  for k in range(1, 11):
    kmeans = KMeans(n_clusters = k, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
  plt.plot(range(1, 11), wcss)
  plt.title('The Elbow Method')
  plt.xlabel('Number of clusters')
  plt.ylabel('WCSS')
  plt.show()

  for i in range(0,len(metric)):
    for j in range(0,len(method)):
      
      sch.dendrogram(sch.linkage(X, method = method[j], metric = metric[i]))
      
      plt.title('Dendrogram Method: {}'.format(method[j]))
      plt.xlabel('Customers')
      plt.ylabel('Distance {}'.format(metric[i]))
      plt.show()

      





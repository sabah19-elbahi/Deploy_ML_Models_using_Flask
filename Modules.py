import pymongo 
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams
import pickle

rcParams['figure.figsize'] = 10, 5

client = pymongo.MongoClient('localhost')
customers = client.spring.customers

save_folder = 'static/images/'


class ChartMaker:
  def __init__(self):
      client = pymongo.MongoClient('localhost')
      customers = client.spring.customers
      cursor = customers.find()
      entries = list(cursor)
      self.df_customer = pd.DataFrame(entries)
  def Histogramme(self,field):
      self.df_customer[field].hist()
      plt.title(field+' Histogramme')
      plt.savefig(save_folder+field+"_hist")
      plt.clf()
  def CountPlot(self):
      sns.countplot(x='gender', data=self.df_customer)
      plt.title('gender countplot')
      plt.savefig(save_folder+'gender_count')
      plt.clf()
  def Clusters(self):
      model = pickle.load(open("model.pkl", 'rb'))
      df_customer = self.df_customer
      X = df_customer[['income', 'score']]
      y_predicted = model.fit_predict(X)
      df_customer['cluster'] = y_predicted
      X = X.values
      plt.scatter(X[y_predicted==0,0],X[y_predicted==0,1],s=50, c='purple',label='Cluster1')
      plt.scatter(X[y_predicted==1,0],X[y_predicted==1,1],s=50, c='blue',label='Cluster2')
      plt.scatter(X[y_predicted==2,0],X[y_predicted==2,1],s=50, c='green',label='Cluster3')
      plt.scatter(X[y_predicted==3,0],X[y_predicted==3,1],s=50, c='cyan',label='Cluster4')
      plt.scatter(X[y_predicted==4,0],X[y_predicted==4,1],s=50, c='yellow',label='Cluster5')

      plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1],s=200,marker='s', c='red', alpha=0.7, label='Centroids')
      plt.title('Customer segments')
      plt.xlabel('Annual income of customer')
      plt.ylabel('Annual spend from customer on site')
      plt.legend()

      plt.savefig(save_folder+'final_cluster')
      plt.clf()

      

#cm = ChartMaker()
#cm.Histogramme("income")
#cm.Histogramme("age")
#cm.Histogramme("score")
#cm.CountPlot()












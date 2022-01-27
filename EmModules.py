import pymongo 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams
rcParams['figure.figsize'] = 10, 5

client = pymongo.MongoClient('localhost')
customers = client.spring.customers

sv_folder = 'static/images/em/'


class EmChartMaker:
  def __init__(self):
      client = pymongo.MongoClient('localhost')
      li = client.spring.emdata
      cursor = li.find()
      entries = list(cursor)
      self.df_dt = pd.DataFrame(entries)
  def Histogramme(self,field):
      self.df_dt[field].hist()
      plt.title(field+' Histogramme')
      plt.savefig(sv_folder+field+"_hist")
      plt.clf()
  def FinalCluster(self):
    print("blati")
      

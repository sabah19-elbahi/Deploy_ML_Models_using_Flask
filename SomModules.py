import pymongo 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import rcParams
rcParams['figure.figsize'] = 10, 5

client = pymongo.MongoClient('localhost')
customers = client.spring.customers

smsv_folder = 'static/images/som/'


class SomChartMaker:
  def __init__(self):
      client = pymongo.MongoClient('localhost')
      li = client.spring.credit
      cursor = li.find()
      entries = list(cursor)
      self.df_dt = pd.DataFrame(entries)
  def Histogramme(self,field):
      self.df_dt[field].hist()
      plt.title(field+' Histogramme')
      plt.savefig(smsv_folder+field+"_hist")
      plt.clf()

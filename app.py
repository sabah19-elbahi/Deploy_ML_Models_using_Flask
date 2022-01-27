import os
import numpy as np
import pickle
from flask_cors import CORS, cross_origin    
from flask import Flask, redirect, url_for, request, render_template,jsonify
from Modules import ChartMaker
from EmModules import EmChartMaker
from SomModules import SomChartMaker
import pickle


imgs = 'static/images/'
imgs_em = 'static/images/em/'

imgs_sm = 'static/images/som/'

# creating instance of the class
app = Flask(__name__, template_folder='templates')
CORS(app)
    
    
# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,2)
    loaded_model = pickle.load(open("model.pkl","rb")) # load the model
    result = loaded_model.predict(to_predict) # predict the values using loded model
    print(result)
    return result[0]


@app.route('/predict', methods = ['GET'])
def preduct():
    if request.method == 'GET':
        income = request.args.get("income")
        score = request.args.get("score")
        to_predict_list = [income,score]
        print(to_predict_list)
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list)
        result = ValuePredictor(to_predict_list)
        result = {
                    "predicted_cluster":int(result),
                    #"cluster_description": addvariablehere
                  }
        print(result)
        return jsonify(result)


# kmeans histograms
@app.route('/graphs/histo', methods = ['GET'])
def getHisto():
    if request.method == 'GET':
        field = request.args.get("field")
        result = {
                    "image_title": field+"_hist",
                    "image_url":   "http://127.0.0.1:5000/"+imgs+field+"_hist.png",
                    
                  }
        return jsonify(result)
#kmeans gender countplot
@app.route('/graphs/count', methods = ['GET'])
def getCountPlot():
    if request.method == 'GET':
        result = {
                    "image_title": "gender_countplot",
                    "image_url":   "http://127.0.0.1:5000/"+imgs+"gender_count.png",
                    
                  }
        return jsonify(result)

#kmeans clusters
@app.route('/graphs/clusters', methods = ['GET'])
def getClusters():
    if request.method == 'GET':
        result = {
                    "image_title": "gender_countplot",
                    "image_url":   "http://127.0.0.1:5000/"+imgs+"final_cluster.png",
                    
                  }
        return jsonify(result)

# em histograms
@app.route('/em/graphs/histo', methods = ['GET'])
def getEmHisto():
    if request.method == 'GET':
        field = request.args.get("field")
        result = {
                    "image_title": field+"_hist",
                    "image_url":   "http://127.0.0.1:5000/"+imgs_em+field+"_hist.png",
                    
                  }
        return jsonify(result)


# som histograms
@app.route('/som/graphs/histo', methods = ['GET'])
def getSomHisto():
    if request.method == 'GET':
        field = request.args.get("field")
        result = {
                    "image_title": field+"_hist",
                    "image_url":   "http://127.0.0.1:5000/"+imgs_sm+field+"_hist.png",
                    
                  }
        return jsonify(result)

# refresh all graphs
@app.route('/graphs/refresh', methods = ['GET'])
def RefreshGraphs():
    if request.method == 'GET':
        cm = ChartMaker()
        numerical = {'income','age','score'}
        for i in numerical:
          cm.Histogramme(i)
        cm.CountPlot()
        cm.Clusters()

        emcm = EmChartMaker()
        columns = {'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'}
        for i in columns:
          emcm.Histogramme(i)


        smcm = SomChartMaker()
        clms = {'A1', 'A2', 'A3', 'A4'}
        for i in clms:
          smcm.Histogramme(i)
          

        result = {"message": "Graphs have been updated succesfully !"}
        return jsonify(result)





if __name__ == "__main__":
    app.run(debug=True) # use debug = False for jupyter notebook
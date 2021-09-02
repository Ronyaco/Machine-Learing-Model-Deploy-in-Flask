from flask import Flask, render_template , request
from numpy import dtype
from numpy.core import records
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import uuid
import pickle
from pandas.io.json import json_normalize
import json


app = Flask(__name__)



@app.route('/predict',methods=['POST'])
def predict():

    ##start_date = request.form.get('start_date')
    ##end_date = request.form.get('end_date')
    ##start_date  and end_date
    ##random_str = uuid.uuid4().hex
    ##path = 'static/'+random_str+'.svg'

    # Creating the data model
    df = pd.read_csv('D:\\Data Science\\Portfolio\\Machine Learing Model Deploy in Flask\\model_creation\\routes.csv')
    df['date'] = pd.to_datetime(df.date)
    df["year"] = pd.to_numeric(df["year"], downcast="integer")
    df["rev_passengers"] = pd.to_numeric(df["rev_passengers"], downcast="float")
    df = df.loc[(df['year'] <= 2019) ]
    data_model =df[['date', 'rev_passengers']]
    data_model = data_model.reset_index(drop=True)
    data_model = data_model.groupby('date').sum()
    #sampling, getting index out column date
    data_model = data_model.resample(rule='M').sum()
    ##make_picture(data_model,model,start_date,end_date,path)
    model = pickle.load(open('D:\\Data Science\\Portfolio\\Machine Learing Model Deploy in Flask\\model_creation\\data\\model.pkl','rb'))
    pred = model.predict(start='2014-08-31', end='2022-10-31')
    pred = pred.astype(int)
    pred.index = pd.to_datetime(pred.index, format = '%Y/%m/%d').strftime('%m-%Y')
    result = pred.to_json(orient="table")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4)
     
      
    ##return render_template('index.html', href=path)

@app.route('/', methods=['GET', 'POST'])
def home ():
    return render_template('index.html', href='static/base_pic.svg')


def make_picture(data_model,model,date_start,date_end,output_file):
    #data_model = pd.read_csv(data_model)  
    pred = model.predict(start=date_start, end=date_end)
    fig = px.line( data_frame = data_model, x = data_model.index, y=data_model.rev_passengers,
                title = "Sydney - Melbourne Revenue", labels = {'x':'Month','y':'Revenue(AUD)'})
    fig.add_trace(go.Scatter(x=pred.index, y = pred , name = 'Holt - Winters Prediction'))
    fig.write_image(output_file, width = 800 , engine = 'kaleido' )
    fig.show()
  # Papi no esta generando el segundo graph
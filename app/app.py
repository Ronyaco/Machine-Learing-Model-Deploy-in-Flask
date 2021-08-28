from flask import Flask, render_template , request
from joblib import load
from statsmodels.tsa.holtwinters.results import HoltWintersResultsWrapper
import pickle
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', href='static/base_pic.svg')
    else:
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        start_date  and end_date
        path = 'static/prediction.svg'

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



        model = pickle.load(open('D:\\Data Science\\Portfolio\\Machine Learing Model Deploy in Flask\\model_creation\\data\\model.pkl','rb'))
        make_picture(data_model,model,start_date,end_date,path)
        return render_template('index.html', href=path)
data_model = "D:\\Data Science\\Portfolio\\Machine Learing Model Deploy in Flask\\model_creation\\data_model.csv"

def make_picture(data_model,model,date_start,date_end,output_file):
  pred = model.predict(start=date_start, end=date_end)
  fig = px.line( data_frame = data_model, x = data_model.index, y=data_model.rev_passengers  , 
              title = "Sydney - Melbourne Revenue", labels = {'x':'Month','y':'Revenue(AUD)'})
  fig.add_trace(go.Scatter(x=pred.index, y = pred , name = 'Holt - Winters Prediction'))
  fig.write_image(output_file, width = 800 , engine = 'kaleido' )
import pandas as pd
import statsmodels.api 
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import plotly.express as px
import plotly.graph_objects as go
import pickle


model = ExponentialSmoothing(data_model, seasonal='mul', seasonal_periods=12).fit()#sesonality seems to be multiplicative
pred = model.predict(start='2014-07-31', end='2019-12-31')

pickle.dump(model,open('D:\\Data Science\\Portfolio\\Machine Learing Model Deploy in Flask\\model_creation\\data\\model.pkl','wb'))

model_in = pickle.load(open('D:\\Data Science\\Portfolio\\Machine Learing Model Deploy in Flask\\model_creation\\data\\model.pkl','rb'))


def make_picture(training_data_filename,model,date_start,date_end,output_file):
  data = pd.read_csv(training_data_filename)
  pred = model.predict(start=2019-12-31, end=2019-12-31)
  fig = px.line( data_frame = data_model, x = data_model.index, y=data_model.rev_passengers  , 
              title = "Sydney - Melbourne Revenue", labels = {'x':'Month','y':'Revenue(AUD)'})
  fig.add_trace(go.Scatter(x=pred.index, y = pred , name = 'Holt - Winters Prediction'))
  fig.write_image(output_file, width = 800 , )
  fig.show() 

data_file='D:\\Data Science\\Portfolio\\Machine Learing Model Deploy in Flask\\model_creation\\data\\data_model.csv'

make_picture(data_file,model_in,'2014-07-31','2015-12-31')

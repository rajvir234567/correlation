# getting data 
# finding relation
# plotting graph

import pandas as pd
import plotly.express as px
import numpy as np

def find_correlation(x, y, df):
    list_x = df[x].tolist()
    print(y)
    list_y = df[y].tolist()
    correlation = np.corrcoef(list_x, list_y)
    print(f"correlation between {x} and {y} is ", correlation[0,1])

def plot_chart(df, x, y):
    chart = px.scatter(df, x = x, y = y, size = x)
    chart.show()

def getData(filename, x_col, y_col):
    df = pd.read_csv(filename)
    find_correlation(x_col,y_col, df)
    plot_chart(df, x_col, y_col)

getData("ice-cream.csv", "Temperature", "Ice-cream Sales( ₹ )")
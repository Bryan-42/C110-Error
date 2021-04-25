import csv
import random
import statistics
import pandas as pd
import plotly.express as go
import plotly.figure_factory as ff

df = pd.read_csv("Average.csv")
data = df["Marks In Percentage"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

populationMean = statistics.mean(data)
fig = go.scatter( x = mean, y = "Marks In Percentage")
fig.show()
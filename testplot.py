import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import plotly
import plotly.express as px

df = pd.read_csv("StudentsPerformance.csv")

fig = px.bar(df, x='gender', color="gender", title="Total number students",
            labels={
                     "gender": "Gender",
                     "count": "Count"
                 }
            )
fig.show()

fig.write_image("test1.png") 
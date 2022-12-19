# loads the necessary modules
from numpy import True_
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loads the titanic dataset
titanic = pd.read_csv("https://static-resources.zybooks.com/static/titanic.csv")

# sets the style of the bar charts
sns.set(style="whitegrid", color_codes=True_)

# title
plt.title('Titanic passengers by class', fontsize=20)

# plots a horizontal bar chart
sns.countplot(y="class", color="b", data=titanic);

# saves the image
plt.savefig("horizontlbarchart.png")

# shows the image
plt.show()
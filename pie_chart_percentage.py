# loads the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns

# loads the titanic dataset
df = sns.load_dataset("titanic")

# counts the number of passengers for each class
a = df[df.pclass == 1]["pclass"].count()
b = df[df.pclass == 2]["pclass"].count()
c = df[df.pclass == 3]["pclass"].count()

# data to plot
labels = 'First', 'Second', 'Third'
sizes = [a, b, c]

# plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# title
plt.title('Titanic passengers by class', fontsize=20)

# legend
patches, texts = plt.pie(sizes)
plt.legend(patches, labels, loc="lower right")

# produces a perfectly circular chart
plt.axis('equal')

# saves the image
plt.savefig("piechart.png")

# shows the image
plt.show()
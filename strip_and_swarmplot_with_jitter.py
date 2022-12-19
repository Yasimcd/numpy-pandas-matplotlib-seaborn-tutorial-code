# loads the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# loads the titanic dataset
titanic = sns.load_dataset("titanic")

# title
plt.title('Fares paid by passengers of the Titanic by deck', fontsize=20)

# create plot(set jitter to true)
sns.stripplot(x="deck", y="fare", jitter=True, data=titanic);

# saves the image
plt.savefig("titanicstripplotwithjitter.png")

# shows the image
plt.show()
# load and summarise the sonar dataset
import pandas as pd
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/sonar.csv"
dataset = read_csv(url, header=None)

# summaries each variable
desc = dataset.describe()


# histograms of the variables
dataset.hist()
pyplot.show()





































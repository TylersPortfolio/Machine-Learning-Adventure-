import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


# Load Iris Dataset

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
dataset = pandas.read_csv(url, names=names)

# Shape of the Data
#print(dataset.shape)

#------------------------------------------#

# Head of the Data
#print(dataset.head(40))

#------------------------------------------#

# Discriptions of Dataset
#print(dataset.describe())

#------------------------------------------#

# class distribution of Data
#print(dataset.groupby("class").size())

#------------------------------------------#

# Box and Whisker Plots of Iris Data
#dataset.plot(kind = "box", subplots = True, layout = (2, 2), sharex = False, sharey = False,)
#plt.show()

#------------------------------------------#

# Histogram of Data
#dataset.hist()
#plt.show()

#------------------------------------------#

# Scatter Plot Matrix
#scatter_matrix(dataset)
#plt.show()

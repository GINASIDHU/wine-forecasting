import pandas as pd
from matplotlib import pyplot as plt
red = pd.read_csv(r'C:\Users\gisidhu\Documents\gurgina SIDHU\Data Science Material\DataSets\Red.csv')
red.head(5)
type(red)
plt.plot(red.Price, red.Year)
plt.show()


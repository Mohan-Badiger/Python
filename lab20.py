#python program to implement histogram and pie chart
import numpy as np
import matplotlib.pyplot as plt
heights=np.random.normal(170,2,100)
plt.figure(figsize=(10,8))
plt.subplot(2,1,1)
plt.hist(heights)
plt.title("Histogram showing distrubution of hright of person")
plt.xlabel("Height of Peroson")
plt.ylabel("Number of observed values")
plt.subplot(2,1,2)
fruits=['appple','banana','mango','orange']
pricess=[2000,1200,3000,560]
plt.pie(pricess,labels=fruits)
plt.grid(True)
plt.tight_layout()
plt.show()

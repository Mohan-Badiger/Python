#python program to demonstrate barchat and linechat using matplot lip
#Create 12months temperature data using arrays show the line chart of tempreture over the months
#Create 4 quarters tempreture data using arrays 
#Show the bar chart of diffent quarters

import numpy as np
import matplotlib.pyplot as plt
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
temp=np.array([20,23,23,28,26,32,29,20,22,21,24,25])
quarter=['Quarter1','Quarter2','Quarter3','Quarter4']
tempquarter=[25,28,33,30]
plt.figure(figsize=(12,8))
plt.subplot(2,1,1)
plt.plot(months,temp,linestyle='-',color='b',marker='o')
plt.xlabel("Months")
plt.ylabel("Temprature")
plt.title("Line chart of showing temprature of 12 months")
plt.legend(months)
plt.subplot(2,1,2)
plt.bar(quarter,tempquarter,color=['red','green','blue','yellow'])
plt.xlabel("Quarters")
plt.ylabel("Temprature data")
plt.title("Temprature data of four quarters in year shown using barchart")
plt.legend(quarter)
plt.grid(True)
plt.tight_layout()
plt.show()

#python program to implement numpy array operation
#perform the sales data analysis using numpy 
#1.create 14days of sales data in an array
#2.find the sum of sales for the first week
#3.find the sum of sales for the second week
#4.find the average sales of both weeks
#5.find the sales which are accured greater than 2000rs
#6.find the highest sales data
#7.find the lowest sales data
import numpy as np
salesdata=np.array([2100,1200,1400,1600,1300,2200,1294,2399,3200,2000,3890,1200,1800,2500])
print("14 days sales are as follows")
for i in range(0,len(salesdata)):
    print(f"Day {i+1}={salesdata[i]}")
firstweek=salesdata[0:7]
totalsalesofweek1=np.sum(firstweek)
secondweek=salesdata[7:]
totalsalesofweek2=np.sum(secondweek)
print("First week data is")
for i in range(0,7):
    print(f"Day{i+1}={salesdata[i]}")
print("Second week data is")
for i in range(7,len(salesdata)):
    print(f"Day{i+1}={salesdata[i]}")
print(f"total sales of first week={totalsalesofweek1}")
print(f"total sales of second week={totalsalesofweek2}")
avgsales=np.mean(salesdata)
print(f"average sales for 14 days ={avgsales}")
salesgt2000=salesdata[salesdata>2000]
print("the sales data greater than 2000")
print(salesgt2000)
print(f"heighest sales data={np.max(salesdata)}")
print(f"lowest sales data={np.min(salesdata)}")

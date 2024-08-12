#Write a python program to demonstrate data analysis by reading excel file using pandas library.
#Create a sales data CSV file with following columns
#1.ID 2.Product 3.Quantity 4.Price
#Read the CSV file into a dataframe
#Calculate amount for each product
#Calculate the total sales
#Calculate the average sales per product
#Draw the barchart showing total sales per product
#a pie chart showing the percentage of total fees per unit

import pandas as pd
df=pd.DataFrame({'rollno':[1,2,3,4,5],'name':['anand','chetan','kirana','mohan','ashwath'],'fees':[1000,1500,1300,1600,1200],'course':['BBA','BCA','BCA','BCOM','BCA']})
print(df)
#synatx to create new column existing dataframe
#df['columname']=expression
df['gender']=['male','male','female','male','male']
print(df)
#adding uniform column with 10% of fee
df['uniform']=df['fees']/100*10
print(df)
#synatax to perform group by operation
#if single column :
#df.groupby('columname').function_name().reset_index()
#if multiple column
#df.groupby('columnname')['columname'].function_name().reset_index()
course_total_fees=df.groupby('course')['fees'].sum().reset_index()
course_total_fees.columns=['course','total_fees']#set the names of columns
print(course_total_fees)

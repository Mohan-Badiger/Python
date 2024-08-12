import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('salesdata.xlsx')
df['Amt']=df['Qty']*df['Price']
print(df)
total_sales=df['Amt'].sum()
print(f"total sales amt={total_sales}")
avg_sales_each_product=df.groupby ('Product') ['Amt'].mean().reset_index()
avg_sales_each_product.columns=['product','average sales']
print(avg_sales_each_product)
total_sales_each_product=df.groupby('Product') ['Amt'].sum().reset_index()
total_sales_each_product.columns=['Product','total_sales']
print(total_sales_each_product)
# total_sales_each_product.plot(kind='bar',xlabel='Product',ylabel='Total sales each product')
# plt.show()
plt.figure(figsize=(10,8))
plt.subplot(2,1,1)
plt.bar(height=total_sales_each_product['total_sales'],x=['A','B'],color=['red','blue'])
plt.legend()
plt.title("Bar chart showing total sales for each product")
plt.xlabel("Product Names")
plt.ylabel("Total sales")
plt.subplot(2,1,2)
plt.pie(total_sales_each_product['total_sales'],labels=['A','B'],autopct='% 1.1f%%')
plt.title("Pie chart showing percentage of total sales of each product")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
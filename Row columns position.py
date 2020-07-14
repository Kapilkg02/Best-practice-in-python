
import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

# Remove duplicates by variable
n2 = new_data.drop_duplicates(["Manufacturer","Horsepower"])

# row positon
n1= new_data.loc[20:40]
# or
new_data[20:40] # 39 will apppear it  always n-1 i.e 40-1 = 39 rows will come

#select all column between two variables
new_data.loc[:, "Sales_in_thousands" :"Vehicle_type"]

# keeping variables by their postion. 0 is first variable
new_data.iloc[:,[0,2,4,6,8,9]]


n1 = new_data.loc[20:40]
n2 =new_data.loc[60:70]
# appendding dataset with same columns names
n3 = pd.concat([n1,n2])









# Saving dataset in folder;
new_da = n2and
new_da.to_excel("D:\Python Video\df.xlsx")
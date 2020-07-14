import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

# transposing the dataset as per row and values
n1 = new_data.pivot(columns="Manufacturer", values = "Price_in_thousands")
n1
#replacing nan by mean
n1.Acura.fillna(n1.Acura.mean(), inplace=True)

#concatinating dataset
n1 = new_data.loc[20:40]
n2 =new_data.loc[60:70]
# appendding dataset with same columns names
n3 = pd.concat([n1,n2])


new_data.Price_in_thousands.shift(-1)
n1 = new_data.Price_in_thousands.shift(2)
n3 = pd.concat([new_data,n1],axis =1)
n3.columns
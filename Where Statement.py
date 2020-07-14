import pandas as pd
new_data = pd.read_excel("D:\Car_sales.xlsx", sheet_name="car")

#where statement ;slicing the dataset ;
n1 = new_data[:][new_data.Manufacturer=="BMW"]
n1
# and conditon #two or more condition
n2 = new_data["__year_resale_value"][(new_data.Horsepower>=150.) & (new_data.Engine_size >=new_data.Engine_size.mean())]
n3 = new_data[:][((new_data.Manufacturer == "Acura") & (new_data.Horsepower>=150) )  ]
n4 = new_data[(new_data.Sales_in_thousands > new_data.Sales_in_thousands.mean()) | new_data.Horsepower <3]

n1=new_data[["Manufacturer","__year_resale_value"]][(new_data.Vehicle_type =="Passenger") &(new_data.Engine_size >=new_data.Engine_size.mean())]
n2 = n1[n1.__year_resale_value.notnull()]
n2



df=pd.DataFrame({'Name':['JOHN','ALLEN','BOB','NIKI','CHARLIE','CHANG'],
              'Age':[35,42,63,29,47,51],
              'Salary_in_1000':[100,93,78,120,64,115],
             'FT_Team':['STEELERS','SEAHAWKS','FALCONS','FALCONS','PATRIOTS','STEELERS']})
df
n1 = df[(df.Age>50) & (df.Salary_in_1000 >80)] # AND condition
n2 = df[(df.Age>50) | (df.Salary_in_1000 >80)] # OR condition
n2
